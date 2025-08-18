import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "db.json"

def load_data():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
