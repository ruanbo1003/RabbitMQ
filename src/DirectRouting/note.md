
#### 一个 productor，两个 worker

productor: 快速的发送 routing_key 分别为 'Error', 'Warning', 'Info' 各 100 个 
 message 到 exchange_name (direct_logs) 中
worker1: 声明 direct 的 log_queue_1，并将 log_queue_1 绑定到 exchange_name 上，
 并绑定 routing_key: Error, Warning, Info
worker2: 声明 direct 的 log_queue_2，并将 log_queue_2 绑定到 exchange_name 上，
 并xepg routing_key: Error

运行结果：
1. worker1 接收到了 100 个 Error, 100 个 Warning，100 个 Info
2. worker2 接收到了 100 个 Error
