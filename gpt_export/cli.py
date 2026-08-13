from pathlib import Path

import typer

from .config import get_account_id, get_cookies, get_token
from .core import convert_to_txt, download_conversation
from .utils import parse_cookie_string
from .config import save_config, ENV_FILE, JSON_ARCHIVES_DIR, TEXT_ARCHIVES_DIR


app = typer.Typer()

@app.command()
def setup():
    """Configura as credenciais do GPT Export."""

    if ENV_FILE.exists():
        overwrite = typer.confirm(
        "Já existe uma configuração. Deseja sobrescrevê-la?"
    )
        if not overwrite:
            typer.echo("Setup cancelado.")
            raise typer.Exit()

    typer.echo("=== GPT Export Setup ===\n")

    author = typer.prompt("Digite seu nome")

    token = typer.prompt(
        "Digite seu token",
        hide_input=True,
    )

    account_id = typer.prompt(
        "Digite seu Account ID",
    )

    cookie = typer.prompt(
        "Cole seu cookie",
        hide_input=True,
    )

    save_config(
        author=author,
        token=token,
        account_id=account_id,
        cookie=cookie,
    )

    typer.echo("\nConfiguração salva em .env!")
    typer.echo("\nVocê já pode usar:")
    typer.echo("  gpt-export download --conversation-id <conversation-id> --output conversa.json")
    typer.echo("  gpt-export txt --input-file conversa.json --output conversa.txt")

@app.command()
def download(
    conversation_id: str = typer.Option(
        help="Id da conversa que deseja baixar"
    ),
    output: str = typer.Option(
        "conversa.json",
        "-o",
        "--output",
        help="Nome do arquivo de saída (será salvo em ./exports/json/)",
    ),
):
    """Baixa uma conversa do ChatGPT."""

    token = get_token()
    account_id = get_account_id()
    cookie_string = get_cookies()

    cookies = parse_cookie_string(cookie_string)

    download_conversation(
        conversation_id=conversation_id,
        token=token,
        account_id=account_id,
        cookies=cookies,
        output_file=output,
    )

    final_path = JSON_ARCHIVES_DIR / output
    typer.echo(f"Conversa salva em {final_path}")

@app.command()
def txt(
    input_file: str = typer.Option(
        "conversa.json",
        "-i",
        "--input-file",
        help="Nome do arquivo JSON de entrada (procura em ./exports/json/)",
    ),
    output: str = typer.Option(
        "conversa.txt",
        "-o",
        "--output",
        help="Nome do arquivo de saída TXT (será salvo em ./exports/txt/)",
    ),
):
    """Converte uma conversa JSON para TXT."""

    in_path = JSON_ARCHIVES_DIR / input_file

    convert_to_txt(
        input_file=str(in_path),
        output_file=output,
    )

    final_out = TEXT_ARCHIVES_DIR / output
    typer.echo(f"Arquivo salvo em {final_out}")