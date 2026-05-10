import json
from pathlib import Path


ASSETS_FILE = Path("data/portfolio_assets.json")


def load_assets():
    if not ASSETS_FILE.exists():
        return []
    try:
        return json.loads(ASSETS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def save_assets(assets):
    ASSETS_FILE.parent.mkdir(parents=True, exist_ok=True)
    ASSETS_FILE.write_text(json.dumps(assets, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_drive_image_url(url):
    url = str(url or "").strip()
    if "drive.google.com" not in url:
        return url
    if "/file/d/" in url:
        file_id = url.split("/file/d/")[1].split("/")[0]
        return f"https://drive.google.com/uc?export=view&id={file_id}"
    if "id=" in url:
        file_id = url.split("id=")[1].split("&")[0]
        return f"https://drive.google.com/uc?export=view&id={file_id}"
    return url


def add_asset(title, url, note=""):
    assets = load_assets()
    image_url = normalize_drive_image_url(url)
    assets.append({"title": title.strip() or "Portfolio Asset", "url": image_url, "note": note.strip()})
    save_assets(assets)
    return assets


def clear_assets():
    save_assets([])
