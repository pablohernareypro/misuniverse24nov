# Cómo trabajar en este repositorio

Este proyecto se lleva en español con Pablo. El destino de trabajo es `pablohernareypro/misuniverse24nov`. El repositorio es público.

Pablo Hernández dirige este proyecto. Norbey Rodríguez representa a Miss Colombia. Cualquier nuevo acceso a NotebookLM requiere autorización expresa de Pablo para ese paso. Un permiso para actualizar GitHub cubre el repositorio. Consulta la [entrega vigente](GEMINI.md) para distinguir los acuerdos, las propuestas y las preguntas pendientes.

## Al abrir una sesión

1. Lee [GEMINI.md](GEMINI.md), [README.md](README.md) y [CONTINUIDAD.md](CONTINUIDAD.md). Contrasta el último avance con los commits recientes y los [Issues abiertos](https://github.com/pablohernareypro/misuniverse24nov/issues).
2. Identifica qué puede hacerse con el material de hoy. Consulta [el catálogo](recursos/catalogo.md) y abre solo la skill o el recurso que haga falta.
3. Conserva las decisiones aprobadas. Si un dato cambia una decisión de publicación y no consta, formula una pregunta concreta a Pablo y avanza en lo que sí tenga evidencia.

## Durante el trabajo

- Cuando Pablo corrija una meta, actualiza [objetivos.json](campana/objetivos.json), los registros y los documentos que la citan. Ejecuta `python3 scripts/validar_proyecto.py` antes de publicar el cambio.
- Registra hechos con su origen, propuestas como propuestas y cifras con hora de corte. Un guion queda escrito al guardarlo. Una publicación queda publicada cuando hay URL comprobable.
- Captura un punto de avance en cuanto haya una pieza utilizable, un insumo nuevo o una decisión aprobada. Así la siguiente herramienta puede recuperar incluso una sesión que se interrumpió a la mitad.
- Guarda el archivo del proyecto junto con la entrada de continuidad correspondiente en un commit descriptivo. Si la tarea queda parcial, consigna lo que ya sirve y qué falta. Verifica que el commit se ve en el remoto.
- Lleva el detalle de las tareas en Issues. Cierra cada Issue al cumplir su criterio de aceptación y añade el vínculo a la evidencia. Una sola copia de cada tabla de cifras es suficiente.
- Este repositorio reúne material de producción publicable. Para originales o conversaciones privadas, conserva una descripción o referencia sin teléfonos ni datos personales y añade solo los fragmentos que el equipo seleccione para compartir.
- Para un principio atribuido a Víctor Heras, conserva título, localizador y contexto. El plan editorial de Pablo y los datos de Norbey tienen sus propias fuentes.

## Para cambiar de herramienta

Ejecuta la skill de [continuidad](.agents/skills/retomar-campana/SKILL.md). Deja fecha, lo que cambió, la evidencia, el bloqueo real y una próxima acción concreta. [ANTIGRAVITY.md](ANTIGRAVITY.md) contiene el prompt de entrada para otra sesión.
