from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    number = db.Column(db.String(64))
    result = db.Column(db.Integer)


class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5))
    if_used = db.Column(db.Boolean)
