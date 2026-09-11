# Pyday Boyacá 2026

**Organiza**: Python Colombia
**Fecha**: 2026-09-12
**Formato**: Charla
**Estado**: Por preparar

## Título

Más allá del notebook: construyendo proyectos de Machine Learning que evolucionan

## Descripción

Un notebook es el punto de partida de la mayoría de proyectos de Machine Learning, pero rara vez es el mejor lugar para que evolucionen. A medida que aparecen nuevas ideas, experimentos y modelos, el código comienza a crecer, las comparaciones se vuelven difíciles y reproducir resultados deja de ser una tarea sencilla.

En esta charla recorreremos la evolución de un proyecto real de Machine Learning: desde un único notebook hasta una solución organizada, modular y preparada para iterar rápidamente. Más que centrarnos en librerías específicas, exploraremos las decisiones de diseño que permitieron experimentar mejor, reutilizar código, comparar modelos y mantener el proyecto a medida que aumentaba su complejidad.

Si alguna vez has sentido que tu notebook dejó de ser suficiente, esta charla te mostrará un camino práctico para convertir un experimento en un proyecto que realmente pueda evolucionar.

## Caso de estudio

Streamly — plataforma de streaming ficticia, dataset sintético de churn en formato panel mensual (una fila = cliente-mes, ~6 meses de historia por cliente). El eje de la charla es la evolución notebook → pipeline modular en 6 etapas (comparar modelos, feature engineering, experimentación, reproducibilidad, proyecto final); el leakage vía `customer_id` aparece solo como una mención breve, no como protagonista. Guion completo en `docs/guion.md`.

Reemplaza a Spaceship Titanic (decisión 2026-09-05) — la corrección pendiente del MDX del portafolio queda como tarea aparte, sin conexión directa con esta charla.

## Slides

- `slides/template.html` — plantilla base con los 4 moldes de marca sacados de `slides/Diapositivas base para PyDay Boyacá.pdf` (portada, título de sección, contacto, cierre) + 6 moldes de contenido (declaración, callout, código, árbol de carpetas, lista, nota al margen). Sirve como referencia/catálogo de moldes.
- `slides/charla.html` — las 16 slides reales de la charla completa, armadas a partir de `docs/guion.md` (gancho + 6 etapas + cierre) sobre esos moldes. Fondo plano (sin degradados) por preferencia de Juan; cada divisor de etapa y cada frase de cierre quedaron fusionados como eyebrow/subtítulo de la slide de contenido en vez de slides aparte.

Mismo motor de navegación del prework de Django Girls (flechas, dots, swipe táctil, teclado). Assets reales (colibríes + franja de auspiciantes) en `slides/assets/`.

Pendiente: el ícono de Python del logo original tiene marca de agua de Canva sin licenciar — el logo quedó reconstruido solo con texto hasta que se resuelva. El dato de contacto solo tiene el correo por ahora (a definir si se agregan GitHub/portafolio).

## Demo de código

`demo-streamly/` contiene la evolución real del caso de estudio, corrida contra el dataset real (`data/streamly_churn.csv`, 90.000 filas) — solo para proyectar en pantalla, no se ejecuta en vivo:

- `01_notebook/` — el "antes": cuatro notebooks que muestran el caos progresivo de las etapas 1-3 del guion (`churn_prediction.ipynb` → `churn_prediction_final.ipynb` → `churn_prediction_final_v2.ipynb` → `churn_prediction_final_v3_de_verdad.ipynb`), cada uno más desordenado que el anterior: comparación de modelos copy-pasteada, features agregadas a mitad de notebook, un experimento colgado que nadie limpió y una versión vieja de `engagement_score` comentada y olvidada.
- `02_pipeline/` — el "después": versión modular reducida (`src/data`, `src/features`, `src/models`, `src/evaluation` + `train.py`), sin `configs/` ni `experiments/` (esas dos etapas se explican en las slides sin código real corriendo). Se corre con `pip install -r requirements.txt && python train.py`.

AUC-ROC real de los 4 modelos sobre el set de prueba: XGBoost 0.772, LightGBM 0.768, Random Forest 0.764, Logistic Regression 0.762 (con `StandardScaler` para que converja limpio).
