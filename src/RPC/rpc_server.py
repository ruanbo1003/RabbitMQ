
import pika

QUEUE_NAME = 'rpc_queue'


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def on_request(ch, method, props, body):
    n = int(body)

    response = fib(n)

    print(f"props.id:{props.correlation_id}, body:{body}"
          f"response:{response}")

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties = pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=str(response)
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


def rpc_server_test():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue=QUEUE_NAME)

    print(f"rpc server Start RPC request")

    channel.start_consuming()


if __name__ == '__main__':
    rpc_server_test()
