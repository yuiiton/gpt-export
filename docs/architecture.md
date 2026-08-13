# Arquitetura

## Visão geral

O `gpt-export` é uma aplicação de linha de comando para baixar conversas do ChatGPT e exportá-las para formatos legíveis.

O projeto foi desenvolvido com foco em simplicidade e possui um fluxo principal:

```text
CLI
 │
 ├── download
 │      │
 │      ▼
 │    Client
 │      │
python main.py download --conversation-id <conversation-id> --output conversa.json
 │  ChatGPT Backend API
 │      │
 │      ▼
 │   JSON da conversa
 │
 └── txt
        │
        ▼
   Exportador TXT
        │
        ▼
      .txt
```

A aplicação separa as responsabilidades entre interface de linha de comando, comunicação HTTP, lógica da aplicação e exportadores.

## Estrutura do projeto

```text
gpt-export/
├── gpt_export/
│   ├── __init__.py
│   │── .env
│   ├── cli.py
│   ├── client.py
│   ├── config.py
│   ├── core.py
│   └── exporters/
│       ├── __init__.py
│       └── txt.py
├── docs/
├── exports/
│   ├── json/
│   │── txt/
├── .env.example
├── .gitignore
├── main.py
└── pyproject.toml
```

## Componentes

### `main.py`

Ponto de entrada da aplicação.

Sua responsabilidade é iniciar a CLI disponibilizada pelo pacote `gpt_export`.

### `cli.py`

Responsável pela interface de linha de comando.

Cuida de:

* Definição dos comandos.
* Argumentos e opções.
* Carregamento das configurações.
* Comunicação com a camada principal da aplicação.
* Apresentação de informações e erros ao usuário.

A CLI não deve conter detalhes de implementação relacionados às requisições HTTP ou à conversão dos arquivos.

### `config.py`

Responsável pelo gerenciamento das configurações da aplicação.

As informações de autenticação são carregadas a partir das variáveis de ambiente e podem ser armazenadas em um arquivo `.env`.

Informações sensíveis não devem ser incluídas diretamente no código-fonte.

### `client.py`

Responsável pela comunicação HTTP com o backend do ChatGPT.

Atualmente, o projeto utiliza o seguinte endpoint interno:

```text
https://chatgpt.com/backend-api/conversation/{conversation_id}
```

Esse endpoint é utilizado para obter os dados de uma conversa a partir de seu identificador.

O módulo `client.py` concentra essa dependência externa para evitar que outras partes da aplicação precisem conhecer detalhes da comunicação com o backend.

### `core.py`

Contém a lógica principal das operações da aplicação.

Por exemplo, o processo de download é coordenado por essa camada:

```text
download_conversation()
        │
        ├── get_conversation()
        │
        └── salvar dados
```

A camada principal atua como intermediária entre o cliente HTTP e os demais componentes.

### `exporters/`

Contém os módulos responsáveis pela exportação das conversas para diferentes formatos.

Atualmente existe um exportador de texto:

```text
exporters/
└── txt.py
```

Novos formatos podem ser adicionados sem modificar a lógica responsável pelo download.

### exports

Contém os arquivos de conversas baixados pela CLI.

## Fluxo de download

Quando o usuário executa:

```bash
python main.py download --conversation-id <conversation-id> --output conversa.json
```

o fluxo é:

```text
Usuário
   │
   ▼
CLI
   │
   │ ID da conversa + configuração
   ▼
Core
   │
   ▼
Client
   │
   │ Requisição HTTP
   ▼
ChatGPT Backend
   │
   │ Resposta JSON
   ▼
Client
   │
   ▼
Core
   │
   ▼
Arquivo JSON
```

## Fluxo de exportação

A exportação ocorre de forma independente do download:

```bash
python main.py txt \
    --input-file conversa.json \
    --output conversa.txt
```

O fluxo é:

```text
Arquivo JSON
     │
     ▼
    CLI
     │
     ▼
    Core
     │
     ▼
Exportador TXT
     │
     ▼
Arquivo TXT
```

Essa separação permite que uma conversa seja baixada apenas uma vez e posteriormente convertida para diferentes formatos.

Nota sobre caminhos de saída

Agora os arquivos exportados são gravados em diretórios padrão para facilitar organização. Ao usar as opções de saída da CLI, passe somente o nome do arquivo (por exemplo `minha-conversa.json` ou `minha-conversa.txt`). O programa irá salvar os arquivos nos diretórios padrão, por exemplo:

- JSON: `./exports/json/{nome}`
- TXT: `./exports/txt/{nome}`

Exemplo de uso (o `--output` recebe apenas o nome; o caminho final é construído automaticamente):

```bash
python main.py download 6a283d48-7d78-83e9-9038-675f1b3d16f3 --output conversa.json
python main.py txt --input-file conversa.json --output conversa.txt
```

## Princípios arquiteturais

### Separação de responsabilidades

Cada módulo deve possuir uma responsabilidade clara.

A CLI lida com a interação com o usuário, o cliente lida com HTTP e os exportadores lidam com os formatos de saída.

### Simplicidade

O `gpt-export` é uma aplicação pessoal de linha de comando.

A arquitetura deve permanecer simples enquanto isso for suficiente para resolver o problema.

Novas abstrações ou componentes só devem ser adicionados quando resolverem uma necessidade real.

### Isolamento da API externa

A dependência do backend do ChatGPT deve permanecer concentrada no módulo `client.py`.

Isso facilita futuras alterações caso o endpoint, autenticação ou formato da resposta sejam modificados.

### Configuração externa

Credenciais e outras informações sensíveis não devem ser armazenadas no código-fonte.

A configuração é fornecida através de variáveis de ambiente.

## Risco conhecido

O principal risco arquitetural do projeto é sua dependência de uma API interna do ChatGPT.

O endpoint utilizado não é uma API pública estável e pode sofrer alterações sem aviso.

Mudanças no endpoint, autenticação, headers ou estrutura da resposta podem fazer com que o projeto deixe de funcionar.

Esse risco é conhecido e aceito como uma limitação do projeto.

## Possíveis evoluções

Algumas evoluções possíveis são:

* Adição de novos formatos de exportação.
* Testes automatizados.
* Tratamento mais detalhado de erros da API.
* Melhorias no gerenciamento das credenciais.
* Adaptação a futuras mudanças do backend do ChatGPT.
