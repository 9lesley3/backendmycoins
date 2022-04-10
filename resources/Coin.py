from flask_restful import Resource, reqparse
from models.ModelCoin import ModelCoin


def get_data_coin():
    args = reqparse.RequestParser()

    args.add_argument('description', type=str, required=True,
                      help="The field 'description' cannot be left blank")
    args.add_argument('value', type=float, required=True,
                      help="The field 'value' cannot be left blank")
    args.add_argument('conservation_state', type=str, required=True,
                      help="The field 'conservation_state' cannot be left blank")
    args.add_argument('country', type=str, required=True,
                      help="The field 'country' cannot be left blank")
    args.add_argument('year', type=int, required=True,
                      help="The field 'year' cannot be left blank")

    data = args.parse_args()
    return data


class Coins(Resource):
    @staticmethod
    def get():
        return {'coins': [coin.to_json() for coin in ModelCoin.query.all()]}


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
