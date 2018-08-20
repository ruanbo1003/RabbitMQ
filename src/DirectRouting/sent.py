
import pika
import time


def send_test():
    parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    exchange_name = 'direct_logs'
    routing_keys = ['Error', 'Warning', 'Info']

    for i in range(1, 101):
        for key in routing_keys:
            channel.basic_publish(
                exchange=exchange_name,
                routing_key=key,
                body=f'{key} message [{i}]',
            )

    print("send over")
    time.sleep(5)
    print("sender close the connection")

    connection.close()


if __name__ == '__main__':
    send_test()
