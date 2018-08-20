
import pika
import time


def send_test():
    parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    exchange_name = 'logs'

    for i in range(1, 101):
        channel.basic_publish(
            exchange=exchange_name,
            routing_key='',
            body=f'Hello World [{i}]',
        )

    print("send over")
    time.sleep(5)
    print("sender close the connection")

    connection.close()


if __name__ == '__main__':
    send_test()
