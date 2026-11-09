#!/usr/bin/env python
"""Generate the Simplified-Chinese deck (index.zh.html) from the English source
(index.html) plus a committed translation catalog (translations.zh.json).

English index.html is the single source of truth. To keep the two decks in sync:

  1. Edit index.html (English) as usual.
  2. Run:  python build_zh.py apply
     Every on-slide text element is looked up in translations.zh.json by its exact
     English inner-HTML. Matches are replaced with the Chinese; anything new or
     changed is left in English and printed under "UNTRANSLATED".
  3. Translate each UNTRANSLATED string, add "<english>": "<chinese>" to
     translations.zh.json (keep any inline tags/hrefs, numbers and proper names),
     and re-run  python build_zh.py apply.

`extract` dumps every translatable string to .zh_todo.json (for a bulk first pass);
`catalog` merges .zh_todo.json + .zh_translations.json into translations.zh.json.
Run from anywhere - paths resolve relative to this script.
"""
import sys, io, json, os
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, 'index.html')
OUT = os.path.join(BASE, 'index.zh.html')
CATALOG = os.path.join(BASE, 'translations.zh.json')
TODO = os.path.join(BASE, '.zh_todo.json')
TRANS = os.path.join(BASE, '.zh_translations.json')

INLINE = {'span', 'b', 'em', 'a', 'i', 'strong', 'sup', 'sub', 'br', 'u', 'small'}
SKIP_ANCESTORS = {'script', 'style', 'svg'}

def has_alpha(t):
    return any(c.isalpha() and ord(c) < 128 for c in t)

def is_target(tag):
    if tag.name in ('script', 'style', 'svg'):
        return False
    for anc in tag.parents:
        if anc.name in SKIP_ANCESTORS:
            return False
    if tag.name in INLINE:
        return False
    for c in tag.find_all(recursive=False):
        if c.name not in INLINE:
            return False
    return has_alpha(tag.get_text())

def targets(soup):
    return [t for t in soup.find_all(True) if is_target(t)]

def load_src():
    return BeautifulSoup(io.open(SRC, encoding='utf-8').read(), 'html.parser')

def extract():
    soup = load_src()
    strings = [t.decode_contents() for t in targets(soup)]
    title = soup.find('title')
    desc = soup.find('meta', attrs={'name': 'description'})
    extra = []
    if title:
        extra.append(title.decode_contents())
    if desc:
        extra.append(desc.get('content', ''))
    io.open(TODO, 'w', encoding='utf-8').write(json.dumps({'strings': strings, 'extra': extra}, ensure_ascii=False, indent=1))
    print('extracted', len(strings), 'block strings +', len(extra), 'meta ->', TODO)

def catalog():
    todo = json.loads(io.open(TODO, encoding='utf-8').read())
    tr = json.loads(io.open(TRANS, encoding='utf-8').read())
    assert len(todo['strings']) == len(tr['strings']), 'length mismatch %d vs %d' % (len(todo['strings']), len(tr['strings']))
    d = {en: zh for en, zh in zip(todo['strings'], tr['strings'])}
    extra = {en: zh for en, zh in zip(todo.get('extra', []), tr.get('extra', []))}
    io.open(CATALOG, 'w', encoding='utf-8', newline='').write(json.dumps({'strings': d, 'extra': extra}, ensure_ascii=False, indent=1))
    print('catalog written:', len(d), 'unique en->zh entries')

def apply():
    cat = json.loads(io.open(CATALOG, encoding='utf-8').read())
    d = cat['strings']
    extra = cat.get('extra', {})
    soup = load_src()
    missing = []
    for tag in targets(soup):
        en = tag.decode_contents()
        if en in d:
            tag.clear()
            for c in list(BeautifulSoup(d[en], 'html.parser').contents):
                tag.append(c)
        elif en.strip():
            missing.append(en)
    title = soup.find('title')
    desc = soup.find('meta', attrs={'name': 'description'})
    if title and title.decode_contents() in extra:
        title.string = extra[title.decode_contents()]
    if desc and desc.get('content', '') in extra:
        desc['content'] = extra[desc['content']]
    ht = soup.find('html')
    if ht:
        ht['lang'] = 'zh-CN'
    head = soup.find('head')
    head.append(soup.new_tag('link', rel='stylesheet',
                             href='https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;800;900&display=swap'))
    ov = soup.new_tag('style')
    ov.string = ".reveal, .reveal h1, .reveal h2, .reveal h3, .reveal p, .reveal .kicker, .reveal .tile, .reveal .card, .reveal .sub { font-family: 'Noto Sans SC','Inter',system-ui,-apple-system,sans-serif; }"
    head.append(ov)
    io.open(OUT, 'w', encoding='utf-8', newline='').write(str(soup))
    print('wrote', OUT)
    if missing:
        print('UNTRANSLATED (%d) - add these to translations.zh.json, then re-run apply:' % len(missing))
        for m in missing:
            print('   ', repr(m[:90]))
    else:
        print('all target strings translated')

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'apply'
    {'extract': extract, 'catalog': catalog, 'apply': apply}[mode]()
