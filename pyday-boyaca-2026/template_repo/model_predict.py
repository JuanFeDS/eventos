"""Genera predicciones de churn para un archivo de clientes de Streamly."""

import sys

import joblib
import pandas as pd

from src.features.engineering import add_features


def main(
        input_path,
        model_path="experiments/run_2026-08-05_e91b/model.pkl"
    ):
    """
    Carga el modelo entrenado y devuelve la probabilidad de cancelación por cliente.
    """
    modelo = joblib.load(model_path)
    df = pd.read_csv(input_path)
    df = add_features(df)
    return modelo.predict_proba(df)[:, 1]


if __name__ == "__main__":
    main(sys.argv[1])
