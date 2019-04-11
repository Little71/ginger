from celery import Celery

app = Celery('tasks',broker='redis://:1q2w3e4r@192.168.222.81:6379/0')


@app.task
def add(x,y):
    print(f'~~~~{x*y}')
    return x*y

