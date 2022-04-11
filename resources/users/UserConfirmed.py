from flask_restful import Resource
from models.ModelUser import ModelUser
from flask import make_response, render_template


class UserConfirmed(Resource):
    @classmethod
    def get(cls, user_id):
        user = ModelUser.find_by_id(user_id)
        if user:
            user.activated = True
            user.save_user()
            headers = {'Content-Type': 'text/html'}
            return make_response(
                render_template(
                    'user_confirm.html',
                    email=user.email,
                    user=user.login
                ),
                200,
                headers)
        else:
            return {"message": "User id '{}' not found.".format(user_id)}, 404
