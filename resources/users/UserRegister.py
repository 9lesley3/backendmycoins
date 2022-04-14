import traceback
from flask_restful import Resource
from models.ModelUser import ModelUser
from data.DataUser import get_data_user


class UserRegister(Resource):
    # /register
    def post(self):
        data = get_data_user()
        if not data.get('email') or data.get('email') is None:
            return {'message': 'The field email cannot be left blank'}, 400

        if ModelUser.find_by_email(data['email']):
            return {'message': "The email '{}' already exists.".format(data['email'])}, 400

        if ModelUser.find_by_login(data['login']):
            return {'message': "The login '{}' already exists.".format(data['login'])}, 400

        user = ModelUser(**data)
        user.activated = False
        try:
            user.save_user()
            user.send_confirmation_email()
        except:
            user.delete_user()
            traceback.print_exc()
            return {'message': 'An internal server error has occurred.'}, 500

        return {'message': 'User created successfully'}, 201
