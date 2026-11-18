#!/usr/bin/env python3
"""Empaqueta el HTML ya compilado y todos los recursos para GitHub Pages.

No requiere Quarto ni paquetes externos. Las páginas permanecen intactas,
excepto los atributos HTML de enlaces que originalmente apuntaban fuera de
_book/ hacia los recursos compartidos del proyecto.

Uso: python scripts/construir_sitio.py
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
from collections import Counter
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

PROJECT = Path(__file__).resolve().parent.parent
BOOK = PROJECT / '_book'
ATTR_RE = re.compile(r'(?P<head>\b(?:href|src|poster|data)\s*=\s*)(?P<q>["\'])(?P<url>.*?)(?P=q)', re.I | re.S)
EXTERNAL = {'http', 'https', 'mailto', 'tel', 'data', 'javascript', 'ftp'}


def convert_link(raw: str, old_html: Path, dest_relative_html: Path) -> tuple[str, bool]:
    """Conserva URLs externas; adapta las que salen de _book."""
    raw_unescaped = html.unescape(raw)
    if not raw_unescaped or raw_unescaped.startswith(('#', '//', '/')):
        return raw, False
    parsed = urlsplit(raw_unescaped)
    if parsed.scheme.lower() in EXTERNAL or parsed.netloc or parsed.scheme:
        return raw, False
    if not parsed.path:
        return raw, False
    target = (old_html.parent / unquote(parsed.path)).resolve()
    try:
        subpath = target.relative_to(PROJECT)
    except ValueError:
        raise ValueError(f'URL fuera del proyecto: {old_html}: {raw}')
    if not target.is_file():
        # Some href links may reference an HTML anchor or a folder. Preserve
        # these, but report actual missing file links during validation.
        return raw, False
    if subpath.parts[0] == '_book':
        return raw, False
    # The output directory has resources/ and fuentes-docente/ at its root.
    new_path = Path(os.path.relpath(subpath.as_posix(), dest_relative_html.parent.as_posix()))
    url_path = quote(new_path.as_posix(), safe='/@:+$-_.~%')
    new_url = urlunsplit(('', '', url_path, parsed.query, parsed.fragment))
    return html.escape(new_url, quote=True).replace('&#x27;', '&#39;'), True


def render(out: Path) -> Counter:
    if not BOOK.is_dir() or not (BOOK / 'index.html').exists():
        raise SystemExit('No se encuentra _book/index.html. Compile el libro primero.')
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(BOOK, out)
    for folder in ('recursos', 'fuentes-docente'):
        if (PROJECT / folder).is_dir():
            shutil.copytree(PROJECT / folder, out / folder)
    (out / '.nojekyll').write_text('', encoding='utf-8')

    stats = Counter()
    for original in sorted(BOOK.rglob('*.html')):
        relative = original.relative_to(BOOK)
        destination = out / relative
        source = destination.read_text(encoding='utf-8')

        def change_match(match: re.Match) -> str:
            new_value, changed = convert_link(match.group('url'), original, relative)
            if changed:
                stats['referencias_adaptadas'] += 1
                return f"{match.group('head')}{match.group('q')}{new_value}{match.group('q')}"
            return match.group(0)

        updated = ATTR_RE.sub(change_match, source)
        if updated != source:
            destination.write_text(updated, encoding='utf-8')
            stats['paginas_con_rutas_adaptadas'] += 1
        stats['paginas_html'] += 1
    stats['archivos_publicados'] = sum(1 for p in out.rglob('*') if p.is_file())
    stats['tamano_mib'] = round(sum(p.stat().st_size for p in out.rglob('*') if p.is_file())/1024**2, 1)
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--salida', type=Path, default=PROJECT / '_publicar', help='Carpeta de sitio web')
    args = parser.parse_args()
    stats = render(args.salida.resolve())
    print('Sitio preparado:', args.salida.resolve())
    for key, value in stats.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
