"""카드뉴스 HTML을 SNS 게시용 PNG 9장(1080×1080)과 미리보기·압축파일로 내보냅니다.
실행: python tools/export_cardnews.py  (Playwright, BeautifulSoup, Pillow 필요)"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from PIL import Image
import base64, mimetypes, zipfile

PERIOD = "2026-09-10"
ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / f"cardnews/{PERIOD}/index.html"
OUT = ROOT / f"cardnews/{PERIOD}/png"
OUT.mkdir(parents=True, exist_ok=True)

soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")
for img in soup.find_all("img"):
    src = img.get("src", "")
    if not src or src.startswith(("http://", "https://", "data:")):
        continue
    p = (HTML.parent / src).resolve()
    mime = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    img["src"] = f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode("ascii")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 540, "height": 540}, device_scale_factor=2)
    page.set_content(str(soup), wait_until="load")
    page.evaluate("document.documentElement.classList.add('export-mode')")
    page.wait_for_timeout(300)
    for i in range(1, 10):
        page.evaluate("n => { document.getElementById('track').style.transform = `translateX(-${n * 100}%)`; }", i - 1)
        page.locator(".viewer").screenshot(path=str(OUT / f"card-{i:02d}.png"))
    browser.close()

cards = [OUT / f"card-{i:02d}.png" for i in range(1, 10)]
tile, gap = 360, 18
m = Image.new("RGB", (tile * 3 + gap * 4, tile * 3 + gap * 4), (24, 24, 26))
for i, c in enumerate(cards):
    m.paste(Image.open(c).convert("RGB").resize((tile, tile)), (gap + (i % 3) * (tile + gap), gap + (i // 3) * (tile + gap)))
m.save(OUT / "cardnews-montage.png")
with zipfile.ZipFile(OUT / f"cardnews-{PERIOD}.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for c in cards:
        z.write(c, c.name)
print(f"Exported 9 cards, montage, zip to {OUT}")
