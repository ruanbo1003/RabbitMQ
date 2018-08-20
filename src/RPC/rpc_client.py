
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.QUEUE_NAME = 'rpc_queue'
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()

        self.callback_queue = 'rpc_callback_queue'
        self.channel.queue_declare(queue=self.callback_queue)
        self.channel.basic_consume(
            self.on_response,
            no_ack=True,
            queue=self.callback_queue
        )

        self.response = ''
        self.corr_id = ''

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange='',
            routing_key=self.QUEUE_NAME,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            ),
            body=str(n)
        )

        while self.response is None:
            self.connection.process_data_events()

        return self.response


fibonacci_rpc = FibonacciRpcClient()


for i in range(10):
    ret = fibonacci_rpc.call(i)

    print(f"fib[{i}] = {ret}")
