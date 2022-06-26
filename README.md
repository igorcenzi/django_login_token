<h1 align="left">👨‍💻 Autenticação com restframework-simplejwt 👨‍💻</h1>

###

<p align="left">Neste projeto simples criado com o intuito de ser um exemplo de criação de usuário e login, devolvendo um JWT.</p>

###

<h3 align="left">Como rodar o projeto 🧰</h3>

###

<p align="left">- Primeiramente você terá que clonar o repositório usando o comando:<br><br>git clone git@github.com:igorcenzi/django_login_token.git<br><br>- Agora você precisa criar um venv na pasta do projeto com o comando<br><br>python -m venv venv<br><br>- Em seguida você vai entrar no ambiente virtual<br><br>- Para instalar os requisitos, execute o comando<br><br>pip install -r requirements.txt<br><br>- Execute esses dois comandos para criar o banco de dados<br><br>python manage.py makemigrations<br>python manage.py migrate<br><br>- Com tudo isso feito, agora é só rodar o servidor usando<br><br>python manage.py runserver</p>

###

<h3 align="left">Endpoints</h3>

###

<p align="left">O projeto possui apenas 2 endpoints, um para registrar o usuário e outro para fazer o login.</p>

###

<h3 align="left">Registrar Usuário 👨‍💼 - /api/register</h3>

###

<p align="left">Nele você vai apenas precisar enviar um json com email e senha.<br><br>{<br>  "email": "exemplo@mail.com",<br>  "password": "strong_p@ssword123"<br>}</p>

###

<h3 align="left">Login 🔏 - /api/login</h3>

###

<p align="left">Aqui você também irá enviar o email e senha que foram cadastrados e ele te retornará um token.<br><br>{<br>  "email": "exemplo@mail.com",<br>  "password": "strong_p@ssword123"<br>}</p>

###
