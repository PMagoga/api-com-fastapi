# API utilizando FastAPI

## 🚀 Sobre o projeto

Esta é uma API desenvolvida utilizando **FastAPI**, com suporte a banco de dados através do **SQLAlchemy**, autenticação utilizando **JWT** e gerenciamento de configurações através de variáveis de ambiente.

---

## 📋 Pré-requisitos

Caso você não esteja utilizando uma IDE (Ambiente de Desenvolvimento Integrado), como **Visual Studio** ou **PyCharm**, é recomendado criar um **ambiente virtual Python**.

O ambiente virtual permite instalar as dependências isoladamente para cada projeto, evitando conflitos entre bibliotecas.

---

## 🐍 Criando o ambiente virtual

Execute o seguinte comando no terminal:

```bash
python -m venv .venv
```

### Ativando o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

---

## 📦 Instalação das dependências

Instale as principais dependências do projeto:

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
```

### Principais bibliotecas

| Biblioteca           | Descrição                                                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FastAPI**          | Framework web principal utilizado para construir a API. Gerencia as rotas, valida automaticamente os dados de entrada e saída utilizando Pydantic e disponibiliza documentação interativa através do Swagger UI. |
| **Uvicorn**          | Servidor ASGI de alta performance responsável por executar a aplicação FastAPI e atender às requisições HTTP.                                                                                                    |
| **SQLAlchemy**       | ORM (Object-Relational Mapper) utilizado para interagir com bancos de dados como PostgreSQL, MySQL e SQLite utilizando objetos Python em vez de consultas SQL diretamente.                                       |
| **Passlib + bcrypt** | Biblioteca utilizada para gerenciamento seguro de senhas, permitindo criar hashes e verificar credenciais sem armazenar as senhas em texto puro.                                                                 |
| **python-jose**      | Biblioteca utilizada para criação, assinatura e validação de tokens JWT (JSON Web Tokens), utilizados na autenticação e autorização de usuários.                                                                 |
| **python-dotenv**    | Permite carregar variáveis de ambiente a partir de um arquivo `.env`, facilitando o gerenciamento de informações sensíveis, como chaves secretas e credenciais de banco de dados.                                |
| **python-multipart** | Parser utilizado pelo FastAPI para processar formulários HTML e uploads de arquivos (`form` e `file`).                                                                                                           |

---

## 📄 Criando o `requirements.txt`

Após instalar todas as dependências, gere o arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Esse arquivo permite registrar as versões das bibliotecas utilizadas pelo projeto.

---

## 📥 Instalando as dependências de um projeto clonado

Caso o projeto tenha sido obtido através de um clone do GitHub, instale todas as dependências utilizando:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a aplicação

Para iniciar a API em modo de desenvolvimento, execute:

```bash
uvicorn main:app --reload
```

A opção `--reload` faz com que o servidor seja reiniciado automaticamente quando alterações forem detectadas no código.

Após iniciar a aplicação, a documentação interativa do FastAPI poderá ser acessada normalmente em:

```text
http://127.0.0.1:8000/docs
```

---

# 🗄️ Banco de dados

Para trabalhar com banco de dados, pode-se utilizar o **SQLAlchemy**.

Para controlar a criação e alteração da estrutura do banco de dados, recomenda-se utilizar o **Alembic**, ferramenta de migração compatível com SQLAlchemy.

---

## ⚙️ Configurando o Alembic

Inicialize o Alembic no projeto:

```bash
alembic init alembic
```

Esse comando criará a estrutura necessária para trabalhar com as migrações.

---

## 🔧 Configurando o banco de dados

No arquivo:

```text
alembic.ini
```

configure a URL de conexão com o banco de dados.

Para utilizar SQLite:

```ini
sqlalchemy.url = sqlite:///banco.db
```

---

## 🔗 Configurando o `env.py`

No arquivo:

```text
alembic/env.py
```

é possível importar os modelos da aplicação para que o Alembic consiga identificar as tabelas existentes.

Adicione:

```python
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from models import Base

target_metadata = Base.metadata
```

### 💡 O que isso faz?

O código adiciona a pasta principal do projeto ao caminho de importação do Python, permitindo importar os modelos definidos na aplicação.

O trecho:

```python
target_metadata = Base.metadata
```

informa ao Alembic quais são os metadados dos modelos que devem ser utilizados para gerar as migrações.

---

# 🏗️ Criando as migrações

Depois de configurar os modelos e o Alembic, crie uma migration inicial:

```bash
alembic revision --autogenerate -m "initial migration"
```

O parâmetro:

```text
--autogenerate
```

faz com que o Alembic compare os modelos SQLAlchemy com a estrutura atual do banco de dados e gere automaticamente as alterações necessárias.

---

## ⬆️ Aplicando as migrações

Para aplicar a migration ao banco de dados:

```bash
alembic upgrade head
```

O comando `upgrade head` aplica todas as migrações pendentes até chegar à versão mais recente.

---
#### Utilizar segurança das rotas por meio de tokens JWT
---

# 📁 Estrutura sugerida do projeto

Uma estrutura possível para organizar a aplicação:

```text
projeto/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── .venv/
│
├── .env
├── alembic.ini
├── database.py
├── models.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔄 Fluxo básico

O fluxo de desenvolvimento pode ser resumido da seguinte maneira:

```text
Criar ambiente virtual
        ↓
Instalar dependências
        ↓
Criar aplicação FastAPI
        ↓
Configurar SQLAlchemy
        ↓
Configurar Alembic
        ↓
Criar modelos
        ↓
Gerar migration
        ↓
Aplicar migration
        ↓
Executar API
        ↓
Testar através do Swagger
```

---

## 🧪 Documentação da API

O FastAPI gera automaticamente uma documentação interativa utilizando **Swagger UI**.

Depois de executar:

```bash
uvicorn main:app --reload
```

acesse:

```text
http://127.0.0.1:8000/docs
```

Também é possível acessar a documentação no formato **ReDoc**:

```text
http://127.0.0.1:8000/redoc
```

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* ⚡ FastAPI
* 🚀 Uvicorn
* 🗄️ SQLAlchemy
* 🔄 Alembic
* 🔐 JWT
* 🔑 Passlib / bcrypt
* ⚙️ python-dotenv
* 📦 python-multipart
* 🗃️ SQLite / PostgreSQL / MySQL

---

## 📌 Observação

Não versionar informações sensíveis no GitHub. Arquivos como `.env` devem ser adicionados ao `.gitignore`.

Exemplo:

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

---

## 📚 Resumo dos principais comandos

```bash
# Criar ambiente virtual
python -m venv .venv

# Instalar dependências
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

# Gerar requirements.txt
pip freeze > requirements.txt

# Instalar requirements
pip install -r requirements.txt

# Iniciar API
uvicorn main:app --reload

# Inicializar Alembic
alembic init alembic

# Criar migration
alembic revision --autogenerate -m "initial migration"

# Aplicar migrations
alembic upgrade head
```

---

## 🎯 Resultado

Com essa estrutura, você terá uma base para desenvolver uma **API REST em Python utilizando FastAPI**, com:

* gerenciamento de dependências;
* ambiente virtual;
* banco de dados;
* ORM com SQLAlchemy;
* migrations com Alembic;
* autenticação com JWT;
* armazenamento seguro de senhas;
* variáveis de ambiente;
* documentação automática com Swagger UI e ReDoc.
