from flask_restful import reqparse


def get_data_user():
    args = reqparse.RequestParser()

    args.add_argument('login', type=str, required=True,
                      help="The field 'login' cannot be left blank")
    args.add_argument('password', type=str, required=True,
                      help="The field 'password' cannot be left blank")

    return args.parse_args()