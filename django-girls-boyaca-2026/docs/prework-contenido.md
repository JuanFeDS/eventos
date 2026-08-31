# Prework Django Girls Boyacá 2026 — Estructura de contenido

Borrador para revisión antes de pasar a slides. Objetivo del prework: que las asistentes lleguen al taller con todo instalado y funcionando, sin fricción ni miedo.

**Scope actual: solo Windows.** Se deja pendiente cubrir Mac/Linux más adelante si hace falta.

---

## 1. Bienvenida y expectativas
- Qué es Django Girls y qué van a construir ese día (un blog propio, funcionando en internet)
- Qué NO es el objetivo: no van a "aprender a programar" en un día, ni dominar Django — el objetivo es perderle el miedo al código y pasarla bien
- Mensaje explícito: "si algo no instala a la primera, es normal, para eso está este prework y el canal de ayuda"

## 2. Qué traer el día del taller
- Laptop propia cargada + cargador
- Espacio libre en disco (aprox. cuánto, a definir según instaladores)
- Este documento/slides como referencia si algo falla

## 3. Línea de comandos — lo mínimo
- Qué es una terminal y para qué la vamos a usar (no es "hackear", es solo dar instrucciones)
- Abrir la terminal (Windows: PowerShell)
- Navegar carpetas: `cd`, listar contenido, crear una carpeta
- **Personalizar la terminal**: instalar Windows Terminal + elegir un esquema de color (2 min, sube el ánimo antes de instalar cosas más pesadas). Oh My Posh queda como bonus opcional, fuera del checklist obligatorio — evita sumar piezas frágiles (Nerd Font + perfil de PowerShell) a un prework autoguiado

## 4. Instalación de Python
- Descarga para Windows
- Pasos de instalación con capturas
- Cómo verificar que quedó instalado (`python --version` en terminal)
- Habilitar ejecución de scripts de PowerShell (`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`) — lo va a pedir el entorno virtual de Python más adelante en el taller; mejor resolverlo ahora que a mitad de sesión

## 5. Editor de código
- Instalación de VS Code (o el que se defina)
- Verificación básica: abrirlo, crear un archivo de prueba

## 6. Cuenta de GitHub
- Crear cuenta en github.com (usuario, email, contraseña)
- Sin uso todavía — solo tener la cuenta lista

## 7. Instalación de Git
- Descarga e instalación para Windows
- Configuración mínima: `git config user.name` y `git config user.email`
- Verificación: `git --version`
- **Conectar Git con GitHub vía GitHub CLI** (`gh auth login` + `gh auth setup-git`) — decisión de scope de Juan (no es parte del tutorial oficial, que despliega por PythonAnywhere). Se eligió GitHub CLI sobre claves SSH manuales por ser mucho menos propenso a errores para principiantes (login por navegador, sin generar/copiar/pegar claves)
- Aclaración explícita: todavía no se hace ningún `git commit` — eso es del taller. Lo que se resuelve en el prework es la conexión de cuentas, no el uso de Git en sí

## 8. Checklist final de verificación
- Lista tipo "si todo esto funciona, estás lista para el taller":
  - [ ] Terminal abre sin error
  - [ ] `python --version` responde
  - [ ] PowerShell puede ejecutar scripts (`Set-ExecutionPolicy` configurado)
  - [ ] Editor de código abre
  - [ ] Cuenta de GitHub creada
  - [ ] `git --version` responde
  - [ ] `gh auth status` muestra el usuario de GitHub conectado

## 9. Canal de ayuda
- A dónde escribir si algo no instaló (grupo/chat de contacto, a definir)
- Mensaje de cierre: "escríbenos antes del taller, no el mismo día a última hora"

---

## Pendientes para cerrar antes de pasar a slides
- [ ] Definir canal de ayuda concreto (WhatsApp/Telegram/otro)
- [ ] Confirmar si el prework es sesión en vivo o autoguiado (afecta tono y nivel de detalle)
- [ ] Confirmar si el evento es virtual o presencial
- [ ] Espacio en disco estimado a mencionar en sección 2
