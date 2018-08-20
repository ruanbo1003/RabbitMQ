
import pika
import time


def send_test():
    parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    for i in range(1, 101):
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=f'Hello World [{i}]',
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )

    print("send over")
    time.sleep(5)
    print("sender close the connection")

    connection.close()


if __name__ == '__main__':
    send_test()
