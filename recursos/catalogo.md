# Recursos, fuentes y skills

Actualizado el 21 de noviembre de 2026. La columna de estado indica con qué puede trabajar hoy la siguiente herramienta.

| Recurso | Estado | Uso y ubicación |
|---|---|---|
| Objetivos, decisiones aprobadas y pendientes | Registrados por Pablo | [Punto de relevo](../CONTINUIDAD.md). |
| Método de extracción de Víctor Heras | Cinco consultas listas | [Guía de NotebookLM](../notebooklm/extraer-metodo.md). El cuaderno completo lo tiene Pablo. |
| Cerebro_Heras.md | Pendiente de la primera extracción verificable | Destino previsto: `notebooklm/Cerebro_Heras.md`. Cada ficha debe llevar un ejemplo y una referencia legible fuera del cuaderno. |
| Comentarios, vistas y estilos de dos publicaciones de Norbey | Referencias comprobadas y vistas de captura | [Línea base con enlaces a ambas publicaciones](../seguimiento/linea-base.md). |
| Calendario oficial del certamen | Verificado | [Miss Universe Puerto Rico](https://muniversepr.com/noticias/miss-universe-anuncia-la-fecha-oficial-de-la-edicion-75-en-puerto-rico/). |
| Retratos IA, WhatsApp y voces | Pablo confirma su existencia. Falta incorporar la selección para producción. | [Inventario por banda](../produccion/inventario.md). Guardar nombre de versión y ubicación autorizada de cada recurso. |
| Guion, calendario y dinámica de voto | Listos como propuestas. La primera frase de Norbey está aprobada. | [Plan de 20](../campana/plan-20-tiktoks.md) y [reglas](../campana/votacion-y-medicion.md). |
| Mediciones de la campaña | Registros preparados. Las filas se completan con datos reales. | [Por pieza](../seguimiento/publicaciones.csv) y [por candidata](../seguimiento/candidatas.csv). |

## Skills disponibles en el proyecto

| Skill | Usarla cuando | Qué entrega |
|---|---|---|
| [Extraer el método de Heras](../.agents/skills/extraer-metodo-heras/SKILL.md) | Llega una tanda del cuaderno o hay que pedirla. | Fichas trazables y cobertura de las fuentes. |
| [Preparar un TikTok](../.agents/skills/preparar-tiktok/SKILL.md) | Se elige una pieza del calendario y hay material para escribirla o mejorarla. | Guion filmable y atribución clara de datos, frases e hipótesis. |
| [Retomar la campaña](../.agents/skills/retomar-campana/SKILL.md) | Cambia el agente o se completa un avance que debe sobrevivir al chat. | Estado actualizado con evidencias, dependencias y siguiente acción. |

Estas tres skills describen cómo trabajar en este proyecto. Para convertir conocimientos específicos de Heras en nuevas skills, el [Issue #5](https://github.com/pablohernareypro/misuniverse24nov/issues/5) depende de los resultados del [Issue #2](https://github.com/pablohernareypro/misuniverse24nov/issues/2).

## Qué skills desarrollar con el cuaderno

| Decisión editorial | Evidencia que necesitamos | Prueba de aceptación |
|---|---|---|
| Elegir ideas de interés para alguien que no conoce al elenco | Criterios de selección y un caso localizado en un video original. | Comparar dos ideas del chat y justificar cuál producir primero. |
| Construir aperturas y relatos | Un ejemplo donde el autor explique por qué un arranque o estructura funciona y bajo qué condiciones. | Proponer dos primeros planos para el mismo intercambio, con promesa y remate comprobables. |
| Leer resultados y ajustar la siguiente pieza | Recomendaciones trazables con plataforma, métrica y límites claros. | Proponer una decisión con las métricas de Norbey y reconocer cuándo faltan datos. |

Para promover una ficha a skill, documentar su entrada, procedimiento, salida, referencia original y un caso donde no se pueda concluir. Guardar las instrucciones en `.agents/skills/<nombre>/SKILL.md` y enlazar el caso probado en el Issue. [Documentación de skills de Antigravity](https://antigravity.google/docs/skills)
