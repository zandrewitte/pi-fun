from kafka_queue import Consumer, TopicSubscribe, subscribe
from user import User
from event import Event


@subscribe('topic3', User.deserialize)
def receive(user):
    print user.email
    print user.password
    print user.uuid


@subscribe('ppro.incoming.event', Event.deserialize)
def consume_event(event):
    print event.header.get("requestUUID")
    print event.meta
    print event.payload


# @subscribe('topic2', User.deserialize)
# def receive_another(user):
#     print 'Another %s' % str(user)


# Consumer().subscribe(
#     TopicSubscribe('test2', receive_another, User.deserialize),
#     TopicSubscribe('this', receive, User.deserialize)
# )
#
# print 'Overhere'
