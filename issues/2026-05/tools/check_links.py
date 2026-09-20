from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
errors = []
for html_path in ROOT.rglob('*.html'):
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    for tag, attr in [('img', 'src'), ('a', 'href')]:
        for node in soup.find_all(tag):
            val = node.get(attr, '')
            if not val or val.startswith(('http://', 'https://', '#', 'mailto:', 'javascript:')):
                continue
            clean = val.split('#')[0].split('?')[0]
            target = (html_path.parent / clean).resolve()
            if target.is_dir():
                target = target / 'index.html'
            if not target.exists():
                errors.append(f'{html_path.relative_to(ROOT)} -> {val}')
if errors:
    print('Broken local references:')
    print('\n'.join(errors))
    raise SystemExit(1)
print('All local references exist.')
