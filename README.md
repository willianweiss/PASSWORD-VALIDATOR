# PASSWORD-VALIDATOR

## Descrição

Este projeto é uma API web simples que verifica se uma senha é válida de acordo com determinadas regras. Ele é construído com Python e FastAPI.

## Regras de validação de senha

Uma senha é considerada válida se:

- Possui nove ou mais caracteres
- Possui pelo menos um dígito
- Possui pelo menos uma letra minúscula
- Possui pelo menos uma letra maiúscula
- Possui pelo menos um caractere especial (!@#$%^&*()-+)
- Não possui caracteres repetidos dentro do conjunto

## Como rodar o projeto

### Com Docker

1.  Execute o contêiner Docker:

`docker-compose up`

2.  Rebuildar o contêiner Docker:

`docker-compose up --build`

A API agora estará disponível em `http://localhost:80/docs`.

### Sem Docker

1.  Crie um ambiente virtual:

`python -m venv venv`

2.  Ative o ambiente virtual:

`source venv/bin/activate`

3.  Instale as dependências:

`pip install -r requirements.txt` 

4.  Execute o servidor:

`uvicorn app.main:app --host 0.0.0.0 --port 80` 

A API agora estará disponível em `http://localhost:80/docs`.

## Como usar a API

A API possui um único endpoint, `POST /validate-password`, que aceita uma senha em um campo de formulário e retorna um booleano indicando se a senha é válida.

Por exemplo:

`curl -d "password=AbTp9!fok" -X POST http://localhost:80/validate-password` 

## Testes

Os testes podem ser executados com pytest:

`pytest`

## Linter

O linter utilizado é o black e isort. Para executá-lo, basta rodar:

`black .`

`isort .`