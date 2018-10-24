from flask import Blueprint

user_api = Blueprint('user_api', __name__)

from oisapi_app.user_api import endpoints