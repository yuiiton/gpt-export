import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

ARCHIVES_DIR = BASE_DIR / "exports"
JSON_ARCHIVES_DIR = ARCHIVES_DIR / "json"
TEXT_ARCHIVES_DIR = ARCHIVES_DIR / "txt"


load_dotenv(ENV_FILE)


def get_base_url() -> str:
    return "https://chatgpt.com/backend-api"


def get_headers() -> dict:
    return {
        "Accept": "*/*",
        "oai-client-build-number": "8721732",
        "oai-client-version": (
            "prod-09fba346c30685f17ce7156ae17baf81ca7d2521"
        ),
        "oai-language": "pt-BR",
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/148.0.0.0 Safari/537.36"
        ),
    }


def save_config(
    author: str,
    token: str,
    account_id: str,
    cookie: str,
) -> None:

    content = f"""AUTHOR={author}
GPT_TOKEN={token}
GPT_ACCOUNT_ID={account_id}
GPT_COOKIES={cookie}
"""

    ENV_FILE.write_text(content, encoding="utf-8")


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"A variável {name} não está configurada. "
            "Execute 'gpt-export setup'."
        )

    return value


def get_token() -> str:
    return get_required_env("GPT_TOKEN")


def get_account_id() -> str:
    return get_required_env("GPT_ACCOUNT_ID")


def get_cookies() -> str:
    return get_required_env("GPT_COOKIES")


def get_author() -> str:
    return get_required_env("AUTHOR")