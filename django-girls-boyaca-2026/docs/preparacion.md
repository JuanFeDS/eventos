# Preparación — Django Girls Boyacá 2026

**Fecha del taller**: 2026-09-11
**Rol de Juan**: Coach
**Fuentes**: [coach.djangogirls.org](https://coach.djangogirls.org) (manual de coaching) y [tutorial.djangogirls.org/es](https://tutorial.djangogirls.org/es/) (tutorial oficial que siguen las asistentes)

---

## 1. Qué es Django Girls y qué NO es el objetivo del taller

> "El objetivo final no es construir un website. No es enseñar todo Django. Tampoco es enseñar programación."

El objetivo real es demostrar que **"el código es divertido"**, generar entusiasmo, mostrar que programar no da miedo y es para todas. Esa chispa inicial es lo que después impulsa horas de autoaprendizaje.

Esto cambia el criterio de éxito del taller: no es "cuánto tutorial cubrimos", es "con qué actitud se van las asistentes".

---

## 2. Estructura del evento (info logística general)

- Formato típico: **evento de un día**, duración habitual **7-8 horas**. Algunos eventos se extienden a dos días o incluyen una sesión de instalación la víspera.
- Trabajo previo del coach fuera del día del taller:
  - ~1-2h conociendo al grupo (comunicación previa)
  - 3+ horas de soporte de instalación vía chat/email antes del evento
  - ~1-3h en reuniones pre/post taller con el equipo organizador
- Se recomienda que las asistentes completen el **capítulo de instalación antes del evento**, para poder "empezar a programar de inmediato" el día del taller — esto es una decisión logística a coordinar con las organizadoras de Boyacá.
- Formato de trabajo: coaches trabajan con **grupos de ~3 participantes**, no charlas frontales. El coach se mantiene "al margen, no al frente" del grupo.

**Pendiente de confirmar con las organizadoras locales** (no está en el manual genérico):
- Horario exacto del 2026-09-11
- Si habrá sesión de instalación previa (¿cuándo?)
- Cuántas asistentes / cuántos coaches habrá, y si a Juan le asignan un grupo fijo
- Sistemas operativos que van a traer las asistentes (Windows vs Mac vs Linux) — condiciona cómo preparar instalación

---

## 3. Índice completo del tutorial oficial (es.tutorial.djangogirls.org)

Es lo que las asistentes siguen paso a paso. El taller completo no necesariamente cubre todo — hay que decidir el corte según el tiempo disponible.

| # | Capítulo | Bloque temático |
|---|----------|------------------|
| — | Introducción (bienvenida, requisitos) | Preliminares |
| 1 | Instalación | Setup |
| 2 | Instalación (Chromebook) | Setup |
| 3 | Cómo funciona Internet | Fundamentos web |
| 4 | Introducción a la línea de comandos | Fundamentos |
| 5 | Instalación de Python | Setup |
| 6 | Editor de código | Setup |
| 7 | Introducción a Python | Python |
| 8 | ¿Qué es Django? | Django |
| 9 | Instalación de Django | Django |
| 10 | ¡Tu primer proyecto en Django! | Django |
| 11 | Modelos en Django | Django |
| 12 | Administrador de Django | Django |
| 13 | ¡Despliega! (deploy intermedio, en PythonAnywhere) | Deploy |
| 14 | URLs en Django | Django |
| 15 | Vistas en Django | Django |
| 16 | Introducción a HTML | Web fundamentals |
| 17 | ORM de Django (QuerySets) | Django |
| 18 | Datos dinámicos en las plantillas | Django |
| 19 | Plantillas de Django | Django |
| 20 | CSS — ¡Que quede bonito! | Web fundamentals |
| 21 | Extendiendo plantillas | Django |
| 22 | Amplía tu aplicación | Práctica libre |
| 23 | Formularios de Django | Django |
| 24 | ¿Y ahora qué? | Cierre / próximos pasos |

**Nota de scope**: el manual de coaching menciona que el contenido "core" cabe en 7-8 horas, pero en la práctica muchos talleres no llegan a los formularios (cap. 23) o a "amplía tu aplicación" (cap. 22). El deploy (cap. 13) suele ser, junto con instalación, donde más tiempo se va por problemas técnicos.

**Falta definir**: qué capítulos concretos cubrir en Boyacá según las horas reales del evento (ver pendiente logístico arriba). Es el primer bloqueante para cerrar el scope del taller.

---

## 4. Manual de coaching — filosofía y reglas prácticas

### 4.1 Palabras: qué decir y qué no decir

| ❌ No decir / hacer | ✅ Decir / hacer en su lugar |
|---|---|
| Jerga técnica sin explicar | Lenguaje accesible, como si le hablaras a alguien sin ningún contexto previo |
| "Es fácil" / "solo tenés que..." | Nada — minimiza el esfuerzo real. Puede ser lo más difícil que hayan hecho |
| Fingir sorpresa ante "¿qué es un directorio?" | Tratarlo como pregunta legítima, sin gesto de asombro |
| "Bueno, en realidad..." (correcciones innecesarias) | Dejarlo pasar si no es relevante para lo que están haciendo |
| Comentarios tipo "hasta mi abuela podría hacer esto" | Nada — son "subtle-isms" que incomodan aunque no haya mala intención |
| "¿Alguna pregunta?" | "¿Qué preguntas tenéis?" (asume que van a tener, no que quizás) |

Frases recomendadas: *"Me alegra que hayas dicho eso"*, *"Excelente pregunta"*, *"No estoy seguro… miremos en internet/preguntemos a alguien"*.

Principio base: asumir que **todas las participantes tienen cero conocimiento pero inteligencia infinita**.

### 4.2 Ritmo y comunicación

- Hablar deliberadamente despacio.
- Dar mucho más tiempo del que te sientas cómodo antes de llenar un silencio — están procesando.
- Ir al ritmo de ellas, no al tuyo. No asumir que algo es "obvio".

### 4.3 El teclado es lava

No tocar el teclado de la participante. Si de verdad hace falta:
1. Preguntar explícitamente "¿te importa si escribo?"
2. Explicar en voz alta qué estás haciendo mientras lo haces
3. Asumir por defecto que en realidad no hace falta que lo hagas tú

Alternativa siempre preferible: explicarle verbalmente qué tiene que hacer y que lo escriba ella.

### 4.4 Aprender del error, no evitarlo

- La estrategia deliberada es dejar que lleguen a un error, y guiarlas a **leer y entender el mensaje** en vez de arreglarlo tú.
- Enseñar que los errores no dan miedo — las páginas de error son "amigas".
- Esto construye la capacidad de resolver problemas por sí solas después del taller (van a tener muchas más horas solas que contigo).
- Técnicas: "¿cómo lo resolverías?", hacerlas buscar en Google en vez de dar la respuesta directa, incentivar que se desvíen del tutorial con ideas propias.

### 4.5 Síndrome del impostor

Particularmente común en mujeres en este contexto. Cómo combatirlo:
- No aceptar frases tipo "soy muy [x] para esto" — redirigir con evidencia de que sí pueden.
- Felicitar logros de forma específica y concreta, no genérica.
- Darles tiempo para mostrar su trabajo.

### 4.6 Checklist de atmósfera segura

- Sonreír, contacto visual, usar sus nombres
- Admitir cuando no sabés algo
- Validar que está bien equivocarse y está bien frustrarse
- No hay "preguntas tontas"
- Preguntar activamente si necesitan ayuda (muchas no se animan a pedirla)
- Silencios largos y en calma mientras procesan, sin llenarlos

### 4.7 Accesibilidad

- **Baja audición**: tener alternativa de comunicación por texto (chat), laptop a mano para mensajes.
- **Baja visión**: preguntar proactivamente al inicio si necesitan ayuda con tamaño de texto/zoom en terminal, editor y navegador — no asumir nada.
- **Manejo de frustración**: los descansos están en el cronograma por una razón — normalizar "está bien parar, tomar agua y volver". El movimiento físico ayuda a asentar conceptos nuevos.
- **Windows vs Mac/Linux**: si tu grupo usa un SO distinto al tuyo, no te preocupes — la instalación en Windows mejoró mucho y hay otros coaches para casos difíciles. Relevante confirmar de antemano qué SO van a traer las asistentes en Boyacá.

### 4.8 Rol de meta-coach (si aplica en Boyacá)

Coach senior sin grupo fijo, disponible para apoyar a otros coaches con problemas técnicos.
- Se presenta al inicio del evento a cada coach, pregunta si hubo problemas en la instalación previa.
- Trabaja **junto con** el coach (no le saca el problema de las manos) para que el coach también aprenda.
- La mayoría de preguntas técnicas surgen en instalación y en el capítulo de deploy.
- Criterio para decidir cómo resolver un bug: ¿la participante quiere aprender a resolverlo, o solo avanzar? A veces un workaround rápido es mejor que el fix "correcto" si consume demasiado tiempo.
- Cuidado: las asistentes usan sus propias laptops con configuraciones únicas — evitar cambios que puedan romper software existente fuera del contexto del taller.

Relevante confirmar: **si el evento de Boyacá va a tener meta-coaches o si Juan sería el único coach de su grupo.**

### 4.9 Después del taller

- Mantener contacto con el grupo — responder dudas y dar apoyo cuando sigan aprendiendo solas.
- Reportar problemas encontrados en el tutorial (idealmente como PR al repo, o como issue en GitHub si no da tiempo en el momento — mejor anotarlo durante el taller para no olvidar detalles).
- Invitar a las participantes a comunidades/eventos locales de Python para que tengan "una cara conocida" en la comunidad tech.
- Compartir aprendizajes propios del taller escribiendo a hello@djangogirls.org — retroalimenta materiales futuros.

---

## 5. Checklist de preparación para Juan

### Antes del evento
- [ ] Confirmar horario exacto, ubicación y duración del 2026-09-11 con organizadoras
- [ ] Confirmar si hay sesión de instalación previa y cuándo
- [ ] Confirmar cuántas asistentes por coach y si Juan tendrá grupo fijo
- [ ] Repasar el tutorial completo (cap. 1-24) haciéndolo él mismo de punta a punta, no solo leerlo
- [ ] Definir junto con organizadoras/otros coaches qué capítulos son el "core" a cubrir según las horas reales
- [ ] Preparar instalación en ambos SO más probables (Windows/Mac) por si toca ayudar fuera de su SO principal
- [ ] Revisar si hay traducción/localización específica pendiente en el tutorial en español (posible tema de contribución)

### El día del taller
- [ ] Presentarse, generar ambiente seguro desde el primer minuto (sonreír, nombres, "qué preguntas tenéis")
- [ ] No tocar el teclado de las participantes salvo permiso explícito
- [ ] Dejar que lean y entiendan los errores antes de resolverlos
- [ ] Estar atento a señales de frustración — recordar que los breaks existen para eso
- [ ] Preguntar proactivamente por necesidades de accesibilidad (texto, zoom)

### Después del taller
- [ ] Seguir en contacto con el grupo (canal de chat, redes)
- [ ] Anotar durante el taller cualquier error/problema del tutorial para reportarlo (PR o issue)
- [ ] Invitar a las participantes a la comunidad Python local
- [ ] Compartir feedback con el equipo de Django Girls (hello@djangogirls.org)

---

## 6. Enlaces de referencia

- Manual de coaching: https://coach.djangogirls.org
  - Info básica: https://coach.djangogirls.org/intro/
  - Reglas y tips: https://coach.djangogirls.org/tips/
  - Después del taller: https://coach.djangogirls.org/summary/
  - Cómo contribuir: https://coach.djangogirls.org/contributing/
- Tutorial oficial (es): https://tutorial.djangogirls.org/es/
