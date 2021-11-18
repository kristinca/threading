import queue
import time


q = queue.PriorityQueue()

q.put((1, 'Priority 1'))
q.put((3, 'Priority 3'))
q.put((4, 'Priority 4'))
q.put((2, 'Priority 2'))


for i in range(q.qsize()):
    print(q.get()[1])

