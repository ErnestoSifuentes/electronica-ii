# Actualización del libro de Electrónica II — Semana 12

## Alcance académico

Se parte exclusivamente de la versión `Libro_Electronica_II_Quarto_Hasta_Semana_11_VIDEO_L7_PARTE2_INTEGRADO.zip`, sin sustituir ni reescribir los archivos `.qmd` de las semanas 1–11.

- **Semana 12 (clases 34–36):** agenda y fechas de entrega según `Planificación_Semana_12.pdf`.
- **Lección 8 (parte 1):** integración y diferenciación de voltajes, modelo inversor con impedancias, demostración por LCK, integrador ideal y con RF, derivador ideal y con R1, cinco ejemplos de la presentación, respuesta temporal, análisis de frecuencia y validación numérica.
- **Práctica 9 (opción 3):** LM35, buffer de referencia, amplificador diferencial de cuatro resistencias, NI myDAQ, LabVIEW (eventos Timeout, Adquirir, Procesar, Guardar), 20 lecturas por temperatura, interpretación y reporte.
- **Multisim:** cinco circuitos principales `.ms14` y enlaces de descarga, con predicciones analíticas para comparar.
- **Tutor IA:** 11 consignas de preguntas secuenciales y trato de usted, con enlaces desde la agenda y el índice.
- **Videos/resúmenes:** video de preparación de L8 parte 1 (`WOLdf93fl-k`) y resumen manuscrito para clase 34; enlace de preparación para clase 37 (`aGGxoPQJmRg`) sin adelantar los contenidos de la semana 13.

## Observaciones técnicas que no modifican los originales

1. Presentación L8, integrador práctico del ejemplo 3: magnitud calculada a 100 Hz = 0.0159 V/V, distinta del valor 0.09 impreso en la diapositiva 13.
2. Presentación L8, derivador práctico del ejemplo 2: magnitud calculada a 1 Hz = 0.0628 V/V, distinta del valor 0.0039 impreso en la diapositiva 24.
3. Práctica 9: los valores nominales del divisor (5.1 kΩ y 220 Ω, 5 V) generan aproximadamente 206.77 mV, mientras que el diseño ideal requiere 200 mV; las razones de resistencias 5.6 kΩ / 1 kΩ dan G=5.6, distinto de 5.5556 ideal.
4. La página 6 de la Práctica 9 muestra un valor textual de 120 °C en el cálculo del extremo superior, pero el rango requerido es 20–110 °C y Vs,max es 1.1 V para 110 °C.
5. El objetivo de resolución de 0.01 °C no debe reportarse como exactitud del sensor ni del sistema.
6. El programa `.vi` reutilizado de Práctica 7 se menciona en la guía, pero no estaba en el ZIP de semana 12: se conserva la instrucción de aprovechar el trabajo del estudiante sin inventar un VI.

## Archivos de entrada

- El ZIP original se conserva como `fuentes-docente/semana-12/Semana_12_original.zip`.
- Los PDF necesarios están en `recursos/semana-12/`.
- Los cinco archivos `.ms14` principales están en `recursos/semana-12/simulaciones/`; las copias de seguridad originales se conservan en el ZIP fuente.

## Compilación HTML y verificación

- Se añadieron las páginas QMD y se actualizaron `_quarto.yml`, portada, calendario, índice de lecciones y Tutor IA.
- **62 páginas HTML** en `_book` (el proyecto hasta semana 11 contenía 60).
- Los HTML nuevos se generaron con Pandoc y se integraron a la estructura visual, JavaScript y navegación de Quarto ya existente; **no es una ejecución nativa de Quarto**, que no se encontraba instalado.
- La comprobación automatizada no encontró enlaces locales ni anclas rotas; el índice de búsqueda se reconstruyó para las 62 páginas.
- Los 46 archivos fuente `.qmd` y los textos principales de las 46 páginas HTML de semanas 1–11 se compararon con el ZIP base y resultaron idénticos.
- La ejecución de Chromium para la inspección visual interactiva fue bloqueada por la configuración del entorno. No se afirma haber realizado una prueba completa en navegador.

Para la compilación nativa, con Quarto instalado, ejecute `quarto render --to html` dentro de la carpeta raíz del proyecto. Para abrir el HTML incluido, extraiga el ZIP completo y haga doble clic en `ABRIR_LIBRO.html`.
