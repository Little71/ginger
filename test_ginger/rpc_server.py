import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.222.81'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n, pre=0, cur=1):
    for i in range(n - 1):
        pre, cur = cur, cur + pre
        if n == 2:
            return cur


def on_request(ch, method, props, body):
    response = fib(int(body))
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id
                     ),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)
channel.start_consuming()
