# Actualización del Tutor IA hasta la Semana 7

- Se conservaron las consignas existentes en semanas 1–5.
- Se incorporaron 11 consignas específicas: cuatro para semana 6 y siete para semana 7.
- Se añadieron secciones en el índice general Tutor IA, con enlaces directos y anclas a cada consigna.
- Las nuevas páginas usan las cajas y el botón **Copiar consigna** con el mismo script que las anteriores, más el enlace **Abrir ChatGPT**.
- Se añadieron accesos desde portada y las agendas de semanas 6 y 7.
- Pedagogía: trato de usted, preguntas secuenciales, espera de respuestas, comprobación de unidades y evidencia, sin inventar mediciones ni revelar respuestas antes de que el estudiante razone.
- No se incorporó un chatbot autónomo dentro del HTML: las consignas se copian y se llevan a ChatGPT, igual que en semanas 1–5. No se requiere clave API.
- La compilación incluida conserva la estructura Quarto original, y las páginas modificadas se actualizaron con Pandoc porque Quarto no está instalado en este entorno. Para compilar todo nativamente: `quarto render --to html`.
