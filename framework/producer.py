from event import Event, Request, Payload
from kafka_queue import Producer
import time
from datetime import datetime
from topics import Topics
import ast


while True:
    for i in range(1):

        event = Event('corID:%s' % i, 'create', 'some_resource', datetime.now().isoformat(), 'some_source', Payload({
                  'field_e_1': 'value_e_1',
                  'field_e_2': 'value_e_2',
                  'field_e_3': 'value_e_3'
              }, {
                  'field_d_1': 'value_d_1',
                  'field_d_2': 'value_d_2',
                  'field_d_3': 'value_d_3'
              }),
              Request('POST', 'some_path', {
                'etag': 'some_etag',
                'content-type': 'application/json',
                'content-length': '123',
                'user-agent': 'some_user_agent',
                'host': '127.0.0.1'
              }, 'someparam=somevalue',
              {
                'remoteAddress': 'some_remote_address'
              }))

        Producer().publish(Topics.PlayerPro.Incoming.Event, event, Event.serialize)
        # Producer().publish('topic3', User('some_other-%s@mail.com' % i, 'test'), User.serialize)
        # time.sleep(2)
