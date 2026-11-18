# Electrónica II · Libro en Quarto

## Abrir el libro

1. Extraiga todo el ZIP en una carpeta de su equipo.
2. Abra `_book/index.html` en su navegador para consultar la versión HTML incluida. Mantenga el contenido de `_book` junto para que funcionen las imágenes y los enlaces.
3. Para editar el libro, abra en PowerShell la carpeta que contiene `_quarto.yml` y ejecute `quarto preview`. Use `quarto render --to html` para regenerar `_book` antes de distribuir o publicar el libro.

La lectura de los apuntes y los recursos incluidos funciona desde el HTML. El video, las referencias en línea y el enlace a ChatGPT requieren conexión. Para buscar en todo el libro desde un servidor local, utilice `quarto preview`.

## Incorporar una lección

- Cree un archivo `.qmd` dentro de la carpeta de su semana en `semanas/`. Use `semanas/01/divisor-de-voltaje.qmd` como ejemplo para organizar la explicación, las figuras, la simulación, el laboratorio y las consignas.
- En `_quarto.yml`, agregue la lección bajo `chapters` de la semana correspondiente. Las semanas 01 y 02 muestran la sintaxis con `part`. Añada la entrada al índice `lecciones.qmd`. En las semanas con una agenda como página única, convierta esa entrada en `part` al agregar su primera lección.
- Coloque los materiales descargables en `recursos/semana-NN/` y añada los enlaces desde la lección. Quarto copia los recursos a `_book` al renderizar.
- Para agregar una consigna, reutilice el bloque `.tutor-box` de la lección inicial. El botón toma el texto de `.tutor-texto` y lo copia para que el estudiante lo pegue en ChatGPT.

## Fuentes del curso

La agenda agrupa las 48 clases del syllabus del Grupo A (2026) en bloques consecutivos de tres. Las agendas de las semanas 1 a 5 siguen sus planificaciones semanales. La planificación de la Semana 3 ubica la continuación de la Lección 1 en la clase 7 y la Práctica 1 en las clases 8 y 9. Para las entregas posteriores, se aplican las planificaciones de las semanas 4 y 5. El resumen del video L2 se entrega en la clase 11. Los Ejercicios propuestos L1 y la simulación de los ejemplos L3 se entregan en la clase 15. Los Ejercicios propuestos L3 se entregan en la clase 18.

La ponderación general del encuadre web procede de la página 4 del syllabus del Grupo A. La diapositiva 26 del encuadre original contiene otra distribución. Para la práctica del amplificador diferencial, la numeración del syllabus pasa de práctica 6 a práctica 8 y menciona el reporte de práctica 7 en la clase 32.

El syllabus original y los tres diagramas editables en Visio se encuentran en `fuentes-docente/`. En la Semana 2, la guía de la actividad para estudiantes precisa la mención al TL084, el punto de operación y la lectura del polo dominante. En la Semana 3, el ejemplo de reporte de la Práctica 1 conserva la rúbrica y presenta el contenido técnico con los datos personales y la calificación retirados.

En la Semana 4 se incluyen la presentación de la Lección 2, la guía de la Práctica 2, los circuitos de ambas y el manual de NI myDAQ. En la Semana 5 se incluyen la presentación de la Lección 3, los ejercicios demostrativos y propuestos, el documento resuelto, sus hojas de cálculo, los circuitos y las dos guías Word v2 de la Actividad L3. Las guías v1 quedan disponibles en `fuentes-docente/semana-05/`. El ejemplo de reporte de simulación L3 se presenta como referencia de redacción, con los datos de identificación y las anotaciones retirados. La Lección 3 y los ejercicios demostrativos precisan los cálculos en los que se usan 10 y 15 Hz como frecuencia de corte en lazo abierto.

Para distribuir el libro a los estudiantes, comparta la carpeta `_book`.

## Actualización hasta la Semana 7 (16 de noviembre de 2026)

Las lecciones 4 y 5 incluyen teoría ampliada, ecuaciones de ganancia finita e ideal, figuras, simulaciones y enlaces a las presentaciones; se incorporan la Práctica 3, los Ejercicios L4, la Práctica 4 y los Ejercicios propuestos L5. Los archivos originales se organizaron en `recursos/semana-06/`, `recursos/semana-07/` y `fuentes-docente/` para las fuentes no públicas. Consulte `COMPILACION_HTML.md` para el detalle del HTML incluido y del comando de recompilación.

## Actualización: Semanas 8 y 9

- Las **semanas 8 y 9** se desarrollaron a partir de sus planificaciones específicas, presentaciones, prácticas y simulaciones. La Semana 8 comprende LabVIEW, resultado de una medida, Práctica 5 y ocho ejercicios integradores. La Semana 9 comprende Lección 6 (sumador inversor), Práctica 6 (termómetro LM35–myDAQ) y Ejercicios L6.
- La **Lección 6** se ubica ahora en Semana 9 porque así lo determina su planificación entregada. El marcador previo en Semana 10 se archivó para evitar duplicidad; esa semana continúa pendiente de nuevos materiales.
- El **Tutor IA** incluye seis consignas nuevas para Semana 8 y siete para Semana 9. Conserva los botones de copia y el acceso a ChatGPT; no es un chatbot autónomo integrado en el sitio.
- La carpeta `recursos/semana-08` conserva los documentos originales, los tres VI y las figuras del material de clase. La carpeta `recursos/semana-09` conserva los documentos, cinco archivos `.ms14` útiles y figuras. Las copias de seguridad de Multisim se conservan en la carpeta `fuentes-docente/semana-09`.
- **Importante:** la Práctica 6 se refiere a programas LabVIEW alojados en el aula virtual, pero estos VI no estaban en el ZIP de la semana 9; no se han inventado ni reemplazado.
- El HTML incluido se produjo mediante **Pandoc** e integración en la estructura gráfica y de navegación de Quarto preexistente; para recompilación nativa use `quarto render --to html` con Quarto instalado.
- Para abrir el HTML completo sin instalar programas, extraiga todo el ZIP y ejecute `ABRIR_LIBRO.html`; las páginas están en `_book`.

