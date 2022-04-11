from sql_alchemy import database
from flask import request, url_for
from requests import post

MAILGUN_DOMAIN = 'sandbox809ef63a9cf74d81bfbd24fd08426e45.mailgun.org'
MAILGUN_API_KEY = 'c19110bb688e6eeb5cfd5140f6da1152-162d1f80-8daefb3a'
FROM_TITLE = 'NO-REPLY'
FROM_EMAIL = 'no-reply@restapi.com'


class ModelUser(database.Model):
    __tablename__ = 'users'

    user_id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(40), nullable=False, unique=True)
    password = database.Column(database.String(40), nullable=False)
    email = database.Column(database.String(40), nullable=False, unique=True)
    activated = database.Column(database.Boolean, default=False)

    def __init__(self, login, password, email, activated):
        self.login = login
        self.password = password
        self.email = email
        self.activated = activated

    def send_confirmation_email(self):
        # 'http://127.0.0.1:5000/confirmation/{user_id}'
        link = request.url_root[:-1] + url_for('userconfirmed', user_id=self.user_id)
        # https://api.mailgun.net/v3/sandbox809ef63a9cf74d81bfbd24fd08426e45.mailgun.org
        post("https://api.mailgun.net/v3/{}/messages".format(MAILGUN_DOMAIN),
             auth=("api", MAILGUN_API_KEY),
             data={"from": '{} <{}>'.format(FROM_TITLE, FROM_EMAIL),
                   "to": self.email,
                   "subject": "MyCoins - Email Confimation",
                   "text": 'Confirm your registration by clicking on the link: {}'.format(link),
                   'html': '<html><p>\
                           Confirm your registration by clicking on the link: <a href="{}">CONFIRMAR EMAIL</a>\
                          </p></html>'.format(link)
                   }
             )

    def to_json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'email': self.email,
            'activated': self.activated
        }

    @classmethod
    def find_by_id(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()  # SELECT * FROM coins WHERE coin_id = $coin_id limited
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()  # SELECT * FROM coins WHERE coin_id = $coin_id limited
        if user:
            return user
        return None

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()  # SELECT * FROM coins WHERE coin_id = $coin_id limited
        if user:
            return user
        return None

    def save_user(self):
        database.session.add(self)
        database.session.commit()

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()
