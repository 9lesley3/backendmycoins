from flask_restful import Resource
from models.ModelUser import ModelUser


class UserLogin(Resource):
    @classmethod
    def post(cls):
