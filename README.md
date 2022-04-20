<div>
    <img height="150em" align="center" src="https://github-readme-stats.vercel.app/api?username=lesleydsilva&show_icons=true&theme=synthwave"/>
    <img height="150em" align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra&layout=compact"/>
</div>

![Teste reports](https://github.com/lesleydsilva/backendmycoins/blob/v0.0.1/reports/newman/html/test_my_coins.html)


# Backend My Coins
Back end para a aplicação Mycoins

# Inicializa projeto python
crie um repositório, indico que faça isso usando o git, e insira um arquivo app.py que é responsavel pelo codigo principal da aplicação


# Inicializa ambiente virtual
No terminal naveque até o repositorio criado seção anterior.
Este projeto usa um ambiente virtual com virtualenv, para instalar o virtualenv basta usar o comando:
```bash
sudo pip install virtualenv
```


Pronto, agora que temos o virtualenv instalado vamos criar um ambiente virtual usando o comando:
virtualenv nome do meu ambiente virtual --python=versão do python
neste projeto usamos esse comando da seguinte forma:
```bash
virtualenv flask --python=python3.8
```
Para ativar o ambiente criado podemos utilizar o comando:
```bash
source flask/bin/activate 
```

Caso deseje desativar o ambiente basta digitar o seguinte comando no seu terminal:
```bash
deactivate
```
mas não iremos fazer isso no momento

Com o ambiente ativado vamos instalar o Flask com o seguinte comando: pip install -r requirements.txt
o arquivo requirements.txt contém todos os pacotes e as suas respetivas versões, necessárias para rodar essa aplicação.

para descobrir quais pacotes foram instalados no seu ambiente, basta usar o seguinte comando:
```bash
python -m pip list
```
caso você queira criar essa informação para utilizar em outro abiente basta salva as informações geradas no pelo passo anterior em um arquivo de texto chamado requirements.txt
para instalar os pacotes em outro ambiente basta digitar o seguinte código no seu terminal:
```bash
pip install -r requirements.txt
```
Procure o arquivo bash_profile ou bashrc e insira as seguintes variáveis de ambiente:
```bash
SQLALCHEMY_DATABASE_URI
JWT_SECRET_KEY
PASSWORD
DATABASE
USER
```
# Heroku
Cria uma instancia no heroku
```bash
heroku git:remote -a restapimycoins
```
Cria banco de dados
```bash
heroku addons:create heroku-postgresql:hobby-dev --app restapimycoins
```
captura o endereço do banco de dados
```bash
heroku config --app restapimycoins
```
deploy
```bash
git push heroku main
```
login
```bash
heroku login
```
logs
```bash
heroku logs --tail
```


# Referencias
 - virtualenv - https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
 - Flask - https://flask.palletsprojects.com/en/2.1.x/
 - Flask-Restful - https://flask-restful.readthedocs.io/en/latest/
 - teste de apai - https://renatogroffe.medium.com/automatizando-testes-de-apis-rest-com-postman-newman-a90f0d90df09

Para inicializar o serviço de API de o seguinte comando:
```bash
python3 app.py
```
# Documentation
 - myCoins - https://documenter.getpostman.com/view/16185090/UVyyuDQt
 - searchCoinsWithFilter - https://documenter.getpostman.com/view/16185090/UVyyuDV9
 - userMyCoinsLogin - https://documenter.getpostman.com/view/16185090/UVyyuDVB

[comment]: <> (http://127.0.0.1:5000/coins)