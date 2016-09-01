from flask import jsonify
from flask_restful import Resource
from framework.cache import Cache


class HealthResource(Resource):
    def __init__(self):
        self.cache = Cache().get_strict()
        self.health = 'OK'

    def get(self):
        return jsonify({'Health': self.health})

    @staticmethod
    def print_value(res):
        print 'Response: %s' % res
