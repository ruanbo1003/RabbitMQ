
import pika
import time


def callback(ch, method, properties, body):
    print("[worker2] get:%r" % body)


def receive_test():
    exchange_name = 'direct_logs'
    queue_name = 'log_queue_2'
    routing_keys = ['Error']

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type='direct'
    )
    channel.queue_declare(queue=queue_name, durable=True)

    for key in routing_keys:
        channel.queue_bind(
            exchange=exchange_name,
            queue=queue_name,
            routing_key=key
        )

    channel.basic_consume(
        callback,
        queue=queue_name,
        no_ack=True
    )

    print(' [Worker2] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    receive_test()
