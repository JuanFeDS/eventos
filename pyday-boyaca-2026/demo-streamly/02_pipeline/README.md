# 02_pipeline — Streamly, versión modular

El mismo problema de `01_notebook/`, después de las etapas 2-3 de la charla: código compartido movido a `src/`, en vez de repetido celda tras celda.

```
02_pipeline/
├── src/
│   ├── data/          # cargar_datos, preparar_matriz
│   ├── features/      # engagement_score, payment_risk, customer_activity, support_intensity
│   ├── models/        # un constructor por modelo (logistic_regression, random_forest, xgboost, lightgbm)
│   └── evaluation/     # auc_roc, matriz de confusión, comparación entre modelos
└── train.py            # arma el pipeline completo y compara los 4 modelos
```

No incluye `configs/` ni `experiments/` — esas dos etapas (experimentación y reproducibilidad) se explican en las slides sin código real corriendo.

## Cómo correr

```
pip install -r requirements.txt
python train.py
```

Lee el dataset desde `../data/streamly_churn.csv`.
