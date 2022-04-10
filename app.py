from flask import Flask
from flask_restful import Api
from resources.Coin import Coin
from resources.Coins import Coins
from resources.User import User
from resources.UserRegister import UserRegister
from resources.UserLogin import UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coin_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database():
    database.create_all()


api.add_resource(Coins, '/coins')
api.add_resource(Coin, '/coin/<int:coin_id>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')


if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
