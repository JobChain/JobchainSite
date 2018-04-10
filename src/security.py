from models.admin import AdminModel
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    admin = UserModel.find_by_username(username)
    if admin and safe_str_cmp(user.password, password):
        return admin


def identity(payload):
    user_id = payload['identity']
    return AdminModel.find_by_id(user_id)
