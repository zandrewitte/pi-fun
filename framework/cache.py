from sys import argv
from redis import ConnectionPool, StrictRedis
import ast
from singleton import Singleton

script, redisHost, redisPort = argv


class Cache(object):
    __metaclass__ = Singleton

    def __init__(self):
        print "Running Cache Init"
        pool = ConnectionPool(host=redisHost, port=redisPort)
        self.strict = StrictRedis(connection_pool=pool)

    def get_strict(self):
        return self.strict


def cache(cache_key, seconds, with_args=False):
    def decorated(f):
        def wrapper(*args, **kwargs):
            c = Cache().get_strict()

            if with_args:
                key = "%s_%s" % (cache_key, "_".join(map(str, kwargs.values())))
            else:
                key = cache_key

            if c.exists(key):
                print "Cache Fetched"
                return ast.literal_eval(c.get(key))
            else:
                print "Calculated"
                try:
                    response = f(*args, **kwargs)
                    c.set(key, response, seconds)
                    return response
                except NoCacheResponse as e:
                    return e.value, e.status_code
                except ValueError:
                    return {}, 204
        return wrapper
    return decorated


class NoCacheResponse(Exception):
    def __init__(self, value=None, status_code=None):
        super(NoCacheResponse, self).__init__()
        self.value = value
        self.status_code = status_code

