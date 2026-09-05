# Guion — Pyday Boyacá 2026: "Más allá del notebook"

## Caso de estudio: Streamly

Empresa ficticia de streaming. Dataset sintético tipo **panel mensual**: una fila = un (customer_id, mes), no un cliente único. 90.000 filas (15.000 clientes × 6 meses). Generador en `demo-streamly/data/generate_dataset.py`.

Columnas:
- Demográficas (casi constantes por cliente): `age`, `country`, `city`
- Suscripción (casi constantes): `plan`, `monthly_price`, `payment_method`
- Antigüedad: `subscription_months`
- Comportamiento (variable mes a mes): `sessions_last_30d`, `hours_watched`, `unique_content_last_30d`, `completion_rate`, `days_since_last_login`, `devices_used`
- Interacciones (variable): `support_tickets`, `complaints`, `failed_payments`
- Target: `churn`

**El eje de la charla es la evolución notebook → pipeline modular (etapas 1-6 de abajo), no el leakage.** El leakage aparece una sola vez, como una nota al margen en la Etapa 1 — es un gancho para los curiosos, no un tema a desarrollar.

---

## Gancho de apertura

*[Diapo: título + logo Streamly ficticio]*

> Streamly, una plataforma de streaming ficticia, les da un CSV con cien mil filas y una tarea: "necesitamos saber quién va a cancelar el próximo mes." Ustedes abren un notebook, lo llaman `churn_prediction.ipynb`, y empiezan.
>
> Cargan los datos. Limpian un par de columnas. Entrenan una regresión logística. Funciona. Perfecto. Cierran la laptop satisfechos.
>
> Una semana después alguien del equipo pregunta: "oye, ¿probamos con Random Forest?" Y ahí — sin que se den cuenta — empieza la historia real de esta charla. No la de un modelo. La de un proyecto que tiene que crecer.

---

## Etapa 1 — El notebook

*[Diapo: `data → preprocessing → model → evaluation`]*

> `churn_prediction.ipynb` tiene una estructura perfectamente razonable:
>
> ```python
> import pandas as pd
> from sklearn.model_selection import train_test_split
> from sklearn.linear_model import LogisticRegression
> from sklearn.metrics import roc_auc_score
>
> df = pd.read_csv("streamly_churn.csv")
>
> # cleaning
> df = df.dropna(subset=["monthly_price", "days_since_last_login"])
>
> # feature engineering
> df["engagement_score"] = df["sessions_last_30d"] * df["completion_rate"]
>
> X = df.drop(columns=["churn", "customer_id"])
> y = df["churn"]
> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
>
> modelo = LogisticRegression(max_iter=1000)
> modelo.fit(X_train, y_train)
>
> print(roc_auc_score(y_test, modelo.predict_proba(X_test)[:, 1]))
> ```
>
> Todo funciona. El notebook tiene 15 celdas, cada una hace una cosa, se lee de arriba a abajo. Esto no tiene nada de malo — es exactamente como debería empezar cualquier proyecto de ML.

**Nota al margen (breve, un solo comentario, seguimos):**

> Un detalle para los que ya vieron `GroupKFold` o `train_test_split` con paneles temporales: como cada cliente de Streamly aparece varias veces (una fila por mes), ese `random_state=42` puede dejar el mes 3 de un cliente en train y su mes 4 en test — información del mismo cliente filtrándose entre los dos lados. Es un problema real y da para una charla completa. Hoy no es el que nos ocupa: el problema que sí vamos a perseguir es organizativo, no estadístico. Sigamos.

---

## Etapa 2 — "Probemos otro modelo"

*[Diapo: cuatro bloques de código casi idénticos]*

> El equipo quiere comparar modelos: Logistic Regression, Random Forest, XGBoost, LightGBM. La forma más rápida de hacerlo es copiar la celda de arriba y cambiar una línea:
>
> ```python
> # Modelo 1: Logistic Regression
> modelo_1 = LogisticRegression(max_iter=1000)
> modelo_1.fit(X_train, y_train)
> auc_1 = roc_auc_score(y_test, modelo_1.predict_proba(X_test)[:, 1])
>
> # Modelo 2: Random Forest
> modelo_2 = RandomForestClassifier(n_estimators=300)
> modelo_2.fit(X_train, y_train)
> auc_2 = roc_auc_score(y_test, modelo_2.predict_proba(X_test)[:, 1])
>
> # Modelo 3: XGBoost
> modelo_3 = XGBClassifier()
> modelo_3.fit(X_train, y_train)
> auc_3 = roc_auc_score(y_test, modelo_3.predict_proba(X_test)[:, 1])
> ```
>
> Funciona. Pero ya se repitió tres veces la misma carga de datos, el mismo split, la misma métrica. Y aparece la primera pregunta incómoda de la charla:
>
> **¿Dónde ponemos el código que todos estos modelos comparten?**

---

## Etapa 3 — Feature engineering

