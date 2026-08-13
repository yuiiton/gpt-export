from config import get_author

def build_message_chain(data: dict) -> list[dict]:
    mapping = data["mapping"]
    current_id = data["current_node"]

    chain = []

    while current_id:
        chain.append(current_id)
        current_id = mapping[current_id].get("parent")

    chain.reverse()

    return [
        mapping[node_id]
        for node_id in chain
    ]


def extract_text(message: dict) -> str:
    content = message.get("content", {})
    parts = content.get("parts", [])

    texts = []

    for part in parts:
        if isinstance(part, str):
            texts.append(part)

    return "\n".join(texts).strip()


def parse_message(node: dict) -> dict | None:
    message = node.get("message")

    if not message:
        return None

    role = message.get("author", {}).get("role")

    if role not in ("user", "assistant"):
        return None

    text = extract_text(message)

    if not text:
        return None

    speaker = {
        "user": get_author(),
        "assistant": "ChatGPT",
    }[role]

    return {
        "speaker": speaker,
        "text": text,
    }


def parse_conversation(data: dict) -> list[dict]:
    nodes = build_message_chain(data)

    messages = []

    for node in nodes:
        message = parse_message(node)

        if message:
            messages.append(message)

    return messages