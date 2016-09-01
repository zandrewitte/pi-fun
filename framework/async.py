from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
from tornado.simple_httpclient import SimpleAsyncHTTPClient
import urllib
from tornado.ioloop import IOLoop


def handle_response(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body


@gen.coroutine
def fetch_async(url):
    http_client = AsyncHTTPClient(IOLoop.current())
    response = yield http_client.fetch(url, handle_response, method='GET', headers=None)
    raise gen.Return(response.body)

#
# fetch_async('http://www.google.com')
#
# IOLoop.instance().start()
