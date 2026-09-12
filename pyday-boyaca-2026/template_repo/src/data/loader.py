"""Carga y limpieza del dataset de churn de Streamly."""

import pandas as pd

RAW_PATH = "data/raw/streamly_churn.csv"


def load_data(path=RAW_PATH):
    """Lee el CSV crudo y aplica la limpieza básica."""
    df = pd.read_csv(path)
    return clean_data(df)


def clean_data(df):
    """Elimina filas sin precio mensual o sin fecha de último login."""
    df = df.dropna(subset=["monthly_price", "days_since_last_login"])
    return df
