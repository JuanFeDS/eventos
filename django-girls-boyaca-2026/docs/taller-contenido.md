# Contenido del taller — Django Girls Boyacá 2026

**Fecha**: viernes 2026-09-11, presencial, ~9:00am-5:00pm
**Prework**: martes 2026-09-08, 7:30pm, virtual (sesión en vivo)

Corte de capítulos del [tutorial oficial](https://tutorial.djangogirls.org/es/) sobre el tiempo real disponible (~6-6.5h de enseñanza tras almuerzo y descansos). El prework ya cubrió instalación (Python, editor, terminal, Git, cuenta GitHub) — el taller arranca en fundamentos y Python.

## Decisión de scope: deploy temprano

El deploy a PythonAnywhere (cap. 13) se mantiene en el orden oficial del tutorial (justo después del primer proyecto, antes de modelos) en vez de dejarlo como stretch goal. Motivo: alto valor motivacional de ver el sitio "vivo" en internet temprano en el día, pese a ser —junto con instalación— el mayor riesgo de consumir tiempo por problemas técnicos. Como instalación ya se resolvió en el prework, se asume ese tiempo liberado para absorber el riesgo del deploy.

Capítulos que quedan fuera del corte obligatorio (stretch goal si el grupo va adelantado, o para practicar después del taller): ORM/QuerySets (17), extender plantillas (21), amplía tu aplicación (22), formularios (23).

## Cronograma

| Hora | Bloque | Duración |
|------|--------|----------|
| 9:00 | Bienvenida + verificación de checklist del prework | 30 min |
| 9:30 | Cómo funciona Internet (cap. 3) | 20 min |
| 9:50 | Introducción a Python (cap. 7) | 50 min |
| 10:40 | Break | 15 min |
| 10:55 | ¿Qué es Django? + instalación de Django (cap. 8-9) | 30 min |
| 11:25 | Primer proyecto Django (cap. 10) | 45 min |
| 12:10 | Deploy a PythonAnywhere (cap. 13) | 45 min |
| 12:55 | Almuerzo | 60 min |
| 13:55 | Modelos + Administrador de Django (cap. 11-12) | 45 min |
| 14:40 | URLs + Vistas (cap. 14-15) | 45 min |
| 15:25 | Break | 15 min |
| 15:40 | Introducción a HTML + plantillas + datos dinámicos (cap. 16, 18, 19) | 50 min |
| 16:30 | CSS — que quede bonito (cap. 20) | 30 min |
| 17:00 | Cierre: ¿y ahora qué? (cap. 24) | — |

## Ensayo del taller

Antes de construir las slides, se ejecutó a mano el bloque "¿Qué es Django? + instalación de Django + primer proyecto" (cap. 8-9-10), siguiendo el tutorial oficial paso a paso, para detectar fricciones reales antes del día del evento.

**Decisiones validadas en el ensayo:**
- **venv + pip**, no Poetry — se consideró Poetry (más legible para principiantes por `pyproject.toml`), pero se descartó porque el script de autoconfiguración de PythonAnywhere (deploy, cap. 13) espera un `requirements.txt`, y usar Poetry habría sumado un paso extra (`poetry export`) justo en el momento de mayor riesgo del día
- **Versión de Django fijada** vía `requirements.txt` con `Django~=5.2.12` (la que recomienda el tutorial oficial) en vez de `pip install django` a secas, que instala la última versión (6.1.1 al momento del ensayo) y podría no coincidir con lo que describe el tutorial
- Entorno virtual con el nombre oficial del tutorial, `myvenv`, y activación en PowerShell con `. myvenv\Scripts\activate.ps1`
- Nombre de proyecto: `mysite` (el que usa el tutorial oficial), no un nombre personalizado — evita confusión si alguien lee el tutorial en paralelo

**Gotcha real encontrado y reproducido:** correr `django-admin.exe startproject mysite .` dos veces en la misma carpeta produce `CommandError: manage.py already exists. Overlaying a project into an existing directory won't replace conflicting files.` — queda documentado como callout de troubleshooting en las slides del taller.

La implementación de referencia del ensayo (`manage.py`, `mysite/`, `requirements.txt`) queda commiteada en la raíz de `django-girls-boyaca-2026/` como material de apoyo para Juan el día del taller (análogo a `demo-streamly/` en Pyday). `venv/` y `db.sqlite3` quedan en `.gitignore`.

## Slides del taller

- [`taller/slides/taller.html`](../taller/slides/taller.html) — mismo motor que el prework (misma plantilla, navegación táctil/teclado, responsive mobile/iPhone). Cubre por ahora los temas 1-3 (¿Qué es Django?, Instalación, Primer proyecto), correspondientes al bloque 10:55-12:10 del cronograma. Los siguientes bloques (deploy, modelos, URLs/vistas, HTML/CSS, cierre) se agregan en sesiones futuras de ensayo, siguiendo el mismo orden cronológico.

## Pendientes para cerrar antes del taller

- [ ] Confirmar número exacto de asistentes en el grupo físico de Juan
- [ ] Confirmar sistemas operativos que van a traer las asistentes (Windows/Mac/Linux) — el prework actual solo cubre Windows
- [ ] Preparar bloque de deploy con troubleshooting anticipado (errores comunes de PythonAnywhere) dado el riesgo de tiempo identificado
- [ ] Continuar el ensayo cronológico y las slides para los bloques restantes del cronograma (cap. 3, 7, 13, 11-12, 14-15, 16+18+19, 20, 24)
