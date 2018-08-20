
import pika
import time


QUEUE_NAME = "auth_test_queue"


def callback(ch, method, properties, body):
    print("[receive] get:%r" % body)
    time.sleep(1)


def receive_test():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672)
    )
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_consume(callback,
                          queue=QUEUE_NAME,
                          no_ack=True)

    print(' [Auth Worker1] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    receive_test()
