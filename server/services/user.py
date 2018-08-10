from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timedelta
from server.utils.view_utils import wrapped_response, serialize_list
from server.models.key import Key
from server.models.user import User
from server.utils.core_utils import logger
from server import db
import jwt

user = Blueprint("/users/v1", __name__)


@user.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    current_user = User.authenticate(**data)

    if not current_user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'sub': current_user.email,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})
