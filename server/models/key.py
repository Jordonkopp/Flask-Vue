from . import db
from server.utils.model_utils import Mixin


class Key(Mixin, db.Model):
    """Key Table."""

    __tablename__ = "key"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    key = db.Column(db.String, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, key, user):
        self.key = key
        self.creator_id = user.id

    def __repr__(self):
        return "<Key {}>".format(self.key)