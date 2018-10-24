from flask import Flask
from config import Config

def create_app(config_class=Config):

	app = Flask(__name__)
	app.config.from_object(config_class)

	from oisapi_app.user_api import user_api
	app.register_blueprint(user_api, url_prefix='/user-api')

	return app