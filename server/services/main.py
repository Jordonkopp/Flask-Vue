from flask import Blueprint, redirect, url_for
from server.utils.core_utils import logger

# Create Blueprint
main = Blueprint("main", __name__)


# redirect when you visit /
@main.route("/")
def index():
    logger.info("Base redirect")
    return redirect(url_for('keys'))
