from flask import jsonify, request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError, post_load
from framework.cache import Cache, cache, NoCacheResponse
import uuid
import ast


class UserListResource(Resource):
    def __init__(self):
        self.cache = Cache().get_strict()

    @cache('some_key', 10)
    def get(self):
        return map(lambda u: ast.literal_eval(u), self.cache.hvals('users'))

    def post(self):
        try:
            # works as validation
            user = User.deserialize(request.json)
            self.cache.hset('users', user.uuid, user.serialize())

            return user.serialize(), 201

        except ValidationError as e:
            return jsonify(e.messages)


class UserResource(Resource):
    def __init__(self):
        self.cache = Cache().get_strict()

    @cache('some_other_key', 10, True)
    def get(self, user_uuid):
        return ast.literal_eval(self.cache.hget('users', user_uuid))

    def put(self, user_uuid):
        try:
            # works as validation
            user = User.deserialize(request.json)
            self.cache.hset('users', user_uuid, user.serialize())

            return user.serialize(), 200

        except ValidationError as e:
            return jsonify(e.messages)

    def delete(self, user_uuid):
        self.cache.hdel('users', user_uuid)

        return 200


class User(object):
    def __init__(self, email, password):
        self.uuid = uuid.uuid4()
        self.email = email
        self.password = password

    def __repr__(self):
        return 'uuid: {self.uuid!r}, email: {self.email!r}, password: {self.password!r}'.format(self=self)

    def serialize(self):
        return UserSchema(strict=True).dump(self).data

    @staticmethod
    def deserialize(json):
        return UserSchema(strict=True).load(json).data


class UserSchema(Schema):
    uuid = fields.UUID()
    email = fields.Email()
    password = fields.Str()

    @post_load
    def make_user(self, data):
        return User(data["email"], data["password"])

