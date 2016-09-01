from kafka import KafkaConsumer
from kafka import KafkaProducer
from singleton import Singleton
import ast
# from multiprocessing import Pool
from pathos.multiprocessing import ProcessingPool as Pool


class Producer(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def publish(self, topic, obj, serializing_func, key=None, partition=None):
        self.producer.send(topic, str(serializing_func(obj)), key, partition)


class Consumer(object):
    # __metaclass__ = Singleton

    def __init__(self, *topics):
        self.consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                      value_deserializer=self.message_serializer
                                      )
        self.consumer.subscribe(list(topics))
        self.pool = Pool(8)

    @staticmethod
    def message_serializer(message):
        try:
            return ast.literal_eval(message)
        except Exception as e:
            print 'Error While Serializing Message (%s). Reason : %s' % (message, e.message)

    def consume_async(self, f, serialize_func):
        for message in self.consumer:
            self.pool.pipe(self.handle_message, message, f, serialize_func)

    @staticmethod
    def handle_message(message, f, serialize_func):
        print 'Received Message on Topic: %s, Payload: %s' % (message.topic, message.value)
        try:
            if message.value is not None:
                f(serialize_func(message.value))
        except Exception as e:
            print 'Error While Executing consumer function with Message (%s). Reason : %s' % (message, e.message)

    def consume_sync(self, f, serialize_func):
        for message in self.consumer:
            print 'Received Message on Topic: %s, Payload: %s' % (message.topic, message.value)
            try:
                if message.value is not None:
                    f(serialize_func(message.value))
            except Exception as e:
                print 'Error While Executing consumer function with Message (%s). Reason : %s' % (message, e.message)
