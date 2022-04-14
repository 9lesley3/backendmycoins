import os


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
DATABASE_URL = "postgres://padvgpdcqxnhhz:4bbc774dc17de1779d7b30209454e703174989e85a033c606672b690c4bcab47@ec2-44-199 \
               -143-43.compute-1.amazonaws.com:5432/d1evmfqifcmdk6 "
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')
USER = os.environ.get('USER')
HOST = 'localhost'
PORT = '5432'

