from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from denylist import DENYLIST


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']

        DENYLIST.add(jwt_id)
        return {'message': 'Logged out successfully.'}, 200
