from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import ConnectionError
from singleton import Singleton
import ast
from pathos.multiprocessing import ProcessingPool as Pool
import threading


class Producer(object):
    __metaclass__ = Singleton

    def __init__(self):
        print 'Running Init'
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9090', 'localhost:9091', 'localhost:9092'])

    def publish(self, topic, obj, serializing_func, key=None, partition=None):
        self.producer.send(topic, str(serializing_func(obj)), key, partition)


class Consumer(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.consumer = KafkaConsumer(bootstrap_servers=['localhost:9090', 'localhost:9091', 'localhost:9092'],
                                      value_deserializer=self.message_serializer
                                      )
        self.function_set = {}
        self.pool = Pool(8)
        self.consumeThread = threading.Thread(target=self.consume_async)

    def add_subscription(self, topic_subscribe):
        if self.consumer.subscription() is not None:
            self.consumer.subscribe(list(self.consumer.subscription() | {topic_subscribe.topic}))
        else:
            self.consumer.subscribe([topic_subscribe.topic])
        self.function_set[topic_subscribe.topic] = topic_subscribe
        if not self.consumeThread.isAlive():
            self.consumeThread.start()

    def subscribe(self, *topic_subscribes):
        topics = list(map(lambda t_sub: t_sub.topic, topic_subscribes))
        self.consumer.subscribe(topics)
        self.function_set = dict(zip(topics, topic_subscribes))
        if not self.consumeThread.isAlive():
            self.consumeThread.start()

    @staticmethod
    def message_serializer(message):
        try:
            return ast.literal_eval(message)
        except Exception as e:
            print 'Error While Serializing Message (%s). Reason : %s' % (message, e.message)

    def consume_async(self):
        for message in self.consumer:
            self.pool.pipe(self.handle_message, self.function_set, message)

    def consume_sync(self):
        for message in self.consumer:
            self.handle_message(self.function_set, message)

    @staticmethod
    def handle_message(function_set, message):
        print 'Received Message on Topic: %s, Payload: %s' % (message.topic, message.value)
        try:
            _ = function_set[message.topic]
            if message.value is not None:
                _.handle_function(_.serializing_function(message.value))
        except Exception as e:
            print 'Error While Executing consumer function with Message (%s). Reason : %s' % (message, e.message)


class TopicSubscribe(object):
    def __init__(self, topic, handle_function, serializing_function):
        self.topic = topic
        self.handle_function = handle_function
        self.serializing_function = serializing_function


def subscribe(topic, serializing_function):
    def decorated(f):
        try:
            c = Consumer()
            c.add_subscription(TopicSubscribe(topic, f, serializing_function))

        except ConnectionError as e:
            print 'Kafka Connection Error: %s' % e.message
    return decorated
