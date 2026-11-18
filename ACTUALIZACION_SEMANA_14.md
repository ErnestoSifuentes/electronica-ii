# Semana 14 integrada — Electrónica II

Base: proyecto editable y HTML hasta la Semana 13. No se han modificado los contenidos de semanas 1 a 13.

## Contenidos

- Clase 40: Lección 9, teoría de filtros analógicos con deducciones RC PB y PA, ejemplos originales, figuras, aproximaciones Butterworth, Chebyshev y Bessel; resumen manuscrito del video asignado en semana 13: https://www.youtube.com/watch?v=WGq5t4VUoQQ.
- Clase 41: Práctica 11 TD5A, ¼ puente de Wheatstone, AI, NI myDAQ, LabVIEW; entrega del diseño teórico y reporte de la Práctica 10.
- Clase 42: continuación de Práctica 11, entrega de experimentos Lección 9 y trabajo del cuestionario.
- Clase 45 (semana 15): entrega del cuestionario L9, conforme a la planificación de semana 14.
- Multisim: cuatro circuitos originales `.ms14`; LabVIEW: tres VI originales `.vi`; hoja de cálculo `.xlsx`; PDF originales; 19 tutorías IA nuevas.

## Notas técnicas

- La guía de Práctica 11 dice 20–140 °C en el objetivo, pero una de sus figuras dice 20–120 °C. Se sigue el objetivo y se documenta la discrepancia.
- El sensor TD5A se describe con los datos proporcionados por la guía, sin verificación independiente de una hoja de datos.
- En el cálculo de ganancia del AI, 2.2 kΩ produce ganancia aproximada 10.09 y puede rebasar 5 V; se indica comprobar el margen.
- Resolución de ADC no equivale a exactitud de temperatura.
- La planificación de semana 13 daba fecha de diseño teórico de P11 en clase 44, pero la propia planificación de semana 14 solicita entrega en clase 41; esta última prevalece en la agenda semanal, sin alterar la original.
- Los resultados experimentales deben obtenerse en laboratorio, no se inventaron.

## Compilación

El entorno no cuenta con ejecutable Quarto. El libro HTML se actualiza mediante Pandoc sobre el HTML Quarto anterior y conserva los estilos, scripts y estructura de navegación. En un equipo con Quarto ejecute `quarto render --to html`. Abrir `ABRIR_LIBRO.html` para explorar el HTML incluido.
