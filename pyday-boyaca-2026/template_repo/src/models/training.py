"""Registro de modelos candidatos para predecir churn en Streamly."""

from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

MODELOS = {
    "logistic_regression": LogisticRegression,
    "random_forest": RandomForestClassifier,
    "xgboost": XGBClassifier,
    "lightgbm": LGBMClassifier,
}


def entrenar_modelo(nombre, X_train, y_train):
    """Entrena una instancia nueva del modelo indicado por nombre."""
    modelo = MODELOS[nombre]()
    modelo.fit(X_train, y_train)
    return modelo
