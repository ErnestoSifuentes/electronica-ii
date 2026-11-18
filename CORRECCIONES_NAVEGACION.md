# Correcciones de presentación y navegación (17 de noviembre de 2026)

- La portada `index.qmd` y `_book/index.html` contienen ahora accesos directos a las semanas 1 a 7 y el calendario.
- Las agendas de las semanas 6 y 7 utilizan la misma estructura que las anteriores: tres columnas de actividades, entregas y trabajo para la semana siguiente.
- Se corrigieron los enlaces del menú lateral de las semanas 6 y 7 en **todas** las páginas HTML, usando rutas relativas válidas y el orden definido en `_quarto.yml`.
- Se actualizaron los contenidos HTML y el índice de búsqueda.
- Se conservaron las lecciones y materiales originales de las semanas 1 a 5.
- Esta versión HTML fue actualizada con Pandoc a partir de las fuentes `.qmd` y el sitio Quarto existente; para regenerarla íntegramente mediante Quarto en un equipo con la herramienta instalada, ejecutar `quarto render --to html`.
