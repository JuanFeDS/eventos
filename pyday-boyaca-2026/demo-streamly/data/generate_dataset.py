"""Genera el dataset sintetico de churn de Streamly en formato panel mensual."""

import numpy as np
import pandas as pd

SEMILLA = 42
NUMERO_CLIENTES = 15000
MESES_MAXIMOS = 6
RUTA_SALIDA = "streamly_churn.csv"
PREVALENCIA_SEGMENTO_EN_RIESGO = 0.22

PAISES = ["CO", "MX", "AR", "CL", "PE"]
PESOS_PAISES = [0.45, 0.20, 0.15, 0.10, 0.10]

CIUDADES_POR_PAIS = {
    "CO": ["Bogota", "Medellin", "Cali", "Barranquilla", "Bucaramanga"],
    "MX": ["Ciudad de Mexico", "Guadalajara", "Monterrey"],
    "AR": ["Buenos Aires", "Cordoba"],
    "CL": ["Santiago", "Valparaiso"],
    "PE": ["Lima", "Arequipa"],
}

PLANES = ["basico", "estandar", "premium"]
PESOS_PLANES = [0.35, 0.40, 0.25]
PRECIO_BASE_PLAN = {"basico": 15000, "estandar": 28000, "premium": 45000}

METODOS_PAGO = ["tarjeta_credito", "tarjeta_debito", "pse", "paypal"]
PESOS_METODOS_PAGO = [0.50, 0.25, 0.15, 0.10]


def generar_clientes(numero_clientes, rng):
    """Genera los atributos estaticos y latentes de cada cliente."""
    paises = rng.choice(PAISES, size=numero_clientes, p=PESOS_PAISES)
    ciudades = [rng.choice(CIUDADES_POR_PAIS[pais]) for pais in paises]
    planes = rng.choice(PLANES, size=numero_clientes, p=PESOS_PLANES)
    precios = [
        round(PRECIO_BASE_PLAN[plan] * rng.uniform(0.90, 1.10) / 100) * 100
        for plan in planes
    ]

    return pd.DataFrame({
        "customer_id": np.arange(1, numero_clientes + 1),
        "age": np.clip(rng.normal(35, 10, numero_clientes).round(), 18, 70).astype(int),
        "country": paises,
        "city": ciudades,
        "plan": planes,
        "monthly_price": precios,
        "payment_method": rng.choice(METODOS_PAGO, size=numero_clientes, p=PESOS_METODOS_PAGO),
        "initial_tenure": np.clip(rng.exponential(12, numero_clientes).round(), 1, 60).astype(int),
        "engagement_baseline": rng.normal(0, 1, numero_clientes),
        "complaint_proneness": rng.exponential(1, numero_clientes),
        "financial_risk": rng.uniform(0, 1, numero_clientes),
        "en_riesgo": rng.random(numero_clientes) < PREVALENCIA_SEGMENTO_EN_RIESGO,
    })


def simular_comportamiento_mes(cliente, rng):
    """Simula las columnas de comportamiento e interacciones de un cliente en un mes dado."""
    baseline = cliente["engagement_baseline"]

    sesiones = rng.poisson(max(0.5, 8 + 6 * baseline))
    horas_vistas = max(0.0, round(sesiones * rng.uniform(0.4, 1.2) + rng.normal(0, 1), 1))
    contenidos_unicos = min(sesiones, max(0, round(sesiones * rng.uniform(0.4, 0.9))))
    tasa_finalizacion = float(np.clip(rng.normal(0.5 + 0.1 * baseline, 0.15), 0, 1))
    dias_sin_entrar = int(np.clip(round(rng.normal(15 - 10 * baseline, 5)), 0, 30))
    dispositivos = int(np.clip(round(rng.normal(1.5 + 0.3 * baseline, 0.7)), 1, 5))

    tickets_soporte = int(rng.poisson(max(0.05, 0.3 * cliente["complaint_proneness"])))
    reclamos = int(rng.binomial(tickets_soporte, 0.6)) if tickets_soporte > 0 else 0
    pagos_fallidos = int(rng.poisson(max(0.02, 0.5 * cliente["financial_risk"])))

    return {
        "sessions_last_30d": int(sesiones),
        "hours_watched": horas_vistas,
        "unique_content_last_30d": int(contenidos_unicos),
        "completion_rate": round(tasa_finalizacion, 2),
        "days_since_last_login": dias_sin_entrar,
        "devices_used": dispositivos,
        "support_tickets": tickets_soporte,
        "complaints": reclamos,
        "failed_payments": pagos_fallidos,
    }


def calcular_probabilidad_churn(comportamiento, subscription_months, en_riesgo, rng):
    """Calcula la probabilidad de churn del mes.

    en_riesgo es un segmento oculto por cliente (satisfaccion, competencia,
    motivos personales) que no se observa en ninguna columna del dataset y
    domina el logit a proposito: es lo que un modelo solo puede explotar si
    detecta -via columnas casi identicas entre meses- que dos filas
    pertenecen al mismo cliente, en vez de aprenderlo de las features de
    comportamiento (que aportan una senal real pero secundaria).
    """
    base_segmento = 1.4 if en_riesgo else -3.6
    logit = (
        base_segmento
        + 0.15 * comportamiento["days_since_last_login"]
        + 0.60 * comportamiento["complaints"]
        + 0.70 * comportamiento["failed_payments"]
        - 0.03 * min(subscription_months, 48)
        - 0.10 * comportamiento["sessions_last_30d"]
        + rng.normal(0, 0.2)
    )
    return 1 / (1 + np.exp(-logit))


def simular_panel(clientes, meses_maximos, rng):
    """Simula el panel mensual completo: cada cliente aporta una fila por mes."""
    columnas_estaticas = ["customer_id", "age", "country", "city", "plan", "monthly_price", "payment_method"]
    filas = []

    for _, cliente in clientes.iterrows():
        for mes in range(1, meses_maximos + 1):
            subscription_months = int(cliente["initial_tenure"] + (mes - 1))
            comportamiento = simular_comportamiento_mes(cliente, rng)
            probabilidad_churn = calcular_probabilidad_churn(
                comportamiento, subscription_months, cliente["en_riesgo"], rng
            )
            churn = int(rng.random() < probabilidad_churn)

            fila = {columna: cliente[columna] for columna in columnas_estaticas}
            fila["mes"] = mes
            fila["subscription_months"] = subscription_months
            fila.update(comportamiento)
            fila["churn"] = churn
            filas.append(fila)

    return pd.DataFrame(filas)


def main():
    rng = np.random.default_rng(SEMILLA)
    clientes = generar_clientes(NUMERO_CLIENTES, rng)
    panel = simular_panel(clientes, MESES_MAXIMOS, rng)
    panel.to_csv(RUTA_SALIDA, index=False)

    print(f"Filas generadas: {len(panel)}")
    print(f"Clientes unicos: {panel['customer_id'].nunique()}")
    print(f"Tasa de churn global: {panel['churn'].mean():.3f}")
    print(panel["mes"].value_counts().sort_index())


if __name__ == "__main__":
    main()
