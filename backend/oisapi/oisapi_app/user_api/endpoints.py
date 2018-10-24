from flask import jsonify
from oisapi_app.user_api import user_api

# Initial route to test interoperation of front- and backend
@user_api.route('/hello')
def say_hello():
	return jsonify({'msg' : 'hello from the ois api!'})