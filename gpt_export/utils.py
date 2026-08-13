import json
from pathlib import Path


def load_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(
    data: dict,
    file_path: str | Path,
) -> None:

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )


def parse_cookie_string(cookie_string: str) -> dict:
    cookies = {}

    for item in cookie_string.split(";"):
        item = item.strip()

        if "=" not in item:
            continue

        key, value = item.split("=", 1)

        cookies[key] = value

    return cookies