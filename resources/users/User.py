from flask_restful import Resource
from models.ModelUser import ModelUser
from flask_jwt_extended import jwt_required


class User(Resource):
    # /user/{user_id}
    def get(self, user_id):
        user = ModelUser.find_by_id(user_id)
        if user:
            return user.to_json(), 200
        return {'message': 'User not found.'}, 404

    @jwt_required()
    def delete(self, user_id):
        user = ModelUser.find_by_id(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404
