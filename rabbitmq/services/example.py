import pika
from config import settings


class RabbitMQExample:
    _instance = None
    _initialized = False
    _queue = 'example'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RabbitMQExample, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self.__class__._initialized:
            return
        self.__class__._initialized = True

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.RABITMQ_HOST, port=settings.RABITMQ_PORT)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self._queue)

    async def worker(self) -> None:
        def callback(ch, method, properties, body):
            ch.basic_ack(delivery_tag=method.delivery_tag)

        while True:
            self.channel.basic_consume(queue=self._queue, on_message_callback=callback, auto_ack=True)
            self.channel.start_consuming()

    async def send(self, message) -> None:
        self.channel.basic_publish(exchange='', routing_key=self._queue, body=message)

    async def close_rabbitmq(self) -> None:
        self.connection.close()
