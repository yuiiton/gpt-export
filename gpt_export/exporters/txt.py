from pathlib import Path


def export_txt(
    messages: list[dict],
    output_file: str | Path,
) -> None:

    with open(output_file, "w", encoding="utf-8") as file:
        for message in messages:
            file.write(
                f"{message['speaker']}: "
                f"{message['text']}\n\n"
            )