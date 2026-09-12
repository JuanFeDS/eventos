"""Entrena y compara los modelos candidatos de churn sobre el dataset de Streamly."""

from sklearn.model_selection import train_test_split

from src.data.loader import load_data
from src.evaluation.metrics import evaluar_modelo
from src.features.engineering import add_features
from src.models.training import MODELOS, entrenar_modelo
from src.utils.seeds import RANDOM_STATE

TARGET = "churn"


def main():
    """Ejecuta el pipeline completo: datos, features, entrenamiento y comparación."""
    df = load_data()
    df = add_features(df)

    X = df.drop(columns=[TARGET, "customer_id"])
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE
    )

    for nombre in MODELOS:
        modelo = entrenar_modelo(nombre, X_train, y_train)
        resultado = evaluar_modelo(modelo, X_test, y_test)
        print(f"{nombre}: roc_auc={resultado['roc_auc']:.3f}")


if __name__ == "__main__":
    main()
