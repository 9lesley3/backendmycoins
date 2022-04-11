from flask import Flask, jsonify
from flask_restful import Api
from resources.coins.Coin import Coin
from resources.coins.Coins import Coins
from resources.users.User import User
from resources.users.UserRegister import UserRegister
from resources.users.UserLogin import UserLogin
from resources.users.UserLogout import UserLogout
from resources.users.UserConfirmed import UserConfirmed
from flask_jwt_extended import JWTManager
from denylist import DENYLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coin_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database():
    database.create_all()


@jwt.token_in_blocklist_loader
def verify_deny_list(self, token):
    return token['jti'] in DENYLIST


@jwt.revoked_token_loader
def token_access_invalidated(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401


api.add_resource(Coins, '/coins')
api.add_resource(Coin, '/coin/<int:coin_id>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserConfirmed, '/confirmation/<int:user_id>')


if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
