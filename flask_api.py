from flask import Flask, jsonify, make_response
from flask_restful import Api
from resources.health_resource import HealthResource
from resources.user_resource import UserListResource, UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(HealthResource, '/health')
api.add_resource(UserListResource, '/user')
api.add_resource(UserResource, '/user/<string:user_uuid>')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
