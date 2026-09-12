### api utilizando fastapi

Caso não estiver usando um IDE (ambiente de desenvolvimento integrado), por exemplo Visual Studio ou pycharm você 
pode criar um ambiente virtual, para instalar as dependências apenas para seu projeto.
#### crie o ambiente virtual python
python -m venv .venv

#### instale as dependências
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

* fastapi -> é o framework web principal utilizado para construir a api. ele gerencia as rotas, valida os dados de 
entrada/saída automaticamente (usando pydantic) e gera a documentação interativa (swagger ui).

* uvicorn -> é o servidor asgi (asynchronous server gateway interface) de alta performance que roda a sua aplicação 
fastapi e atende às requisições http.

* sqlalchemy -> é o orm (object-relational mapper) utilizado para interagir com o banco de dados (como postgresql, 
mysql ou sqlite) usando objetos python em vez de escrever consultas sql puras.

* passlib[bcrypt] -> biblioteca para gerenciamento de senhas. a opção [bcrypt] inclui o algoritmo de criptografia 
seguro bcrypt, usado para criar hashes de senhas e verificar o login sem armazenar senhas em texto puro.

* python-jose[cryptography] -> biblioteca para criação, assinatura e verificação de tokens jwt (json web tokens), 
utilizados para autenticação e autorização de usuários.

* python-dotenv -> carrega variáveis de ambiente a partir de um arquivo .env para o projeto, permitindo esconder 
informações sensíveis (como chaves secretas e credenciais de banco de dados).

* python-multipart -> parser necessário para que o fastapi consiga processar formulários html e uploads de arquivos 
(form e file).

#### Após instalar as dependências, crie um arquivo com os requirements
pip freeze > requirements.txt

#### caso tenha feito um clone do projeto, instale as dependências
pip install -r requirements.txt

#### para rodar o app, executar no terminal
uvicorn main:app --reload

#### para usar banco de dados, pode se usar a biblioteca sqlalchemy, para fazer as migrations, pode-se usar a biblioteca alembic
alembic init alembic

#### no arquivo alembic.ini direcionar onde estará o banco de dados
sqlalchemy.url = sqlite:///banco.db

#### criar as tabelas do banco de dados
alembic revision --autogenerate -m "initial migration"

#### criar as migrações
alembic 


