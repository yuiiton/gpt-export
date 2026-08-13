import requests

from config import get_base_url, get_headers


BASE_URL = get_base_url()

HEADERS = get_headers()


def get_conversation(
    conversation_id: str,
    token: str,
    account_id: str,
    cookies: dict,
) -> dict:

    headers = HEADERS.copy()

    headers["Authorization"] = f"Bearer {token}"
    headers["chatgpt-account-id"] = account_id

    response = requests.get(
        f"{BASE_URL}/conversation/{conversation_id}",
        headers=headers,
        cookies=cookies,
    )

    response.raise_for_status()

    return response.json()