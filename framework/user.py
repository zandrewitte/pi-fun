from marshmallow import Schema, fields, post_load
import uuid
import dill


class User(object):
    def __init__(self, email, password):
        self.uuid = uuid.uuid4()
        self.email = email
        self.password = password

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


u = User('emal@emal.com', 'test')