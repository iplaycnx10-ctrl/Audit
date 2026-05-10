import json
from pathlib import Path


def load_json(path, default=None):
    path = Path(path)
    if not path.exists():
        return default if default is not None else []

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default if default is not None else []


def save_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
