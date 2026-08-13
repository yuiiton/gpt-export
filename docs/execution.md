# Execução do projeto

Este documento mostra como o projeto é executado na prática.

O fluxo do `gpt-export` é simples:

1. preparar o ambiente Python;
2. configurar o arquivo `.env` com as credenciais;
3. baixar uma conversa com o comando `download`;
4. converter o JSON resultante para TXT com o comando `txt`.

---

## 1. Pré-requisitos

Antes de rodar o projeto, certifique-se de que você tenha:

- Python 3.13 ou superior;
- acesso ao ChatGPT em uma sessão autenticada;
- as credenciais necessárias armazenadas em `.env`.

> Se você ainda não configurou as credenciais, leia primeiro [configuration.md](configuration.md). Esse arquivo explica como obter `GPT_TOKEN`, `GPT_ACCOUNT_ID` e `GPT_COOKIES`.

---

## 2. Instalar as dependências

Na raiz do projeto, crie um ambiente virtual e instale as dependências:

```bash
cd gpt-export
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Depois disso, o comando `gpt-export` estará disponível no terminal.

---

## 3. Configurar o projeto

O ponto de entrada da aplicação é o comando:

```bash
gpt-export setup
```

Esse comando pede os dados visíveis na sessão do usuário e salva as informações em um arquivo `.env` na raiz do projeto.

A estrutura esperada é semelhante a:

```env
AUTHOR=Seu Nome
GPT_TOKEN=...
GPT_ACCOUNT_ID=...
GPT_COOKIES=...
```

Se preferir, você pode criar o arquivo manualmente. O processo completo está em [configuration.md](configuration.md).

---

## 4. Verificar os comandos disponíveis

Para visualizar a CLI e os comandos disponíveis, execute:

```bash
gpt-export --help
```

Você deve ver comandos como:

- `setup`
- `download`
- `txt`

---

## 5. Baixar uma conversa

O comando principal para obter uma conversa do ChatGPT é:

```bash
gpt-export download --conversation-id <conversation-id> --output conversa.json
```

### Como funciona

- `--conversation-id` recebe o identificador da conversa;
- `--output` recebe apenas o nome do arquivo;
- o programa salva automaticamente em `./exports/json/`.

Exemplo:

```bash
gpt-export download --conversation-id 6a283d48-7d78-83e9-9038-675f1b3d16f3 --output teste.json
```

O arquivo gerado ficará em algo como:

```text
./exports/json/teste.json
```

Essa etapa é o download bruto da conversa em JSON. Em outras palavras, ela pega o conteúdo da sessão do ChatGPT e salva localmente para que você possa processar a informação depois.

---

## 6. Converter o JSON para TXT

Depois de baixar a conversa, você pode exportá-la para um texto legível:

```bash
gpt-export txt --input-file conversa.json --output conversa.txt
```

### Como funciona

- `--input-file` aponta para o nome do arquivo JSON dentro de `./exports/json/`;
- `--output` recebe apenas o nome do arquivo TXT;
- o programa salva automaticamente em `./exports/txt/`.

Exemplo:

```bash
gpt-export txt --input-file teste.json --output teste.txt
```

O resultado ficará em:

```text
./exports/txt/teste.txt
```

Esse arquivo é útil para buscas locais, arquivamento e leitura mais simples em editores ou terminal.

---

## 7. Fluxo completo de uso

Um fluxo típico do projeto é este:

```bash
gpt-export setup

gpt-export download --conversation-id <conversation-id> --output minha-conversa.json

gpt-export txt --input-file minha-conversa.json --output minha-conversa.txt
```

### Observações importantes

- os comandos `--output` e `--input-file` recebem apenas nomes de arquivo, não caminhos completos;
- os diretórios de saída são gerenciados automaticamente pela aplicação;
- a parte de autenticação e obtenção de credenciais está detalhada em [configuration.md](configuration.md);
- a parte de arquitetura do projeto está em [architecture.md](architecture.md).

---

## 8. Onde os arquivos são salvos

A aplicação organiza a saída em pastas padrão:

```text
./exports/json/
./exports/txt/
```

Assim, um fluxo normal gera algo como:

```text
exports/
├── json/
│   └── minha-conversa.json
└── txt/
    └── minha-conversa.txt
```

---

## 9. Quando usar cada comando

### `setup`

Use quando estiver configurando o projeto pela primeira vez ou quando precisar atualizar as credenciais.

### `download`

Use quando quiser pegar uma conversa específica do ChatGPT e salvar como JSON local.

### `txt`

Use quando quiser transformar o JSON em um texto legível para consulta, busca ou arquivamento.

---

## 10. Segurança

As credenciais do projeto são sensíveis e devem ficar apenas no arquivo `.env`.

Nunca:

- compartilhe o `.env` publicamente;
- adicione credenciais em código-fonte;
- publique screenshots com tokens ou cookies reais.

Se precisar revisar a parte de configuração em detalhes, consulte [configuration.md](configuration.md).
