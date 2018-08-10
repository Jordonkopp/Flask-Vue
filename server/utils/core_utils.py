from typing import Tuple

from werkzeug.local import LocalProxy
from flask import current_app
from flask.wrappers import Response

from server.utils.view_utils import wrapped_response

# logger object for all views to use
logger = LocalProxy(lambda: current_app.logger)


# add specific Exception handlers before this, if needed
def all_exception_handler(error: Exception) -> Tuple[Response, int]:
    """
    Handles all exceptions, add more specific error Handlers.
    """
    return wrapped_response(message=str(error), status=500)