🚀 Caso de estudio: ¿Qué clientes abandonarán la plataforma?

Imagina una empresa ficticia de streaming:

Streamly quiere anticiparse a los usuarios que probablemente cancelarán su suscripción durante el próximo mes.

Tenemos información como:

edad
país
tipo de plan
antigüedad
número de sesiones
horas de uso
número de dispositivos
días desde último acceso
número de contenidos vistos
porcentaje de contenidos terminados
cantidad de reclamos
método de pago
precio del plan
uso de promociones
etc.

Y nuestro target:

churn = 1 → canceló
churn = 0 → permaneció

Lo interesante es que el problema parece trivial al principio.

Entonces puedes comenzar la charla con algo como:

"Nos dieron un CSV con 100.000 usuarios y nos pidieron construir un modelo que prediga quién va a cancelar."

Iteración 1 — El notebook

Inicialmente:

churn_prediction.ipynb

Y dentro:

import pandas as pd

df = pd.read_csv("data.csv")

# cleaning
...

# feature engineering
...

# train/test split
...

# model
...

# evaluation
...

Pruebas Logistic Regression.

Luego Random Forest.

Luego XGBoost.

Luego cambias una feature.

Luego otra.

Luego vuelves a correr todo.

Y de repente tienes:

churn_prediction.ipynb

    Cell 1
    Cell 2
    Cell 3
    ...
    Cell 47
    Cell 48
    Cell 49

😂

Ahí comienza realmente tu charla.

Pero podemos hacer el caso mucho más interesante

Yo diseñaría el dataset desde el principio pensando en la evolución de la charla.

Por ejemplo, generaríamos unos 50.000–100.000 clientes sintéticos, pero con relaciones razonablemente realistas.

Podríamos tener:

Datos demográficos
customer_id
age
country
city
Información de suscripción
plan
monthly_price
subscription_months
payment_method
has_discount
Comportamiento
sessions_last_30d
hours_watched
unique_content_last_30d
completion_rate
days_since_last_login
devices_used
Interacciones
support_tickets
complaints
failed_payments
Target
churn

Y podemos introducir relaciones artificiales pero plausibles:

Más tiempo sin entrar → mayor churn.
Más reclamos → mayor churn.
Mayor antigüedad → menor churn.
Usuarios con descuento → comportamiento diferente.
Fallos de pago → mayor churn.
Usuarios muy activos → menor churn.

Así el modelo tiene algo que aprender.

Y aquí aparece lo bonito para tu charla

Puedes hacer que cada etapa de la arquitectura nazca de un problema real.

🟢 Etapa 1 — Notebook

Todo funciona.

data → preprocessing → model → evaluation

Perfecto.

🟡 Etapa 2 — "Probemos otro modelo"

Ahora queremos comparar:

Logistic Regression
Random Forest
XGBoost
LightGBM

Y empiezas a copiar código.

# Model 1
...

# Model 2
...

# Model 3
...

Entonces aparece la primera pregunta:

¿Dónde ponemos el código que todos estos modelos comparten?

🟠 Etapa 3 — Feature engineering

Descubrimos que podemos crear:

engagement_score
payment_risk
customer_activity
support_intensity

Pero ahora tenemos:

notebook_final.ipynb
notebook_final_v2.ipynb
notebook_final_v3.ipynb
notebook_final_really_final.ipynb

💀

Aquí introduces módulos:

src/
├── data/
├── features/
├── models/
├── evaluation/
└── utils/
🔵 Etapa 4 — Experimentación

Ahora queremos saber:

¿Qué combinación de features + modelo + hiperparámetros funciona mejor?

Y aparece naturalmente algo como:

model: xgboost

features:
  - engagement_score
  - payment_risk
  - support_intensity

hyperparameters:
  max_depth: 6
  learning_rate: 0.05
  n_estimators: 300

Ya no estamos simplemente "entrenando un modelo".

Estamos gestionando experimentos.

🟣 Etapa 5 — Reproducibilidad

Alguien pregunta:

"¿Cómo obtuviste ese 0.91 de ROC-AUC?"

Y empieza el terror.

😂

Porque ya no sabes:

qué dataset utilizaste
qué features estaban activas
qué modelo
qué hiperparámetros
qué random seed
qué preprocessing

Entonces introduces configuración y tracking.

🔴 Etapa 6 — El proyecto

Finalmente tenemos algo parecido a:

churn-prediction/
│
├── data/
├── notebooks/
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── evaluation/
│
├── configs/
├── experiments/
├── tests/
│
├── train.py
├── predict.py
├── requirements.txt
└── README.md

Y ese es el verdadero protagonista de la charla.

No XGBoost.

No MLflow.

No Prefect.

No Docker.

Sino las decisiones que nos llevaron a necesitar esas cosas.