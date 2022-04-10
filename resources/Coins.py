from flask_restful import Resource
from models.ModelCoin import ModelCoin


class Coins(Resource):
    @staticmethod
    def get():
        return {'coins': [coin.to_json() for coin in ModelCoin.query.all()]}

