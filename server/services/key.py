from flask import Blueprint, jsonify, request
from server.utils.view_utils import wrapped_response, serialize_list
from server.models.key import Key
from server.utils.core_utils import logger
from server.utils.auth import token_required
from server import db

key = Blueprint("/keys/v1", __name__)


# sanity check route
@key.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@key.route('/keys', methods=['GET', 'POST'])
@token_required
def all_keys(user):
    if request.method == 'POST':
        # TODO: Log Access when Auth is implemented
        logger.info("Creating new Key: {}".format(user.email))
        data = request.get_json()

        k = data['key']

        # TODO: When Auth is implemented retrieve logged in user
        # user = User.query.filter(User.username == auth.username()).first()

        # Create Key
        new_key = Key(key=k, user=user)

        logger.info("{}".format(new_key))
        try:
            # Save both objects
            db.session.add(new_key)
            db.session.commit()
            logger.info("new Key: {} created by: {}".format(new_key.key, user.email))
            json_response, status = wrapped_response({"key_id": new_key.id, "key": new_key.key}, 200,
                                                     'Key successfully created')
            return json_response

        except Exception as e:
            # TODO: reduce error message verbosity when debug flag is False by using sys.tracebacklimit = 0
            json_response, status = wrapped_response({}, 400, "{}, {}".format(type(e).__name__, e))
            return json_response
    else:
        try:
            # TODO: Log Access when Auth is implemented
            logger.info("Key List Accessed by: {}".format(user.email))

            keys = Key.query.filter(Key.creator_id == user.id).all()

            data = {"keys": serialize_list(keys)}
            status = 200
            message = "List of all current keys created by currently logged in user"

        except Exception as e:

            logger.error("Error: {}".format(e))
            data = {}
            status = 500
            message = e

        # TODO: reduce error message verbosity when debug flag is False by using sys.tracebacklimit = 0
        json_response, status = wrapped_response(data, status, message)
        return json_response


@key.route('/keys/<key_id>', methods=['DELETE', 'GET'])
@token_required
def single_key(user, key_id):
    if request.method == 'DELETE':
        try:
            # TODO: Log Access when Auth is implemented
            logger.info("Key Delete Accessed by: {}".format(user.email))

            k = Key.query.filter(Key.id == key_id).first()

            if k:
                if k.creator_id == user.id:
                    db.session.delete(k)
                    db.session.commit()
                    data = {}
                    status = 202
                    message = "Key: {} deleted by: {}".format(k.key, user.email)
                    logger.info("Key: {} deleted by: {}".format(k.key, user.email))
                else:
                    data = {
                        'message': "Unauthorized access"
                    }
                    status = 401
                    return jsonify(data), status
            else:
                data = {}
                status = 404
                message = "Key not found with ID: {}".format(key_id)
        except Exception as e:

            logger.error("Error: {}".format(e))
            data = {}
            status = 500
            message = e

        # TODO: reduce error message verbosity when debug flag is False by using sys.tracebacklimit = 0
        json_response, status = wrapped_response(data, status, message)
        return json_response
    elif request.method == 'GET':
        try:
            # TODO: Log Access when Auth is implemented
            logger.info("Key GET Accessed by: {}".format(user.email))

            k = Key.query.filter(Key.key == key_id).first()

            if k:
                if k.creator_id == user.id:
                    data = {"key": k.to_dict()}
                    status = 200
                    message = "Get Key by key_id owned by user"
                else:
                    data = {
                        'message': "Unauthorized access"
                    }
                    status = 401
                    return jsonify(data), status
            else:
                data = {}
                status = 404
                message = "Key not found with ID: {}".format(key_id)

        except Exception as e:

            logger.error("Error: {}".format(e))
            data = {}
            status = 500
            message = e

        # TODO: reduce error message verbosity when debug flag is False by using sys.tracebacklimit = 0
        json_response, status = wrapped_response(data, status, message)
        return json_response