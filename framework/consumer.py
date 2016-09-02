from kafka_queue import Consumer, TopicSubscribe, subscribe
from user import User


@subscribe('test2', User.deserialize)
def receive(user):
    print user.email
    print user.password


@subscribe('this', User.deserialize)
def receive_another(user):
    print 'Another %s' % str(user)


# Consumer().subscribe(
#     TopicSubscribe('test2', receive_another, User.deserialize),
#     TopicSubscribe('this', receive, User.deserialize)
# )
#
# print 'Overhere'
