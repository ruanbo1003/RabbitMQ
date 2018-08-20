
import pika
import time


def callback(ch, method, properties, body):
    print("[worker2] get:%r" % body)


# all routing keys: ['auth.Error', 'auth.Info', 'kernel.Error', 'kernel.Info']
def receive_test():
    exchange_name = 'topic_log_exchange'
    queue_name = 'topic_log_queue_2'
    bind_routing_key = '*.Error'

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type='topic'
    )
    channel.queue_declare(queue=queue_name, durable=True)

    channel.queue_bind(
        exchange=exchange_name,
        queue=queue_name,
        routing_key=bind_routing_key
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
