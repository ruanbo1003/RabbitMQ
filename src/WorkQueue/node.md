
#### 一个 productor，两个 worker
productor: 快速的发送 100 个 message
worker1: 慢处理，time.sleep(1)
worker2: 快处理, time.sleep(2)

运行结果：
1. basic_consume() 时，指定 no_ack = False, 那么 RabbitMQ 在将 message
 发送给 consumer 后，会等待 consumer 的 ack，之一才会将 message 删除。
 要记得，在 consumer 处理完 message 后，要 ack，ch.basic_ack(delivery_tag=method.delivery_tag)；
 否则到导致 RabbitMQ 存储的 message 一直增加。
2. channel.basic_qos(prefetch_count=1, all_channels=True)。
 一次只发送一个 message 到 consumer，配合 ack 使用，RabbitMQ 只能等到上
 一个 message 处理完成后的 ack，才会发送下一个 message 到这个 consumer。
3. 有了 2 的设置，所有的 message 就不会平均的分配给 consumer，而是一次只发送
 一个 message 到 consumer，等待处理完成，哪个 consumer 将处理完成，就先接收到
 下一个 message。 上面的 worker1、worker2：worker2 处理的 message 数量是
 worker1 的两倍。
4. queue_declare() 时，可以指定 durable = True，表示将 message 持久化； 这样，即使 RabbitMQ 在
 中途挂机，也不会丢失 message。
5. 另 pika 0.12.0 版本，还是平均分配给每个 consumer，而 0.11.0 版本是正常的。
