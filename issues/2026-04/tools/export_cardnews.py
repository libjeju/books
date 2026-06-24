from pathlib import Path
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import base64
import mimetypes

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "cardnews/2026-07-08/index.html"
OUT = ROOT / "cardnews/2026-07-08/png"
OUT.mkdir(parents=True, exist_ok=True)

soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")
for img in soup.find_all("img"):
    src = img.get("src", "")
    if not src or src.startswith(("http://", "https://", "data:")):
        continue
    p = (HTML.parent / src).resolve()
    mime = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    img["src"] = f"data:{mime};base64,{data}"
html_text = str(soup)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 540, "height": 540}, device_scale_factor=2)
    page.set_content(html_text, wait_until="load")
    page.evaluate("document.documentElement.classList.add('export-mode')")
    for i in range(1, 10):
        page.evaluate("n => { document.getElementById('track').style.transform = `translateX(-${n * 100}%)`; }", i - 1)
        page.locator(".viewer").screenshot(path=str(OUT / f"card-{i:02d}.png"))
    browser.close()

print(f"Exported 9 cards to {OUT}")
