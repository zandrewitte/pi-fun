from user import User
from kafka_queue import Producer
import time


while True:
    time.sleep(5)
    for i in range(1):
        print 'publish'
        Producer().publish('topic3', User('email_%s@mail.com' % i, 'password'), User.serialize)
        # Producer().publish('topic2', User('some_other-%s@mail.com' % i, 'test'), User.serialize)

