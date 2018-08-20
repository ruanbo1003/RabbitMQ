
import pika
import time


def callback(ch, method, properties, body):
    print("[receive2] get:%r" % body)
    time.sleep(1)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def receive_test():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_consume(
        callback,
        queue='task_queue',
        no_ack=False
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1, all_channels=True)
    channel.start_consuming()


if __name__ == '__main__':
    receive_test()
