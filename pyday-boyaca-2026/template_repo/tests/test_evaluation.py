"""Pruebas de las métricas de evaluación."""

from src.evaluation.metrics import evaluar_modelo


def test_evaluar_modelo_returns_roc_auc(modelo_entrenado, X_test, y_test):
    """El resultado debe incluir un roc_auc válido entre 0 y 1."""
    resultado = evaluar_modelo(modelo_entrenado, X_test, y_test)
    assert 0.0 <= resultado["roc_auc"] <= 1.0
