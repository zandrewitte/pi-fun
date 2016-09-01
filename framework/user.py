from marshmallow import Schema, fields, post_load
import uuid


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