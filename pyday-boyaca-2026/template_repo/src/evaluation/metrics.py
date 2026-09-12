"""Métricas de evaluación y comparación entre modelos."""

from sklearn.metrics import confusion_matrix, roc_auc_score


def evaluar_modelo(modelo, X_test, y_test):
    """Calcula ROC-AUC y matriz de confusión para un modelo ya entrenado."""
    proba = modelo.predict_proba(X_test)[:, 1]
    return {
        "roc_auc": roc_auc_score(y_test, proba),
        "confusion_matrix": confusion_matrix(y_test, modelo.predict(X_test)).tolist(),
    }


def comparar_modelos(resultados_por_modelo):
    """Imprime el ROC-AUC de cada modelo, de mejor a peor."""
    for nombre, resultado in sorted(
        resultados_por_modelo.items(), key=lambda item: item[1]["roc_auc"], reverse=True
    ):
        print(f"{nombre}: roc_auc={resultado['roc_auc']:.3f}")
