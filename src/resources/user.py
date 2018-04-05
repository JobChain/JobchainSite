from flask_restful import Resource, reqparse
from models.users import UserModel

#Use this to find user by id can also delete the user
#Example:
#GET
#{url}/user/<int: id>
#RETURNS {name:str, work:listof(WORK), education:listof(EDUCATION)}

#DELETE
#{url}/user/<int: id>
#RETURNS {message:str}

class User(Resource):
    parser = reqparse.RequestParser()

    def get(self, id):
        user = UserModel.find_by_id(id):

        if user:
            return user.json()
        else:
            return {'message': 'User not in Database'}, 404

    def delete(self, id):
        user = UserModel.find_by_id()

        if user:
            user.delete_from_db()

        return {'message': 'User Deleted :D'}
