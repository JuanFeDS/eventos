"""Registro de modelos candidatos para predecir churn en Streamly."""

from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

CONSTRUCTORES_MODELOS = {
    "logistic_regression": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "random_forest": lambda: RandomForestClassifier(n_estimators=300, random_state=42),
    "xgboost": lambda: XGBClassifier(eval_metric="logloss", random_state=42),
    "lightgbm": lambda: LGBMClassifier(random_state=42, verbose=-1),
}


def entrenar_modelo(nombre_modelo, predictoras_entrenamiento, objetivo_entrenamiento):
    """Entrena una instancia nueva del modelo indicado por nombre."""
    modelo = CONSTRUCTORES_MODELOS[nombre_modelo]()
    modelo.fit(predictoras_entrenamiento, objetivo_entrenamiento)
    return modelo
