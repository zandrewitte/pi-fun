from kafka_queue import Consumer
from user import User

cons = Consumer('test2')


def receive(user):
    print user.email
    print user.password

cons.consume_async(receive, User.deserialize)

print 'overhere'