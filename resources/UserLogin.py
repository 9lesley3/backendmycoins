from flask_restful import Resource
from models.ModelUser import ModelUser
from data.DataUser import get_data_user
from flask_jwt_extended import create_access_token
from hmac import compare_digest


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = get_data_user()
        user = ModelUser.find_by_login(data['login'])

        print("-------------")
        print(user.user_id)
        print(user.login)
        print(user.password)
        print("-------------")
        print(data['login'])
        print(data['password'])
        print("-------------")

        if user and compare_digest(user.password, data['password']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'The username or password is incorrect.'}, 401  # Unauthorized
