from flask_restful import Resource
from models.ModelCoin import ModelCoin
from data.DataCoin import get_data_coin


class Coin(Resource):
    @staticmethod
    def get(coin_id):
        coin = ModelCoin.find_by_id(coin_id)
        if coin:
            return coin.to_json()
        return {'message': 'Coin not found.'}, 404

    @staticmethod
    def post(coin_id):
        if ModelCoin.find_by_id(coin_id):
            return {'message': "Coin id '{} already exists.".format(coin_id)}, 400

        data = get_data_coin()
        coin = ModelCoin(coin_id, **data)

        try:
            coin.save_coin()
        except:
            return {'message': 'An internal error occurred trying to save coin'}, 500

        return coin.to_json()

    @staticmethod
    def put(coin_id):
        data = get_data_coin()
        found_coin = ModelCoin.find_by_id(coin_id)

        if found_coin:
            found_coin.update_coin(**data)
            found_coin.save_coin()
            return found_coin.to_json(), 200

        coin = ModelCoin(coin_id, **data)
        coin.save_coin()
        return coin.to_json(), 201

    @staticmethod
    def delete(coin_id):
        coin = ModelCoin.find_by_id(coin_id)
        if coin:
            coin.delete_coin()
            return {'message': 'Coin deleted.'}
        return {'message': 'Coin not found.'}, 404
