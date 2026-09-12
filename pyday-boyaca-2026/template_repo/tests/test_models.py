"""Pruebas del entrenamiento de modelos."""

from src.models.training import entrenar_modelo


def test_entrenar_modelo_returns_fitted_estimator(X_train, y_train):
    """El modelo entrenado debe quedar listo para predecir."""
    modelo = entrenar_modelo("logistic_regression", X_train, y_train)
    assert hasattr(modelo, "predict")
