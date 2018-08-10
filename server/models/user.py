from . import db
from server.utils.model_utils import Mixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(Mixin, db.Model):
    """User Table."""

    __tablename__ = "user"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    db.relationship('Key', backref="creator", lazy=False)

    def __init__(self, email, password):
        self.username = email
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def __repr__(self):
        return "<User {}>".format(self.username)
