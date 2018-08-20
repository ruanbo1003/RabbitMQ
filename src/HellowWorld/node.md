
#### 一个 productor，两个 worker
productor: 快速的发送 100 个 message
worker1: 慢处理，time.sleep(1)
worker2: 快处理, time.sleep(2)

运行结果：
1. RabbitMQ 将 message 平均的分配给两个 worker。
2. RabbitMQ 将接收到的 message 立即发送个 worker。
3. 如果 worker 意外退出，那么未处理的 message 也将丢失。
