# Livros API

Este projeto é uma API RESTful desenvolvida em Python utilizando o framework Django e Django Ninja para o gerenciamento de livros. Ela permite criar, visualizar, atualizar e deletar livros, bem como realizar avaliações e sortear livros com base em filtros.
Esta API foi desenvolvida para fins de estudo e prática com Django e Django Ninja. Ela fornece uma base para o gerenciamento de dados e práticas RESTful e pode ser expandida com novos recursos e validações conforme necessário.

## Tecnologias Utilizadas

- Python 3.x
- Django 5.x
- Django Ninja
- SQLite (como banco de dados)

## Estrutura do Projeto

- **`manage.py`**: Script de gerenciamento do Django.
- **`livro/`**: Diretório principal do aplicativo, contendo os seguintes módulos:
  - **`api.py`**: Define as rotas e endpoints para o gerenciamento de livros e avaliações.
  - **`apps.py`**: Configurações do aplicativo `livros`.
  - **`models.py`**: Define os modelos `Livros` e `Categorias` usados no banco de dados.
  - **`schemas.py`**: Esquemas para a validação de dados com Django Ninja.
  - **`migrations/`**: Arquivos de migração para criação e modificação das tabelas no banco de dados.

## Endpoints da API

Abaixo, estão descritos os principais endpoints disponíveis.

### Livros

- **GET `/livros/`**: Retorna uma lista de todos os livros cadastrados.
- - **GET `/livros/id`**: Retorna o livro correspondente ao id informado.
- **POST `/livros/`**: Cria um novo livro com os dados fornecidos no corpo da requisição.
  - Campos obrigatórios: `nome`, `streaming`, `categorias`
  - Streaming deve ser `"F"` (Físico) ou `"AK"` (Amazon Kindle).
- **PUT `/livros/{livro_id}`**: Avalia um livro existente com `nota` e `comentarios`.
  - Nota deve estar entre 0 e 5.
- **DELETE `/livros/{livro_id}`**: Deleta um livro com base no ID.

### Sorteio de Livros

- **GET `/livros/sortear/`**: Retorna um livro aleatório, com filtros opcionais como `nota_minima`, `categorias`, e `reler`.

## Modelos

- **Livros**: Armazena informações sobre os livros, incluindo nome, streaming (tipo de formato), nota e comentários.
- **Categorias**: Lista de categorias associadas aos livros.

## Instalação e Configuração

### Pré-requisitos

- Python 3.x
- Virtualenv (recomendado)

### Passos

1. Clone o repositório:

   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>

2. Criar e ativar ambiente virtual

   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
   
3. Instale as dependências
     ```bash
     pip install -r requirements.txt

4. Execute as migrações para o banco
    ```bash
    python manage.py migrate
    
5. Inicie o servidor
   ```bash
   python manage.py runserver

