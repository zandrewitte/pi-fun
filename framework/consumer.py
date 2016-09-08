from kafka_queue import Consumer, TopicSubscribe, subscribe
from user import User
from event import Event
from topics import Topics


@subscribe(Topics.Topic.test, User.deserialize)
def receive(user):
    print user.email
    print user.password
    print user.uuid


@subscribe(Topics.PlayerPro.Incoming.Event, Event.deserialize)
def consume_event(event):
    print 'requestUUID : %s \n' % event.header.get("requestUUID")
    print 'userUUID : %s \n' % event.meta.get("userUUID")
    for element in event.payload.get('body'):
        print element.get('id')


# @subscribe('topic2', User.deserialize)
# def receive_another(user):
#     print 'Another %s' % str(user)


# Consumer().subscribe(
#     TopicSubscribe('test2', receive_another, User.deserialize),
#     TopicSubscribe('this', receive, User.deserialize)
# )
#
# print 'Overhere'
