#!/usr/bin/python 
# -*- coding: utf-8 -*-  
import random,time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass
    
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
#绑定端口5000,设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey='abc')
manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()
#放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
manager.shutdown()

#The program can not run under Windows