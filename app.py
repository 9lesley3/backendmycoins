from flask import Flask
from flask_restful import Api
from resources.Coin import Coin
from resources.Coins import Coins
from resources.User import User
from resources.UserRegister import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coin_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_database():
    database.create_all()


api.add_resource(Coins, '/coins')
api.add_resource(Coin, '/coin/<int:coin_id>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
