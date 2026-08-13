from client import get_conversation
from exporters.txt import export_txt
from parser import parse_conversation
from utils import load_json, save_json
from config import JSON_ARCHIVES_DIR, TEXT_ARCHIVES_DIR


def download_conversation(
    conversation_id: str,
    token: str,
    account_id: str,
    cookies: dict,
    output_file: str,
) -> None:

    data = get_conversation(
        conversation_id=conversation_id,
        token=token,
        account_id=account_id,
        cookies=cookies,
    )

    output_path = JSON_ARCHIVES_DIR / output_file

    if output_path.suffix != ".json":
        output_path = output_path.with_suffix(".json")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    save_json(
        data=data,
        file_path=output_path,
    )

def convert_to_txt(
    input_file: str,
    output_file: str,
) -> None:

    data = load_json(input_file)

    messages = parse_conversation(data)

    output_path = TEXT_ARCHIVES_DIR / output_file

    if output_path.suffix != ".txt":
        output_path = output_path.with_suffix(".txt")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    export_txt(
        messages=messages,
        output_file=output_path,
    )