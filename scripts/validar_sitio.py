#!/usr/bin/env python3
"""Verifica enlaces relativos, destinos y anclas de la versión pública."""
from __future__ import annotations

import argparse
import os
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

PROJECT = Path(__file__).resolve().parent.parent
EXTERNAL = {'http', 'https', 'mailto', 'tel', 'data', 'javascript', 'ftp'}
CSS_URL = re.compile(r'url\(\s*["\']?(.*?)["\']?\s*\)', flags=re.I)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        if ad.get('id'):
            self.ids.add(ad['id'])
        if tag == 'a' and ad.get('name'):
            self.ids.add(ad['name'])
        for k in ('href', 'src', 'poster', 'data'):
            if ad.get(k):
                self.links.append(ad[k])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sitio', type=Path, default=PROJECT / '_publicar')
    args = ap.parse_args()
    base = args.sitio.resolve()
    if not (base / 'index.html').is_file():
        raise SystemExit(f'No existe la portada {base / "index.html"}')
    pages = {p.resolve(): PageParser() for p in base.rglob('*.html')}
    for p, parser in pages.items():
        parser.feed(p.read_text(encoding='utf-8'))
    errors=[]
    stats=Counter()
    for p, parser in pages.items():
        stats['paginas_html'] += 1
        for link in parser.links:
            u=urlsplit(link)
            if u.scheme in EXTERNAL or u.scheme or u.netloc or link.startswith('//'):
                stats['enlaces_externos']+=1
                continue
            if not u.path and not u.fragment:
                continue
            if u.path.startswith('/'):
                errors.append((str(p.relative_to(base)),link,'ruta absoluta no portable'))
                continue
            t=(p.parent / unquote(u.path)).resolve() if u.path else p
            try:
                t.relative_to(base)
            except ValueError:
                errors.append((str(p.relative_to(base)),link,'sale fuera del sitio'))
                continue
            if not t.exists():
                errors.append((str(p.relative_to(base)),link,'no existe'))
                continue
            stats['enlaces_locales_validos']+=1
            if u.fragment and t.suffix.lower()=='.html':
                if t in pages and unquote(u.fragment) not in pages[t].ids:
                    errors.append((str(p.relative_to(base)),link,'ancla no encontrada'))
                else: stats['anclas_validas']+=1
    for css in base.rglob('*.css'):
        for raw in CSS_URL.findall(css.read_text(encoding='utf-8')):
            raw=raw.strip().strip('\'"')
            if not raw or raw.startswith(('data:', 'http:','https:','//','#')):continue
            uri=urlsplit(raw)
            dest=(css.parent / unquote(uri.path)).resolve()
            if not dest.is_file():errors.append((str(css.relative_to(base)),raw,'recurso CSS no encontrado'))
            else: stats['recursos_css_validos']+=1
    print('Verificación de',base)
    print('Estadísticas:',dict(stats))
    print('Tamaño del sitio: %.1f MiB'%(sum(p.stat().st_size for p in base.rglob('*') if p.is_file())/1048576))
    if errors:
        print('Errores:',len(errors))
        for p,link,err in errors[:50]:print(' -',p,'::',link,'=>',err)
        raise SystemExit(1)
    print('RESULTADO: SIN ENLACES LOCALES NI ANCLAS ROTOS')

if __name__ == '__main__':
    main()
