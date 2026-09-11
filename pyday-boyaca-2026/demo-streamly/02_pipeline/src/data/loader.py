"""Carga y prepara el dataset de churn de Streamly para entrenamiento."""

import pandas as pd

COLUMNAS_OBLIGATORIAS = ["monthly_price", "days_since_last_login"]
COLUMNAS_CATEGORICAS = ["country", "city", "plan", "payment_method"]
COLUMNAS_IDENTIFICADORAS = ["customer_id"]


def cargar_datos(ruta_csv):
    """Lee el CSV de Streamly y descarta filas sin datos obligatorios."""
    datos = pd.read_csv(ruta_csv)
    return datos.dropna(subset=COLUMNAS_OBLIGATORIAS)


def preparar_matriz(datos, columna_objetivo="churn"):
    """Separa features (codificando categoricas) y target, lista para entrenar."""
    objetivo = datos[columna_objetivo]
    predictoras = datos.drop(columns=[columna_objetivo, *COLUMNAS_IDENTIFICADORAS])
    predictoras = pd.get_dummies(predictoras, columns=COLUMNAS_CATEGORICAS)
    return predictoras, objetivo
