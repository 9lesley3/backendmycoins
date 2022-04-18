import traceback
from flask_restful import Resource
from models.ModelUser import ModelUser
from data.DataUser import get_data_user


class UserRegister(Resource):
    # /register
    def post(self, user_id):
        data = get_data_user()
        if not data.get('email') or data.get('email') is None:
            return {'message': 'The field email cannot be left blank'}, 400

        if ModelUser.find_by_email(data['email']):
            return {'message': "The email ({}) already exists.".format(data['email'])}, 400

        if not data.get('login') or data.get('login') is None or (data.get('login') == ""):
            return {'message': 'The login email cannot be left blank'}, 400

        if ModelUser.find_by_login(data['login']):
            return {'message': "The login ({}) already exists.".format(data['login'])}, 400

        if not data.get('password') or data.get('password') is None or (data.get('password') == ""):
            return {'message': 'The field password cannot be left blank'}, 400

        user = ModelUser(user_id, **data)
        user.activated = False
        try:
            user.save_user()
            user.send_confirmation_email()
        except:
            user.delete_user()
            traceback.print_exc()
            return {'message': 'An internal server error has occurred.'}, 500

        return user.to_json(), 201
