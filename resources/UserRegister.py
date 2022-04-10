from flask_restful import Resource
from models.ModelUser import ModelUser
from data.DataUser import get_data_user


class UserRegister(Resource):
    @staticmethod
    # /register
    def post():
        data = get_data_user()
        if ModelUser.find_by_login(data['login']):
            return {'message': "The login '{}' already exists.".format(data['login'])}

        user = ModelUser(**data)
        user.save_user()
        return {'message': 'User created successfully'}, 201
