from flask import Flask
from flask_restful import Api
from resources.coin import Coins, Coin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coin_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_database():
    database.create_all()


api.add_resource(Coins, '/coins')
api.add_resource(Coin, '/coins/<int:coin_id>')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
