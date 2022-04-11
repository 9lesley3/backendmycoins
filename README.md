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

Com o ambiente ativado vamos instalar o Flask com o seguinte comando:
pip install Flask

amos instalar também o Flask-Restful com o seguinte comando:
pip install Flask-Restful

instalando Flask-SQLAlchemy:
pip install Flask-SQLAlchemy

instalando flask_jwt_extended
pip install flask_jwt_extended

instalando passlib
pip install passlib

para descobrir quais pacotes foram instalados no seu ambiente, basta usar o seguinte comando:
python -m pip list

caso você queira criar essa informação para utilizar em outro abiente basta salva as informações geradas no pelo passo anterior em um arquivo de texto chamado requirements.txt
para instalar os pacotes em outro ambiente basta digitar o seguinte código no seu terminal:
pip install -r requirements.txt


# Referencias
virtualenv - https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
Flask - https://flask.palletsprojects.com/en/2.1.x/
Flask-Restful - https://flask-restful.readthedocs.io/en/latest/

Para inicializar o serviço de API de o seguinte comando:
python3 app.py

# Documentation
myCoins - https://documenter.getpostman.com/view/16185090/UVyyuDQt
searchCoinsWithFilter - https://documenter.getpostman.com/view/16185090/UVyyuDV9
userMyCoinsLogin - https://documenter.getpostman.com/view/16185090/UVyyuDVB

[comment]: <> (http://127.0.0.1:5000/coins)