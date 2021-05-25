# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:26:21 2021

@author: tamil
"""
def bank_queue():
    queue_length = 0
    
    def queue_len():
        print(queue_length)
    
    def enqueue():
        nonlocal queue_length
        queue_length +=1
    
    def dequeue():
        nonlocal queue_length
        queue_length +=-1
    
    return (queue_len, enqueue, dequeue)


queue_len_func, enqueue_func, dequeue_func = bank_queue()

queue_len_func()
enqueue_func()
enqueue_func()
enqueue_func()
queue_len_func()
dequeue_func()
dequeue_func()
queue_len_func()
enqueue_func()
enqueue_func()
queue_len_func()
dequeue_func()
queue_len_func()