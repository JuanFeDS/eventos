"""Evaluacion y comparacion de modelos de churn de Streamly."""

from sklearn.metrics import confusion_matrix, roc_auc_score


def evaluar_modelo(modelo, predictoras_prueba, objetivo_prueba):
    """Calcula AUC-ROC y matriz de confusion del modelo sobre el set de prueba."""
    probabilidades = modelo.predict_proba(predictoras_prueba)[:, 1]
    predicciones = modelo.predict(predictoras_prueba)
    return {
        "auc_roc": roc_auc_score(objetivo_prueba, probabilidades),
        "matriz_confusion": confusion_matrix(objetivo_prueba, predicciones),
    }


def comparar_modelos(resultados_por_modelo):
    """Imprime los modelos evaluados ordenados de mejor a peor AUC-ROC."""
    ranking = sorted(resultados_por_modelo.items(), key=lambda item: item[1]["auc_roc"], reverse=True)
    for nombre_modelo, resultado in ranking:
        print(f"{nombre_modelo:20s} auc_roc={resultado['auc_roc']:.4f}")
