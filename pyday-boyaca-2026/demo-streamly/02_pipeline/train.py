"""Entrena y compara los modelos candidatos de churn sobre el dataset de Streamly."""

from sklearn.model_selection import train_test_split

from src.data.loader import cargar_datos, preparar_matriz
from src.evaluation.metrics import comparar_modelos, evaluar_modelo
from src.features.engineering import agregar_features
from src.models.training import CONSTRUCTORES_MODELOS, entrenar_modelo

RUTA_DATASET = "../data/streamly_churn.csv"


def main():
    """Ejecuta el pipeline completo: datos, features, entrenamiento y comparacion."""
    datos = cargar_datos(RUTA_DATASET)
    datos = agregar_features(datos)
    predictoras, objetivo = preparar_matriz(datos)

    predictoras_train, predictoras_test, objetivo_train, objetivo_test = train_test_split(
        predictoras, objetivo, test_size=0.2, random_state=42
    )

    resultados_por_modelo = {}
    for nombre_modelo in CONSTRUCTORES_MODELOS:
        modelo = entrenar_modelo(nombre_modelo, predictoras_train, objetivo_train)
        resultados_por_modelo[nombre_modelo] = evaluar_modelo(modelo, predictoras_test, objetivo_test)

    comparar_modelos(resultados_por_modelo)


if __name__ == "__main__":
    main()
