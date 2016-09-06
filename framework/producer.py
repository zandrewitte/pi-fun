from user import User
from event import Event
from kafka_queue import Producer
import time
import uuid


while True:
    for i in range(250):

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
            "description": "test",
            "privacy": "public",
            "eventType": "Pickup",
            "rsvps": {
                "missing": 0,
                "maybe": 0,
                "invited": 0,
                "going": 0,
                "declined": 0
            },
            "venue": {
                "id": 473,
                "city": "",
                "fields": [
                    {
                        "name": "Tokyo, Japan",
                        "id": 487
                    }
                ],
                "name": "Tokyo, Japan",
                "address": "Tokyo, Japan"
            },
            "field": {
                "name": "Tokyo, Japan",
                "id": 487
            },
            "title": "Test",
            "date": "2015-10-22T17:38:00Z",
            "isManager": False,
            "id": 235
        }

        Producer().publish('ppro.incoming.event', Event(eventHeader, eventMeta, eventPayload),
                           Event.serialize)
        # Producer().publish('topic3', User('some_other-%s@mail.com' % i, 'test'), User.serialize)

