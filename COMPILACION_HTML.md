# Registro de compilación y edición

- Base: libro Quarto ampliado hasta la Semana 05; sus fuentes y sus recursos se conservan.
- Semanas 06–07: se ampliaron las lecciones y se incorporaron páginas Quarto adicionales para prácticas y ejercicios.
- Materiales originales de Multisim: archivos `.ms13` y `.ms14` proporcionados por el docente. Los archivos temporales y copias de seguridad no se incluyen como material público.
- Material de evaluación U1: guardado solamente en `fuentes-docente/semana-06/examen-unidad-1.pdf`, no dentro de `_book`.
- Se preserva la página original de introducción a LabVIEW: la planificación la menciona, pero su presentación no estaba en los ZIP de Semana 7.
- Versión HTML incluida: los capítulos nuevos se generaron mediante Pandoc 3.1.11.1 y se incorporaron a la maqueta Quarto original, pues `quarto` no está disponible en el entorno de elaboración. Se mantuvieron sus hojas de estilo, bibliotecas JavaScript y navegación; el libro es consultable en `_book/index.html`.
- Para **regenerar nativamente** todo el libro en un equipo con Quarto: abrir una terminal en esta carpeta y ejecutar `quarto render --to html`. El proyecto se mantiene editable por medio de los archivos `.qmd`, `_quarto.yml` y `estilos.css`.

## Actualización a semanas 08 y 09

- Se conservaron las hojas de estilo anteriores y la estructura de la portada. Se añadieron botones de acceso a Semanas 8 y 9 y su navegación lateral.
- Se añadieron siete páginas de contenido técnico y dos agendas nuevas a partir de los ZIP entregados; los capítulos originales de las semanas 1–6 permanecen idénticos, y en Semana 7 se actualizaron dos referencias a la presentación de LabVIEW disponible a partir de Semana 8.
- Total esperado en `_quarto.yml`: 53 páginas HTML configuradas.
- Tutor IA con 13 consignas nuevas.
- Quarto no estaba disponible en la máquina de elaboración, así que el HTML incluido es una edición navegable integrada mediante Pandoc en la plantilla HTML Quarto original, no una ejecución nativa de `quarto render`.
- Verificaciones automáticas: archivos locales, destinos de enlaces, anclas de navegación y lectura de ZIP. La validación interactiva en navegador no se pudo completar debido a restricciones de ejecución del navegador en este entorno.

## Actualización a Semana 12

- Se integraron Lección 8 (parte 1), Práctica 9 (opción 3) y simulaciones de ejemplos L8, tomando la planificación semanal como fuente.
- Se incorporaron **11 consignas Tutor IA** y los enlaces de video/resumen, con botón de acceso en la portada y en la agenda.
- El proyecto tiene **62 páginas HTML** configuradas. El HTML publicado se generó con Pandoc en la estructura Quarto conservada, no mediante ejecución de `quarto render` en este entorno.
- Validación automática de enlaces locales, anclas y correspondencia de QMD anterior, sin errores detectados. No se completó prueba visual con Chromium por bloqueo del entorno.
- Consulte `ACTUALIZACION_SEMANA_12.md` para detalles y notas numéricas.

## Semana 13

- Se integró la Lección 8 (parte 2), Práctica 10 de amplificador de instrumentación, ejemplos Multisim y lecturas complementarias.
- Se conservaron los documentos originales y el ZIP del docente.
- Se asignaron videos, resúmenes y entregas conforme a la planificación, además de 12 consignas Tutor IA.
- La edición HTML se integró con Pandoc sobre la estructura Quarto existente; en un equipo con Quarto use `quarto render --to html`.

- **Semana 13:** el libro tiene 65 páginas HTML y 12 tutorías nuevas. La prueba automática interactiva de Chromium fue bloqueada por `ERR_BLOCKED_BY_ADMINISTRATOR`; sí se verificaron rutas, anclas, tablas y matemáticas del HTML generado. No se realizó compilación nativa de Quarto.

## Semana 14: filtros analógicos y termómetro TD5A

Se integró la Lección 9 con teoría y figuras, los experimentos RC en Multisim y LabVIEW, la Práctica 11 con hoja XLSX y el Cuestionario L9; se conservan las fuentes completas en `fuentes-docente/semana-14/Semana_14_original.zip`. También se añadieron 19 consignas del Tutor IA, el video con actividad de resumen y las fechas de entrega de la planificación.

Se puede abrir el HTML incluido con `ABRIR_LIBRO.html` tras extraer el ZIP. Para una compilación nativa en una computadora con Quarto instalado, use `quarto render --to html`. Esta entrega generó/actualizó las páginas HTML con Pandoc y la plantilla visual Quarto previa; la prueba de navegador automático estuvo bloqueada por las políticas del entorno.

## Integración final · Semanas 15 y 16

La entrega final incluye 71 páginas HTML y las páginas editables `.qmd`. Se incorporan las figuras originales generadas para los cinco documentos Word, sin capturas del pizarrón ni marcas temporales. Los enlaces a videos se encuentran al principio de las dos partes de la Lección 10, con la actividad de apuntes manuscritos, y los archivos docentes complementarios en Recursos por semana.

Debido a que el ejecutable de Quarto no está disponible en este entorno, se generó HTML con Pandoc y se insertó en las páginas Quarto de la edición anterior, conservando los estilos, búsqueda y navegación. Si dispone de Quarto, entre a la carpeta del proyecto y ejecute `quarto render --to html` para obtener una compilación nativa.

La versión ZIP utiliza recursos compartidos entre el proyecto editable y el HTML incluido: los enlaces de las páginas HTML apuntan a `../recursos` del proyecto, reduciendo duplicaciones sin omitir archivos. Es indispensable conservar juntas `_book/` y `recursos/` al abrir el sitio entregado. La recompilación con Quarto restaura la estructura independiente habitual de `_book`.
