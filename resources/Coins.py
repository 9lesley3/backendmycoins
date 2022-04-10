from flask_restful import Resource
from models.ModelCoin import ModelCoin


class Coins(Resource):
    def get(self):
        return {'coins': [coin.to_json() for coin in ModelCoin.query.all()]}

