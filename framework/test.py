from marshmallow import Schema, fields, post_load
import json


class StringValue(object):
    def __init__(self, string_value):
        self.string_value = string_value


class StringValueSchema(Schema):
    string_value = fields.Str()
    __model__ = StringValue

    @post_load
    def make_string_value(self, data):
        return self.__model__(**data)


class IntValue(object):
    def __init__(self, int_value):
        self.int_value = int_value


class IntValueSchema(Schema):
    int_value = fields.Int()
    __model__ = IntValue

    @post_load
    def make_int_value(self, data):
        return self.__model__(**data)


class CustomValue(fields.Field):

    __schemas__ = [StringValueSchema, IntValueSchema]

    def _serialize(self, value, attr, obj):
        print value
        print attr
        print obj
        return value

    def _deserialize(self, value, attr, data):
        return self.__try_deserialize(self.__schemas__, value)

    @staticmethod
    def __try_deserialize(schemas, value):
        for schema in schemas:
            try:
                return schema().load(value).data
            except TypeError:
                pass


class Test(object):
    def __init__(self, name, some_value):
        self.name = name
        self.some_value = some_value


class TestSchema(Schema):
    name = fields.Str()
    some_value = CustomValue()
    __model__ = Test

    @post_load
    def make_test(self, data):
        return self.__model__(**data)

json1 = json.dumps({
    "name": "test",
    "some_value": {
        'string_value': 'some_string_value'
    }
})
json2 = json.dumps({
    "name": "test",
    "some_value": {
        "int_value": 1
    }
})


def partition(l, f):
    a = []
    b = []
    for i in l:
        if f(i):
            a.append(i)
        else:
            b.append(i)

    return a, b


print partition([1, 2, 3, 5, 6, 3], lambda i: i >= 5)


def partition_by_field(l, field):
    dict_set = {}
    for i in l:
        dict_set.setdefault(i.__dict__[field].__class__.__name__, [])
        dict_set[i.__dict__[field].__class__.__name__].append(i)

    return dict_set.items()


print partition_by_field([TestSchema().loads(json1).data, TestSchema().loads(json1).data,
                          TestSchema().loads(json2).data], 'some_value')
