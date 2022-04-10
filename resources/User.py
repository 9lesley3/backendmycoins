from flask_restful import Resource
from models.ModelUser import ModelUser


class User(Resource):
    @staticmethod
    # /user/{user_id}
    def get(user_id):
        user = ModelUser.find_by_id(user_id)
        if user:
            return user.to_json()
        return {'message': 'User not found.'}, 404

    @staticmethod
    def delete(user_id):
        user = ModelUser.find_by_id(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404
