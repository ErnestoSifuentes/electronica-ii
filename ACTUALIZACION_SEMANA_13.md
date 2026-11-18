# Actualización — Semana 13

Base: Libro de Electrónica II hasta Semana 12 con Tutor IA. Se respetan archivos `.qmd` de semanas 1–12.

## Contenido

- Clase 37: Lección 8, parte 2 (derivador inversor, análisis ideal y práctico, dos ejemplos, simulación) y entrega de resumen manuscrito del video asignado en la semana 12: https://www.youtube.com/watch?v=aGGxoPQJmRg.
- Clase 38: Práctica 10 (AI de tres op-amp y siete resistencias; offset, GD, GC, CMRR y desbalance) y entrega del reporte de la Práctica 9.
- Clase 39: continuación de Práctica 10 y entrega de simulaciones de ejemplos L8, parte 2.
- Extra clase: video https://www.youtube.com/watch?v=WGq5t4VUoQQ y resumen a mano en clase 40 (semana 14); preparación del diseño teórico de Práctica 11 sobre RTD, puente W y AI, con entrega en clase 44 (semana 15).
- Tutor IA: 12 consignas nuevas (una pregunta por turno, tratamiento de usted, sin inventar datos).

## Observaciones técnicas

- La diapositiva 24 presenta |A|=0.0039 a 1 Hz, pero con R1=1 kΩ, RF=10 kΩ, C1=1 µF, la fórmula da |A|=0.0628 V/V; verifique en Multisim.
- La guía de Práctica 10 presenta una convención de signo no homogénea entre ecuaciones: usar un orden declarado de entradas y comprobar fase de la salida.
- La ecuación (14) de la guía expresa una suma de recíprocos en dB: no sumar recíprocos de niveles logarítmicos al calcular el CMRR experimental.
- No se generaron mediciones experimentales.

## Archivo original y compilación

- `fuentes-docente/semana-13/Semana_13_original.zip` conserva las fuentes completas (incluidas las copias de seguridad de Multisim).
- Los circuitos `.ms14` publicables se encuentran en `recursos/semana-13/simulaciones/`.
- Abrir `ABRIR_LIBRO.html` o ejecutar `quarto render --to html` en una instalación local de Quarto.

## Verificación final

- 65 páginas HTML configuradas en `_quarto.yml` y publicadas en `_book`.
- Comprobación estructural de enlaces locales, anclas y recursos: sin errores detectados.
- Los 56 archivos `.qmd` de las semanas 1–12 coinciden con la versión anterior, sin modificaciones.
- La prueba interactiva automatizada con Chromium fue bloqueada por la política del entorno (`ERR_BLOCKED_BY_ADMINISTRATOR`), tanto para enlaces locales como para servidor HTTP. No se afirma haber completado dicha prueba.
