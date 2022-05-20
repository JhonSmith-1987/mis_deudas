from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id_usuario, fullname, email,  username, password) -> None:
        self.id_usuario = id_usuario
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password


    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)