## Actualización: Semana 12

La Semana 12 se amplió en tres páginas: **Lección 8 (parte 1): integrar y diferenciar voltajes**, **Práctica 9: LM35 y myDAQ (opción 3)** y **simulaciones guiadas en Multisim**. La agenda respeta las entregas de las clases 34 a 36; el video de la Lección 8 se acompaña de una consigna de resumen manuscrito, y el video preparatorio de la semana 13 conserva su propia fecha. El Tutor IA incorpora 11 consignas. La navegación, el calendario y la portada incluyen accesos a la semana 12. Consulte `ACTUALIZACION_SEMANA_12.md` para notas técnicas, materiales fuente y alcance de las verificaciones.

## Semana 13

- Se integró la Lección 8 (parte 2), Práctica 10 de amplificador de instrumentación, ejemplos Multisim y lecturas complementarias.
- Se conservaron los documentos originales y el ZIP del docente.
- Se asignaron videos, resúmenes y entregas conforme a la planificación, además de 12 consignas Tutor IA.
- La edición HTML se integró con Pandoc sobre la estructura Quarto existente; en un equipo con Quarto use `quarto render --to html`.

## Semana 14: filtros analógicos y termómetro TD5A

Se integró la Lección 9 con teoría y figuras, los experimentos RC en Multisim y LabVIEW, la Práctica 11 con hoja XLSX y el Cuestionario L9; se conservan las fuentes completas en `fuentes-docente/semana-14/Semana_14_original.zip`. También se añadieron 19 consignas del Tutor IA, el video con actividad de resumen y las fechas de entrega de la planificación.

Se puede abrir el HTML incluido con `ABRIR_LIBRO.html` tras extraer el ZIP. Para una compilación nativa en una computadora con Quarto instalado, use `quarto render --to html`. Esta entrega generó/actualizó las páginas HTML con Pandoc y la plantilla visual Quarto previa; la prueba de navegador automático estuvo bloqueada por las políticas del entorno.

## Cierre del curso: semanas 15 y 16 (noviembre de 2026)

Las 16 semanas están incluidas. La **Lección 10** se organiza en dos capítulos completos: filtros activos pasa-bajas de **primer orden**, a partir de las tres primeras grabaciones, y filtros **Sallen–Key de segundo orden**, a partir de las grabaciones cuarta y quinta. Las cinco grabaciones están vinculadas desde el comienzo del capítulo que corresponde; se conservaron las consignas de apuntes manuscritos y las entregas de las clases **45** y **47**.

Los capítulos incorporan deducciones matemáticas, funciones de transferencia, ejemplos resueltos y figuras redibujadas a partir de los cinco documentos académicos Word elaborados previamente. Las versiones originales de dichos Word se encuentran en `recursos/semana-15/` y `recursos/semana-16/`, junto con los PDF, minitutoriales y simulaciones Multisim.

La agenda de la semana 15 sigue su **planificación original**; la semana 16 utiliza la secuencia de 48 clases y las entregas fijadas en dicha planificación, además del enunciado de la **Actividad 3** y el **Examen U3** recibidos. No se atribuye una fecha de entrega no indicada a la Actividad 3.

El índice `lecciones.qmd` muestra **solo lecciones**. Los ejercicios, cuestionarios, evaluaciones, simulaciones, Word ampliados y demás archivos permanecen en los apartados **Recursos** de las semanas correspondientes. El Tutor IA incluye 14 consignas nuevas (6 en semana 15 y 8 en semana 16) y el proyecto Quarto y HTML se entregan juntos.

El sitio HTML incluido se produjo mediante Pandoc y se integró en los archivos visuales y de navegación Quarto del paquete base. No equivale a una compilación nativa de Quarto, que puede ejecutar en Windows con `quarto render --to html` dentro del proyecto. Los archivos de video MP4 comprimidos **no están dentro del ZIP**, para evitar duplicar aproximadamente 500 MB; cada lección enlaza sus videos de YouTube indicados en la planificación original.

### Organización del paquete HTML para descarga

Para evitar duplicar los archivos PDF, Word, figuras y simulaciones, el HTML entregado en `_book/` enlaza a la carpeta `recursos/` situada en el proyecto principal. **Extraiga el ZIP completo** y utilice `ABRIR_LIBRO.html`; no separe `_book/` de `recursos/` en esta entrega. Si requiere distribuir únicamente `_book/`, primero ejecute una compilación nativa con `quarto render --to html` para que Quarto copie de nuevo los recursos dentro del sitio.
