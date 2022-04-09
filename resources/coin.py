from flask_restful import Resource, reqparse

value_id = 2
coins = [
    {
        'coin_id': 0,
        'description': 'Moeda de um real',
        'value': 1,
        'conservation_state': 'BC',
        'country': 'Brazil',
        'year': 2019
    },
    {
        'coin_id': 1,
        'description': 'Moeda de um real',
        'value': 1,
        'conservation_state': 'BC',
        'country': 'Brazil',
        'year': 2018
    },
    {
        'coin_id': 2,
        'description': 'Moeda de um real',
        'value': 1,
        'conservation_state': 'BC',
        'country': 'Brazil',
        'year': 2022
    },
]


def update_coin_id():
    global value_id
    value_id = value_id + 1


def get_data_coin():
    args = reqparse.RequestParser()

    args.add_argument('description')
    args.add_argument('value')
    args.add_argument('conservation_state')
    args.add_argument('country')
    args.add_argument('year')

    data = args.parse_args()
    return data


def add_coins():
    data = get_data_coin()
    new_coin = {'coin_id': value_id, **data}

    coins.append(new_coin)
    return new_coin


def find_coin_by_id(coin_id):
    for coin in coins:
        if coin['coin_id'] == coin_id:
            return coin


class Coins(Resource):
    @staticmethod
    def get():
        return coins


class Coin(Resource):
    @staticmethod
    def get(coin_id):
        coin = find_coin_by_id(coin_id)
        if coin:
            return coin
        return {'message': 'Coin not found.'}, 404

    @staticmethod
    def post(coin_id):
        update_coin_id()
        new_coins = add_coins()
        return new_coins, 200

    @staticmethod
    def put(coin_id):
        data = get_data_coin()
        new_coin = {'coin_id': coin_id, **data}

        coin = find_coin_by_id(coin_id)
        if coin:
            coin.update(new_coin)
            return new_coin, 200
        coins.append(new_coin)
        return new_coin, 201

    @staticmethod
    def delete(coin_id):
        coin = find_coin_by_id(coin_id)
        if coin:
            coins.remove(coin)
            return {'message': 'Coin deleted.'}
        return {'message': 'Coin not found.'}, 404
