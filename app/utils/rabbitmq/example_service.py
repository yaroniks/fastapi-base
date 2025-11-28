import json
import pika
from config import settings


class RabbitMQExample:
    _instance = None
    _initialized = False
    _queue = 'example'  # ТУТ НАЗВАНИЕ ОЧЕРЕДИ

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

    def worker(self) -> None:
        def callback(ch, method, properties, body):  # ТУТ МЫ ПОЛУЧАЕМ ЗАПРОС И ОБРАБАТЫВАЕМ ЕГО
            body = json.loads(body)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        while True:
            self.channel.basic_consume(queue=self._queue, on_message_callback=callback)
            self.channel.start_consuming()

    def send(self, message) -> None:  # ТУТ МЫ ОТПРАВЛЯЕМ ЗАПРОС
        self.channel.basic_publish(exchange='', routing_key=self._queue, body=message)  # json.dumps(message)

    def close_rabbitmq(self) -> None:
        self.connection.close()
