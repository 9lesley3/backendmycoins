# backendmycoins
Back end para a aplicação Mycoins

# Inicializa projeto python
crie um repositório, indico que faça isso usando o git, e insira um arquivo app.py que é responsavel pelo codigo principal da aplicação


# Inicializa ambiente virtual
No terminal naveque até o repositorio criado seção anterior.
Este projeto usa um ambiente virtual com virtualenv, para instalar o virtualenv basta usar o comando:
sudo pip install virtualenv

Pronto, agora que temos o virtualenv instalado vamos criar um ambiente virtual usando o comando:
virtualenv nome do meu ambiente virtual --python=versão do python
neste projeto usamos esse comando da seguinte forma:
virtualenv flask --python=python3.8

Para ativar o ambiente criado podemos utilizar o comando:
source flask/bin/activate 

Caso deseje desativar o ambiente basta digitar o seguinte comando no seu terminal:
deactivate
mas não iremos fazer isso no momento

Com o ambiente ativado vamos instalar o Flask com o seguinte comando: pip install -r requirements.txt
o arquivo requirements.txt contém todos os pacotes e as suas respetivas versões, necessárias para rodar essa aplicação.
Conteúdo do arquivo requirements.txt
Package                  Version
------------------------ ---------
aniso8601                9.0.1
attrs                    21.4.0
certifi                  2021.10.8
charset-normalizer       2.0.12
click                    8.1.2
clickclick               20.10.2
connexion                2.6.0
Flask                    2.1.1
Flask-JWT-Extended       4.3.1
Flask-RESTful            0.3.9
Flask-SeaSurf            1.1.1
Flask-SQLAlchemy         2.5.1
greenlet                 1.1.2
idna                     3.3
importlib-metadata       4.11.3
inflection               0.5.1
itsdangerous             2.1.2
Jinja2                   3.1.1
jsonschema               4.4.0
MarkupSafe               2.1.1
openapi-schema-validator 0.2.3
openapi-spec-validator   0.4.0
packaging                21.3
passlib                  1.7.4
pip                      22.0.4
psycopg2-binary          2.9.3
PyJWT                    2.3.0
pyparsing                3.0.8
pyrsistent               0.18.1
pytz                     2022.1
PyYAML                   6.0
requests                 2.27.1
resources                0.0.1
setuptools               58.1.0
six                      1.16.0
SQLAlchemy               1.4.35
urllib3                  1.26.9
Werkzeug                 2.1.1
wheel                    0.37.1
zipp                     3.8.0


para descobrir quais pacotes foram instalados no seu ambiente, basta usar o seguinte comando:
python -m pip list

caso você queira criar essa informação para utilizar em outro abiente basta salva as informações geradas no pelo passo anterior em um arquivo de texto chamado requirements.txt
para instalar os pacotes em outro ambiente basta digitar o seguinte código no seu terminal:
pip install -r requirements.txt


Procure o arquivo bash_profile ou bashrc e insira as seguintes variáveis de ambiente:
SQLALCHEMY_DATABASE_URI
JWT_SECRET_KEY
PASSWORD
DATABASE
USER

# Heroku
Cria uma instancia no heroku
heroku git:remote -a restapimycoins
Cria banco de dados
heroku addons:create heroku-postgresql:hobby-dev --app restapimycoins
captura o endereço do banco de dados
heroku config --app restapimycoins
deploy
git push heroku main
login
heroku login
logs
heroku logs --tail


# Referencias
 - virtualenv - https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
 - Flask - https://flask.palletsprojects.com/en/2.1.x/
 - Flask-Restful - https://flask-restful.readthedocs.io/en/latest/

Para inicializar o serviço de API de o seguinte comando:
python3 app.py

# Documentation
 - myCoins - https://documenter.getpostman.com/view/16185090/UVyyuDQt
 - searchCoinsWithFilter - https://documenter.getpostman.com/view/16185090/UVyyuDV9
 - userMyCoinsLogin - https://documenter.getpostman.com/view/16185090/UVyyuDVB

[comment]: <> (http://127.0.0.1:5000/coins)