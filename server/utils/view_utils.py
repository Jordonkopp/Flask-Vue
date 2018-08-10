from typing import Tuple, List

from flask import jsonify
from flask.wrappers import Response


def wrapped_response(data: dict = None, status: int = 200, message: str = "") -> Tuple[Response, int]:
    """
    Create a wrapped response to have uniform json response objects
    """

    if type(data) is not dict and data is not None:
        raise TypeError("Expected data to be type Dictionary")

    response = {
        "success": 200 <= status < 300,
        "code": status,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


def serialize_list(items: List) -> List:
    """Serializes a list of SQLAlchemy Objects, exposing their attributes.

    :param items - List of Objects that inherit from Mixin
    :returns List of dictionaries
    """
    if not items or items is None:
        return []
    return [x.to_dict() for x in items]
