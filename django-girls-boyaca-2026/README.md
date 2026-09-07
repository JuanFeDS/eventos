# Django Girls Boyacá 2026

**Fecha**: 2026-09-11 (taller, presencial) · 2026-09-08 (prework, virtual)
**Formato**: Taller
**Estado**: Prework completo · slides del taller en construcción (temas 1-3 de 9)

## Estructura

- `docs/` — investigación y contenido base
  - [`preparacion.md`](docs/preparacion.md) — resumen del manual de coaching y del tutorial oficial de Django Girls
  - [`prework-contenido.md`](docs/prework-contenido.md) — estructura de contenido del prework (aprobada)
  - [`taller-contenido.md`](docs/taller-contenido.md) — cronograma, corte de capítulos y bitácora del ensayo del taller
- `prework/` — material del prework
  - `slides/` — slides del prework
    - `template.html` — plantilla/guía de diseño con los 6 moldes reutilizables (referencia)
    - `prework.html` — deck completo, 36 slides, los 10 temas + terminal personalizada + conexión Git-GitHub + cuenta y token de PythonAnywhere + video de Code.org
  - `assets/` — capturas de pantalla, embebidas en `prework.html` (base64)
    - `terminal-powershell.png` · `terminal-personalizada.png` · `python-descarga.png` · `vscode-instalado.png` · `github-registro.png` · `git-instalador.png` · `gh-auth-login.png`
- `taller/` — material del taller (en construcción)
  - `slides/taller.html` — deck del taller, mismo motor que el prework. Cubre por ahora ¿Qué es Django?, instalación y primer proyecto (temas 1-3)
- `manage.py`, `mysite/`, `requirements.txt` — implementación de referencia del ensayo del taller (venv + pip, Django~=5.2.12), para que Juan la use como apoyo el día del evento. `venv/` y `db.sqlite3` quedan fuera de git
