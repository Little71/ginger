import sys

import pika


def publish(msg):
    # 建立连接
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.222.81'))

    # 创建channel通道
    channel = connection.channel()

    # 声明一个消息队列，名为hello
    # channel.queue_declare(queue='hello',durable=True)
    # channel.queue_declare(queue='task_queue',durable=True)

    # channel.exchange_declare(exchange='logs', exchange_type='fanout')
    # channel.exchange_declare(exchange='direct_logs') #默认是direct 
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


    message = ' '.join(msg) or "Hello World!"

    # 生产者发送消息给队列，交换器为空，路由键是hello，内容是body
    channel.basic_publish(
        exchange='topic_logs',
        routing_key=msg,
        body=message,
        # delivery_mode=2 使用信息持久化
        # properties=pika.BasicProperties(delivery_mode=2),
    )

    # 关闭连接
    connection.close()

a = ["kern.critical", "A critical kernel error"]

for i in a:
    publish(f'messages {i}')
