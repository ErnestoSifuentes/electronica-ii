# Electrónica II: primera edición para GitHub Pages

El proyecto contiene los 16 módulos semanales, el libro HTML, los archivos
`.qmd`, recursos descargables, las carpetas de materiales originales, videos
enlazados y el Tutor IA.

**Todo el material del paquete se conserva.** Durante la publicación GitHub
Actions genera un sitio web temporal sin duplicar los PDF, documentos y
simulaciones dentro del repositorio.

## Publicar por primera vez (Windows)

1. Inicie sesión en [GitHub](https://github.com/) y cree un repositorio nuevo
   **público**, por ejemplo `electronica-ii`. Utilice la rama `main`.
2. Abra **GitHub Desktop** (https://desktop.github.com/). Clone el repositorio
   vacío en su equipo.
3. Descomprima este archivo y copie **el contenido interior** de la carpeta
   `Libro_Electronica_II_Quarto` dentro de la carpeta del repositorio clonado.
   Incluya también las carpetas ocultas `.github` y el archivo `.gitignore`.
   No copie únicamente `_book`: necesitamos también `recursos/`,
   `fuentes-docente/`, `semanas/` y los archivos `.qmd`.
4. En GitHub Desktop, escriba un comentario como «Publicación inicial del
   libro de Electrónica II», seleccione **Commit to main** y después
   **Push origin**.
5. En GitHub (en el navegador), abra su repositorio y entre a
   **Settings → Pages → Build and deployment → Source → GitHub Actions**.
6. En la pestaña **Actions** se ejecutará «Publicar libro Electrónica II».
   Si la ejecución inicial fue anterior a la configuración de Pages, elija
   el flujo y use «Run workflow» para publicarlo manualmente.
7. Cuando termine correctamente, GitHub mostrará la dirección del libro,
   habitualmente `https://USUARIO.github.io/electronica-ii/`.

**Nota:** subir el archivo ZIP tal cual al repositorio NO publica su contenido.
Primero hay que extraerlo y subir los archivos.

## Comprobar el sitio antes de subirlo

Desde PowerShell, dentro de `Libro_Electronica_II_Quarto`:

```powershell
python scripts/construir_sitio.py
python scripts/validar_sitio.py
python -m http.server 8000 --directory _publicar
```

Luego abra `http://localhost:8000/` en el navegador. Para detener la vista
previa pulse `Ctrl+C` en la consola.

## Cómo actualizar el libro

1. Modifique los archivos `.qmd` y sus recursos.
2. Si hay cambios de contenido, ejecute `quarto render --to html` para
   actualizar `_book`. Una vez generado, compruebe los enlaces.
3. En GitHub Desktop, haga **Commit to main** y **Push origin**.
4. GitHub Actions reconstruirá automáticamente el sitio público.

La carpeta `_publicar` es temporal y **no debe subirse al repositorio**.
El flujo de publicación se encarga de construirla. Los archivos fuente del
libro, las figuras, las prácticas, los archivos descargables y las consignas
no se alteran por este proceso.

## Consideraciones antes de hacerlo público

- Verifique que cuenta con permiso para distribuir públicamente manuales,
  presentaciones y otros materiales de terceros presentes en el repositorio.
- Los enlaces a YouTube no almacenan una copia del video en GitHub.
- Los estudiantes pueden consultar el libro sin iniciar sesión. Para descargar
  ciertos recursos es necesario que su navegador admita el tipo de archivo;
  las simulaciones Multisim requieren el software correspondiente.
- El Tutor IA abre instrucciones y enlaces a ChatGPT; no ejecuta un modelo
  de inteligencia artificial alojado en GitHub Pages.
- Si los estudiantes deben entregar prácticas o tareas, mantenga esa gestión
  en el aula virtual institucional: GitHub Pages es un sitio estático.

## Si hay un error de publicación

Abra la pestaña **Actions** de GitHub y consulte el registro de ejecución.
Los errores de rutas locales pueden detectarse con el validador incluido.
Para cuestiones de publicación, consulte
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
