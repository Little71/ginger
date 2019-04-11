import time

import pika


def callback(ch, method, properties, body):
    print('~~~ch', ch)  # 管道实例
    print('~~~method', method)  # 方法
    print('~~~properties', properties)  #
    print('~~~body', body)  # 消息内容
    print(body.count(b'.'))
    time.sleep(1)
    # 当消费这处理完后消息后发送确认ack响应
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    print('~~~end')


# 建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.222.81'))

# 创建channel通道
channel = connection.channel()

# 声明一个消息队列，名为hello
# channel.queue_declare(queue='task_queue',durable=True)
result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue

# channel.exchange_declare(exchange='logs', exchange_type='fanout')
# channel.exchange_declare(exchange='direct_logs')
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# channel.queue_bind(exchange='logs',queue=queue_name)

a = ["#","kern.*","*.critical","kern.*" "*.critical",]

for i in a:
    channel.queue_bind(exchange='topic_logs', queue=queue_name,routing_key=f'messages {i}')

# channel.basic_qos(prefetch_count=1)

# 消费者 开始消费 传入队列名称，信息回调函数
channel.basic_consume(queue=queue_name,auto_ack=True, on_message_callback=callback)

# 阻塞的，用来等待消息数据并且在需要的时候运行回调函数的无限循环
channel.start_consuming()

