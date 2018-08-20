
#### 一个 productor，两个 worker
productor: 快速的发送 100 个 message 到 exchange_name 中
worker1: 声明 fanout 的 exchange_name，并将 log_queue_1 绑定到 exchange_name 上
worker2: 声明 fanout 的 exchange_name，并将 log_queue_2 绑定到 exchange_name 上

运行结果：
1. woker1 接收到了 100 个 message； worker2 接收到了 100 个 message
2. 如果 woker1、worker2 中的 quene_name 相同，那么 100 个 message 将平均分配到两个 woker 上
