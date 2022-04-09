from flask import Flask
from flask_restful import Api
from resources.coin import Coins, Coin

app = Flask(__name__)
api = Api(app)

api.add_resource(Coins, '/coins')
api.add_resource(Coin, '/coins/<int:coin_id>')

if __name__ == '__main__':
    app.run(debug=True)
