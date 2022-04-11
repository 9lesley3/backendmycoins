from flask_restful import Resource
from models.ModelUser import ModelUser
from data.DataUser import get_data_user
from flask_jwt_extended import create_access_token
from Hashing.UserHashing import hash_password, check_hashed_password


class UserLogin(Resource):
    def post(self):
        data = get_data_user()
        user = ModelUser.find_by_login(data['login'])
        hashed_login = hash_password(data['login'])
        hashed_password = hash_password(data['password'])

        if user and check_hashed_password(user.login, hashed_login):
            if check_hashed_password(user.password, hashed_password):
                token_de_acesso = create_access_token(identity=user.user_id)
                return {'access_token': token_de_acesso}, 200
            else:
                return {'message': 'The password is incorrect.'}, 401  # Unauthorized
        else:
            return {'message': 'The username is incorrect.'}, 401  # Unauthorized
