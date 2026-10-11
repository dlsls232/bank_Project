import json
from pathlib import Path
from typing import Any


def read_json_file(file_path: str | Path) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей с данными."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError, json.JSONDecodeError:
        return []

    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return data

    return []
