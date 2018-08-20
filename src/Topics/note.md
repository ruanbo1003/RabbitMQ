
#### topic 模式：一个 productor，三个 worker

productor: 快速的发送 routing_key 分别为 'auth.Error', 'auth.info', 
 'kernel.Error', 'kernel.info' 各 100 个 message 到 exchange_name
  (topic_log_exchange) 中
  
worker1: 绑定 'kernel.*'
worker2: 绑定 '*.Error'
worekr3: 绑定 '#'
 
运行结果：
1. worker1: 接收到 kernel.Error、kernel.info 各 100 个
2. worker2: 接收到 auth.Error、kernel.Error 各 100 个
3. worker3: 接收到 auth.Error、auth.info、kernel.Error、kernel.info 各 100 个
