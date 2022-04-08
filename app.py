from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

coins = [
    {
        'coinId': 0,
        'description': 'Moeda de um real',
        'value': 1,
        'conservationState': 'BC',
        'country': 'Brazil',
        'year': 2019
    },
    {
        'coinId': 1,
        'description': 'Moeda de um real',
        'value': 1,
        'conservationState': 'BC',
        'country': 'Brazil',
        'year': 2018
    },
    {
        'coinId': 2,
        'description': 'Moeda de um real',
        'value': 1,
        'conservationState': 'BC',
        'country': 'Brazil',
        'year': 2022
    },
]


class Coins(Resource):
    def get(self):
        return {'coins': coins}


api.add_resource(Coins, '/coins')

if __name__ == '__main__':
    app.run(debug=True)
