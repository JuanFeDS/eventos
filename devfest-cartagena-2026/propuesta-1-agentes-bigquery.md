# Propuesta 1 — Agentes analistas con ADK y BigQuery

Respuestas para el formulario del CFP de DevFest Cartagena 2026, en el orden en que aparecen.

---

## 1. Datos básicos

| Campo | Respuesta |
|-------|-----------|
| Nombre completo | Juan Felipe Martínez |
| Correo | jmartinezbernal02@gmail.com |
| WhatsApp | +57 311 875 6670 |
| Ciudad | TODO |
| País | Colombia |
| ¿Presencial el 28 de noviembre? | TODO |

## 2. Sobre ti

- **Organización / empresa**: Mercado Libre
- **Cargo o rol actual**: Data Scientist
- **Biografía profesional**:

  > Soy Data Scientist con más de seis años de experiencia diseñando soluciones basadas en datos e inteligencia artificial. Actualmente trabajo en Mercado Libre, donde desarrollo productos y modelos para resolver problemas de negocio a gran escala.
  >
  > A lo largo de mi carrera he trabajado en proyectos de machine learning, sistemas de recomendación, procesamiento de lenguaje natural, ingeniería de datos y, más recientemente, en el desarrollo de agentes de IA y automatización de procesos con Python.
  >
  > Me apasiona compartir conocimiento y construir soluciones prácticas que combinen ingeniería, ciencia de datos e inteligencia artificial para resolver problemas reales. En 2026 fui speaker en Pyday Boyacá y coach en Django Girls Boyacá.
- **Enlace a foto de perfil**: TODO

## 3. Redes y perfiles

- **LinkedIn**: https://www.linkedin.com/in/juanfe-martinez/
- **GitHub**: https://github.com/JuanFeDS

## 4. Tu propuesta

**Título**: Construye un equipo de agentes analistas con Google ADK y BigQuery

**Tipo de sesión**: Charla técnica

**Tema principal**: Gemini / Google AI

**Descripción de la sesión**:

En casi cualquier empresa, las respuestas a las preguntas de negocio ya están en una base de datos, pero para sacarlas hace falta saber SQL o esperar a que alguien del equipo de datos tenga tiempo. Un agente con acceso a BigQuery parece la solución obvia, hasta que le pides que consulte, grafique, revise y explique al mismo tiempo: se confunde, inventa columnas y es imposible saber en qué paso falló.

En esta sesión recorremos, con el código de un proyecto real en Python y Google ADK (Agent Development Kit), el camino de ese agente único a un equipo de agentes especializados. Un agente coordinador recibe la pregunta en español y delega en un agente de SQL que consulta BigQuery, uno de visualización que arma la gráfica y uno revisor que valida el resultado y lo explica en lenguaje natural. En cada paso vemos qué problema resuelve dividir el trabajo y cuál nuevo aparece: cómo se pasan contexto los agentes, cómo evitar que el de SQL lance consultas caras o peligrosas y cómo depurar cuando la respuesta final está mal.

**¿Qué se llevará la audiencia?**

- Cuándo un solo agente deja de ser suficiente y cómo reconocerlo antes de que el sistema se vuelva inmanejable
- Cómo estructurar un sistema multiagente en ADK: agente coordinador, subagentes especializados y herramientas de BigQuery
- Protecciones mínimas para conectar agentes a datos reales: permisos de solo lectura, control de costo de las consultas y un agente que revisa antes de responder
- El repositorio con el código completo de la demo para replicarlo en casa

**Nivel**: Intermedio

**Duración**: 30 minutos

## 5. Formato y material

- **¿Incluye código, demo o actividad práctica?**: Sí
- **Enlace a slides**: — (se construyen solo si la propuesta es aceptada)
- **Otros recursos**: https://github.com/JuanFeDS/eventos — material de charlas y talleres anteriores (Pyday Boyacá 2026, Django Girls Boyacá 2026)

## 6. Comunidad

**¿Por qué quieres participar como speaker en DevFest Cartagena 2026?**

Este año empecé a compartir en serio lo que hago: fui speaker en Pyday Boyacá y coach en Django Girls Boyacá, y en los dos espacios confirmé que lo que más disfruto es ver a alguien salir de una sesión con ganas de construir algo propio. Quiero participar en DevFest Cartagena porque los agentes de IA son hoy la parte de mi trabajo que más me emociona, y siento que hay mucho ruido y pocas explicaciones aterrizadas sobre cómo se construyen de verdad. Me gustaría aportar esa mirada práctica, de alguien que trabaja con datos todos los días, y de paso conocer y aprender de la comunidad tecnológica de la Costa.

**¿Cómo puede tu propuesta aportar a la comunidad tecnológica de Cartagena?**

Lleva los agentes de IA del demo vistoso a un caso de uso concreto que cualquier equipo tiene: hablar con los datos de su propio negocio o proyecto. Muestra un patrón de arquitectura (agentes especializados que colaboran) que sirve mucho más allá de BigQuery. La demo usa herramientas con capa gratuita y el código queda abierto, así que cualquiera puede replicarla al salir de la charla.

**¿Has participado en comunidades, espacios educativos, mentorías o iniciativas tecnológicas?**: Sí

En 2026 fui coach en Django Girls Boyacá, donde acompañé a un grupo de participantes que programaban por primera vez, desde la instalación hasta el despliegue de su blog en un día. También di la charla "Más allá del notebook: construyendo proyectos de Machine Learning que evolucionan" en Pyday Boyacá 2026.

## 7. Autorizaciones

Marcar las tres casillas (uso de imagen, autoría del material, información correcta).
