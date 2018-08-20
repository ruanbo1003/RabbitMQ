
import pika
import time


def callback(ch, method, properties, body):
    print("[receive] get:%r" % body)


def receive_test():
    exchange_name = 'logs'
    queue_name = 'log_queue_2'

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type='fanout'
    )
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(exchange=exchange_name, queue=queue_name)

    channel.basic_consume(
        callback,
        queue=queue_name,
        no_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    receive_test()
