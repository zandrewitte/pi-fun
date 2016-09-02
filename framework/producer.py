from user import User
from kafka_queue import Producer
import time


while True:
    time.sleep(2)
    for i in range(1):
        print 'publish'
        Producer().publish('test2', User('email_%s@mail.com' % i, 'password'), User.serialize)
        Producer().publish('this', User('some_other-%s@mail.com' % i, 'test'), User.serialize)