*[Diapo: listado de features derivadas + árbol de `src/`]*

> Alguien se da cuenta de que combinando columnas se puede describir mejor a un cliente de Streamly:
>
> - `engagement_score` = `sessions_last_30d` × `completion_rate`
> - `payment_risk` = función de `failed_payments` y `payment_method`
> - `customer_activity` = combinación de `devices_used` y `unique_content_last_30d`
> - `support_intensity` = `support_tickets` + `complaints`
>
> El problema: cada vez que se agrega una feature nueva, hay que volver a correr las 15 celdas originales para los 4 modelos. La carpeta empieza a verse así:
>
> ```
> churn_prediction.ipynb
> churn_prediction_final.ipynb
> churn_prediction_final_v2.ipynb
> churn_prediction_final_v3_de_verdad.ipynb
> ```
>
> 💀 Nadie recuerda cuál de los cuatro tiene el `engagement_score` corregido.
>
> Aquí es donde nace la primera decisión de arquitectura real: sacar el código del notebook.
>
> ```
> src/
> ├── data/          # cargar y limpiar streamly_churn.csv
> ├── features/      # engagement_score, payment_risk, customer_activity, support_intensity
> ├── models/        # una función de entrenamiento por modelo
> ├── evaluation/     # roc_auc, matriz de confusión, comparación entre modelos
> └── utils/
> ```
>
> El notebook deja de ser el lugar donde vive el código. Pasa a ser el lugar donde se *usa* el código.

---

## Etapa 4 — Experimentación

*[Diapo: archivo `configs/experimento_01.yaml`]*

> La pregunta ahora es otra: ¿qué combinación de features + modelo + hiperparámetros funciona mejor para predecir churn en Streamly? Empiezan a aparecer variantes:
>
> - Con `engagement_score` y sin él
> - XGBoost con `max_depth=4` vs `max_depth=8`
> - Con o sin `payment_risk`
>
> En vez de escribir un notebook nuevo por cada combinación, aparece algo así:
>
> ```yaml
> model: xgboost
> features:
>   - engagement_score
>   - payment_risk
>   - support_intensity
> hyperparameters:
>   max_depth: 6
>   learning_rate: 0.05
>   n_estimators: 300
> ```
>
> Ya no estamos entrenando un modelo. Estamos **gestionando experimentos** — y un archivo de configuración describe cada uno sin tocar el código.

---

## Etapa 5 — Reproducibilidad

*[Diapo: cara de pánico / "¿cómo obtuviste ese 0.91?"]*

> Alguien del equipo pregunta en el standup: "oye, ¿cómo obtuviste ese 0.91 de ROC-AUC en Streamly?"
>
> Y ahí empieza el terror, porque ya no se sabe con certeza:
>
> - qué versión de `streamly_churn.csv` se usó
> - qué features estaban activas ese día
> - qué modelo y qué hiperparámetros
> - qué `random_state`
> - qué preprocesamiento tenía el notebook en ese momento
>
> La solución no es "acordarse mejor" — es dejar de depender de la memoria. El `.yaml` de la etapa anterior empieza a guardarse junto con su resultado, con su seed y con un identificador único por corrida. Cada experimento queda registrado, no solo ejecutado.

---

## Etapa 6 — El proyecto

*[Diapo: árbol completo de carpetas]*

> Después de seis etapas de fricción real, lo que queda ya no es un notebook. Es esto:
>
> ```
> streamly-churn/
> ├── data/
> ├── notebooks/          # exploración, ya no producción
> ├── src/
> │   ├── data/
> │   ├── features/
> │   ├── models/
> │   └── evaluation/
> ├── configs/
> ├── experiments/        # resultados + configuración de cada corrida
> ├── tests/
> ├── train.py
> ├── predict.py
> ├── requirements.txt
> └── README.md
> ```
>
> Y este es el verdadero protagonista de la charla. No XGBoost. No MLflow. No Docker. **Las decisiones que nos llevaron a necesitar esas cosas** — y ninguna de esas decisiones se tomó de un tirón: cada carpeta de este árbol nació de una fricción concreta que ya vivimos juntos hoy.

---

## Cierre — mensaje que conecte con la audiencia

> Si tienen en su computador una carpeta con `_final_v2_de_verdad.ipynb`, no es porque hicieron algo mal. Es la señal de que su proyecto ya superó lo que un solo notebook puede sostener — exactamente lo que le pasó a Streamly en esta charla.
>
> No existe un punto en el que un proyecto "se gana el derecho" a tener una carpeta `src/`. Se gana ese derecho la primera vez que alguien pregunta "¿dónde va el código compartido?" y no hay una buena respuesta.
>
> Así que la próxima vez que sientan que su notebook dejó de alcanzar, no lo lean como una falla personal. Léanlo como la primera señal de que el proyecto está listo para evolucionar — y ya vieron hoy, paso a paso, hacia dónde.
