# Eventos

Directorio personal de presentaciones, talleres y material de soporte para charlas y talleres como speaker.

---

## Tabla de Contenido

1. [Eventos](#1-eventos)
2. [Estructura del repositorio](#2-estructura-del-repositorio)
3. [Estado por evento](#3-estado-por-evento)
4. [Contacto](#4-contacto)

---

## 1. Eventos

| Evento | Rol | Fecha | Estado |
|--------|-----|-------|--------|
| 🐍 [Django Girls Boyacá 2026](django-girls-boyaca-2026/) | Taller | 2026-09-11 | 🟡 Prework y contenido del taller listos · faltan slides del taller |
| 📊 [Pyday Boyacá 2026](pyday-boyaca-2026/) | Charla | 2026-09-12 | 🟡 16 slides listas (fondo plano) · falta demo real de código |

---

## 2. Estructura del repositorio

Cada evento vive en su propia carpeta, con su propio README como fuente de verdad de fecha, formato y estado.

```
eventos/
├── django-girls-boyaca-2026/
│   ├── docs/              # investigación: manual de coaching, tutorial oficial, contenido del prework
│   ├── prework/
│   │   ├── slides/        # deck HTML del prework (template.html + prework.html)
│   │   └── assets/        # capturas de pantalla usadas en el deck
│   └── README.md
├── pyday-boyaca-2026/
│   ├── docs/              # guion de la charla
│   ├── slides/            # deck de la charla + assets/
│   ├── demo-streamly/     # proyecto de ejemplo: 01_notebook/ (caos) → 02_pipeline/ (modular), data/ sintética
│   └── README.md
└── README.md
```

---

## 3. Estado por evento

### 🐍 Django Girls Boyacá 2026 — Taller
- ✅ Investigación de base: manual de coaching oficial + tutorial de Django Girls resumidos en `docs/preparacion.md`
- ✅ Prework de instalación completo: 30 slides interactivas (`prework/slides/prework.html`) cubriendo línea de comandos, Python, terminal personalizada, VS Code, GitHub, Git + conexión con GitHub CLI, y checklist final con progreso guardado por navegador
- ✅ Logística confirmada: prework en vivo y virtual el martes 2026-09-08 (7:30pm), taller presencial el viernes 2026-09-11 (9am-5pm), Juan con grupo físico fijo
- ✅ Contenido del taller cerrado: cronograma completo con corte de capítulos en `docs/taller-contenido.md`, incluye deploy temprano a PythonAnywhere
- 🟡 Pendiente: slides del taller, canal de ayuda concreto (WhatsApp/Telegram), número exacto de asistentes y sistemas operativos que van a traer

### 📊 Pyday Boyacá 2026 — Charla
- 📝 Título y descripción definidos: *"Más allá del notebook: construyendo proyectos de Machine Learning que evolucionan"*
- 🎯 Caso de estudio elegido: Streamly (streaming ficticio), churn sintético en panel mensual; dataset generado en `demo-streamly/data/`
- ✅ Guion completo (gancho + 6 etapas de evolución notebook → pipeline + cierre) en `pyday-boyaca-2026/docs/guion.md`. Leakage/GroupKFold queda como mención breve, no como eje de la charla
- ✅ Plantilla de slides (`slides/template.html`, 10 moldes, fondo plano) + charla completa armada en 16 slides (`slides/charla.html`) a partir del guion
- 🔴 Pendiente: el código de demo real de `demo-streamly/01_notebook/` y `02_pipeline/`, y resolver el ícono del logo (marca de agua de Canva)

---

## 4. Contacto

JuanFe — [jmartinezbernal02@gmail.com](mailto:jmartinezbernal02@gmail.com)
