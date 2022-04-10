from flask_restful import Resource
from models.ModelUser import ModelUser
from data.DataUser import get_data_user
from flask_jwt_extended import create_access_token
from hmac import compare_digest


class UserLogin(Resource):
    def post(self):
        data = get_data_user()
        user = ModelUser.find_by_login(data['login'])

        if user and compare_digest(user.password, data['password']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'The username or password is incorrect.'}, 401  # Unauthorized
