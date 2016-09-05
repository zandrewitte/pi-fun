from user import User
from event import Event
from kafka_queue import Producer
import time
import uuid
import ast


while True:
    for i in range(1):

        eventHeader = {
            'requestUUID': str(uuid.uuid4()),
            'eventType': 'SavedEvent',
            'someField': 'SomeValue'
        }

        eventMeta = {
            'userUUID': str(uuid.uuid4()),
            'someMeta': 'SomeMetaValue'
        }

        eventPayload = {
            'eventName': 'This Event %s' % i,
            'location': 'Some Location %s' % i,
            'Teams': {
                'Team1UUID': str(uuid.uuid4()),
                'Team2UUID': str(uuid.uuid4())
            }
        }

        Producer().publish('ppro.incoming.event', Event(eventHeader, eventMeta, eventPayload),
                           Event.serialize)
        # Producer().publish('topic3', User('some_other-%s@mail.com' % i, 'test'), User.serialize)

        time.sleep(5)

