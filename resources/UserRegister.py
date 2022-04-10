from flask_restful import Resource, reqparse
from models.ModelUser import ModelUser


def get_data_user():
    args = reqparse.RequestParser()

    args.add_argument('login', type=str, required=True,
                      help="The field 'login' cannot be left blank")
    args.add_argument('password', type=str, required=True,
                      help="The field 'password' cannot be left blank")

    return args.parse_args()


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
