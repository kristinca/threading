import queue
import threading
import time


def putting_thread(q1):
    while True:
        print('starting thread')
        # putting an item every 10 seconds
        time.sleep(10)
        q1.put(5)
        print('put something')


q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q, ), daemon=True)
t.start()

v = q.put(5)


# print(q.get())

print('first item gotten')

print(q.get())

print('finished')
# print(q.empty())


# FIFO

# for i in range(5):
#     q.put(i)
#
# while not q.empty():
#     print(q.get(), end = ' ')
#
