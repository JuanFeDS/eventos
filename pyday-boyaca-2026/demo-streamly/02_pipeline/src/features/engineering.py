"""Features derivadas del comportamiento y riesgo de los clientes de Streamly."""

RIESGO_POR_METODO_PAGO = {
    "tarjeta_credito": 0.0,
    "tarjeta_debito": 0.1,
    "pse": 0.2,
    "paypal": 0.15,
}


def agregar_engagement_score(datos):
    """Combina sesiones y finalizacion de contenido en un solo indicador de uso."""
    datos["engagement_score"] = datos["sessions_last_30d"] * datos["completion_rate"]
    return datos


def agregar_payment_risk(datos):
    """Combina pagos fallidos con el riesgo historico del metodo de pago."""
    riesgo_metodo = datos["payment_method"].map(RIESGO_POR_METODO_PAGO)
    datos["payment_risk"] = datos["failed_payments"] + riesgo_metodo
    return datos


def agregar_customer_activity(datos):
    """Combina dispositivos y variedad de contenido consumido."""
    datos["customer_activity"] = datos["devices_used"] * datos["unique_content_last_30d"]
    return datos


def agregar_support_intensity(datos):
    """Suma tickets de soporte y reclamos en un solo indicador de friccion."""
    datos["support_intensity"] = datos["support_tickets"] + datos["complaints"]
    return datos


def agregar_features(datos):
    """Aplica todas las features derivadas sobre el dataset de Streamly."""
    datos = agregar_engagement_score(datos)
    datos = agregar_payment_risk(datos)
    datos = agregar_customer_activity(datos)
    datos = agregar_support_intensity(datos)
    return datos
