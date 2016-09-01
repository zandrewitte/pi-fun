from user import User
from kafka_queue import Producer
import time


prod = Producer()

while True:
    time.sleep(2)
    for i in range(25):
        prod.publish('test2', User('email_%s@mail.com' % i, 'password'), User.serialize)

