from redis import ConnectionPool, StrictRedis, ConnectionError
import ast
from singleton import Singleton
import yaml_reader
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Cache(object):
    __metaclass__ = Singleton

    def __init__(self, config_location='../conf/redis.yaml'):
        redis_config = yaml_reader.read_yaml(config_location).get('redis', {'host': 'localhost', 'port': 6379})
        pool = ConnectionPool(**redis_config)
        self.strict = StrictRedis(connection_pool=pool)

    def get_strict(self):
        return self.strict


def cache(cache_key, seconds, with_args=False):
    def decorated(f):
        def wrapper(*args, **kwargs):
            try:
                c = Cache().get_strict()

                if with_args:
                    key = "%s_%s" % (cache_key, "_".join(map(str, list(args) + kwargs.values())))
                else:
                    key = cache_key

                if c.exists(key):
                    logging.getLogger().info("Fetching Value from Cache for key: %s" % key)
                    return ast.literal_eval(c.get(key))
                else:
                    logging.getLogger().info("Calculating Value")
                    try:
                        response = f(*args, **kwargs)
                        c.set(key, response, seconds)
                        logging.getLogger().info("Storing Response in Cache for key: %s, value: %s" % (key, response))
                        return response
                    except NoCacheResponse as e:
                        return e.value, e.status_code
                    except ValueError:
                        return {}, 204
            except ConnectionError as e:
                logging.getLogger().error('Redis Connection Error: %s' % e.message)
                return f(*args, **kwargs)
        return wrapper
    return decorated


class NoCacheResponse(Exception):
    def __init__(self, value=None, status_code=None):
        super(NoCacheResponse, self).__init__()
        self.value = value
        self.status_code = status_code


@cache('some_key', 5)
def add(x, y):
    return x + y

