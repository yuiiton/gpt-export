# Configuração

Este documento descreve como obter as credenciais necessárias para utilizar o `gpt-export` e como configurar o projeto.

## Obtendo as credenciais

As informações necessárias podem ser obtidas através das ferramentas de desenvolvedor do navegador.

1. Acesse o ChatGPT e faça login.
2. Abra as ferramentas de desenvolvedor do navegador (`F12`).
3. Acesse a aba **Network**.
4. Recarregue a página.
5. Localize uma requisição para o domínio `chatgpt.com`.
6. Procure uma requisição relacionada ao carregamento de uma conversa, semelhante a ´´conversation/<conversation-id></conversation>´´

### `GPT_TOKEN`

Na requisição, procure pelo cabeçalho:

```text
Authorization: Bearer <token>
```

O valor utilizado em `GPT_TOKEN` é o token depois de `Bearer`.

Por exemplo:

```env
GPT_TOKEN=eyJ...
```

### `GPT_ACCOUNT_ID`

O `GPT_ACCOUNT_ID` corresponde ao ID da conta utilizada na sessão do ChatGPT.

Ele possui um formato semelhante a:

```text
c6e2c585-463e-408d-92e0-f6009a54e36e
```

### `GPT_COOKIES`

Na mesma requisição, procure pelo cabeçalho:

```text
Cookie
```

Copie o valor completo desse cabeçalho.

Esse valor será utilizado como `GPT_COOKIES`.

> Dependendo do navegador e da versão do ChatGPT, as informações presentes na requisição podem variar.

---

## Configuração utilizando o `setup`

O `gpt-export` possui um comando interativo para facilitar a configuração inicial.

Com o ambiente virtual ativado, execute:

```bash
python main.py setup
```

O programa solicitará as informações necessárias e criará ou atualizará o arquivo `.env` automaticamente.

Ao final, o arquivo deverá possuir uma estrutura semelhante a:

```env
AUTHOR=Seu Nome
GPT_TOKEN=...
GPT_ACCOUNT_ID=...
GPT_COOKIES=...
```

Os valores de `GPT_TOKEN`, `GPT_ACCOUNT_ID` e `GPT_COOKIES` devem ser obtidos conforme descrito na seção [Obtendo as credenciais](#obtendo-as-credenciais).

---

## Configuração manual

Também é possível configurar o projeto manualmente através do arquivo `.env`.

Na raiz do projeto, crie um arquivo chamado:

```text
.env
```

Caso exista um arquivo `.env.example`, ele pode ser utilizado como base:

```bash
cp .env.example .env
```

Depois, preencha as variáveis necessárias:

```env
AUTHOR=Seu Nome
GPT_TOKEN=seu_token
GPT_ACCOUNT_ID=seu_account_id
GPT_COOKIES=seus_cookies
```

### `AUTHOR`

Nome do autor utilizado pelo projeto:

```env
AUTHOR=Seu Nome
```

### `GPT_TOKEN`

Token de autenticação obtido conforme descrito na seção [Obtendo as credenciais](#obtendo-as-credenciais):

```env
GPT_TOKEN=eyJ...
```

### `GPT_ACCOUNT_ID`

ID da conta utilizada na sessão do ChatGPT:

```env
GPT_ACCOUNT_ID=c6e2c585-463e-408d-92e0-f6009a54e36e
```

### `GPT_COOKIES`

Cookies da sessão autenticada:

```env
GPT_COOKIES=oai-did=...; oai-hlib=true; ...
```

> O valor de `GPT_COOKIES` deve ser mantido em uma única linha.

---

## Testando a configuração

Depois de configurar o arquivo `.env`, utilize uma conversa para testar a autenticação:

```bash
# Observe: o `--output` aceita apenas o nome do arquivo. O programa salva o JSON no diretório padrão de JSONs.
python main.py download --conversation-id <conversation-id> --output teste.json
```

Se as credenciais estiverem válidas, a conversa será salva no diretório padrão (por exemplo `./exports/json/`) com o nome indicado.

Por exemplo:

```bash
python main.py download 6a283d48-7d78-83e9-9038-675f1b3d16f3 --output teste.json
```

---

## Segurança

As variáveis `GPT_TOKEN`, `GPT_ACCOUNT_ID` e `GPT_COOKIES` contêm informações relacionadas à autenticação da sessão.

**Nunca:**

- publique o arquivo `.env`;
- compartilhe suas credenciais;
- coloque credenciais diretamente no código;
- adicione o `.env` ao Git;
- inclua credenciais reais em exemplos ou screenshots.

Certifique-se de que o arquivo `.env` esteja presente no `.gitignore`:

```gitignore
.env
```

Caso alguma credencial seja exposta, encerre ou invalide a sessão correspondente e obtenha novas credenciais.

> O `gpt-export` utiliza endpoints internos do ChatGPT. Esses endpoints não constituem uma API pública estável e podem sofrer alterações que façam com que o projeto deixe de funcionar ou exija mudanças futuras.
