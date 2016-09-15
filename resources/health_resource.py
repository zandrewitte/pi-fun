from flask import jsonify, request
from flask_restful import Resource


class HealthResource(Resource):
    def __init__(self):
        self.health = 'OK'

    def get(self):
        # print request.headers
        print request.headers
        print request.query_string
        print request.remote_addr
        print dict(request.args)
        print request.url
        print request.get_json(silent=True)

        return jsonify({'Health': self.health})

    @staticmethod
    def print_value(res):
        print 'Response: %s' % res
