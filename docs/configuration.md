# Configuração

O `gpt-export` utiliza informações da sessão autenticada do ChatGPT para acessar as conversas. Essas informações são armazenadas no arquivo `.env`.

## Obtendo as credenciais

As informações necessárias podem ser obtidas através das ferramentas de desenvolvedor do navegador.

1. Acesse o ChatGPT e faça login.
2. Abra as ferramentas de desenvolvedor do navegador (`F12`).
3. Acesse a aba **Network**.
4. Recarregue a página.
5. Localize uma requisição para o backend do ChatGPT, algo semelhante à `GET /backend-api/conversation`.
6. Abra a requisição e consulte os cabeçalhos enviados.

### `GPT_TOKEN`

Na requisição, procure pelo cabeçalho:

```text
Authorization: Bearer <token>
```

Copie apenas o valor após `Bearer`.

Esse valor será utilizado como `GPT_TOKEN`.

### `GPT_ACCOUNT_ID`

O `GPT_ACCOUNT_ID` pode ser obtido nas informações de autenticação presentes na requisição ou nos dados associados à sessão.

O valor possui um formato semelhante a:

```text
c6e2c585-463e-408d-92e0-f6009a54e36e
```

### `GPT_COOKIES`

Na mesma requisição, procure pelo cabeçalho:

```text
Cookie
```

Copie o valor completo do cabeçalho.

Esse valor será utilizado como `GPT_COOKIES`.

> Os valores e a estrutura das informações de autenticação podem mudar conforme alterações no ChatGPT.

---

## Configuração utilizando o `setup`

O `gpt-export` possui um comando interativo para configurar o arquivo `.env`.

Execute:

```bash
python main.py setup
```

O comando solicitará as informações necessárias:

- `AUTHOR`
- `GPT_TOKEN`
- `GPT_ACCOUNT_ID`
- `GPT_COOKIES`

Após o preenchimento, o `setup` criará ou atualizará o arquivo `.env`.

O arquivo terá uma estrutura semelhante a:

```env
AUTHOR=Seu Nome
GPT_TOKEN=...
GPT_ACCOUNT_ID=...
GPT_COOKIES=...
```

---

## Configuração manual

Também é possível configurar o projeto manualmente.

Crie um arquivo `.env` na raiz do projeto:

```text
.env
```

Caso exista um `.env.example`, ele pode ser utilizado como base:

```bash
cp .env.example .env
```

Preencha as variáveis:

```env
AUTHOR=Seu Nome
GPT_TOKEN=seu_token
GPT_ACCOUNT_ID=seu_account_id
GPT_COOKIES=seus_cookies
```

### `AUTHOR`

Nome do autor:

```env
AUTHOR=Seu Nome
```

### `GPT_TOKEN`

Token obtido no cabeçalho `Authorization` da requisição:

```env
GPT_TOKEN=eyJ...
```

### `GPT_ACCOUNT_ID`

ID da conta obtido nas informações da sessão:

```env
GPT_ACCOUNT_ID=c6e2c585-463e-408d-92e0-f6009a54e36e
```

### `GPT_COOKIES`

Valor completo do cabeçalho `Cookie`:

```env
GPT_COOKIES=oai-did=...; oai-hlib=true; ...
```

O valor de `GPT_COOKIES` deve permanecer em uma única linha.
