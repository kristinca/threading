import threading


x = 0

def thread_task(lock1):
    global x
    for i in range(1000000):
        lock1.acquire()
        x += 1
        lock1.release()


def main_task():
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock, ))
    t2 = threading.Thread(target=thread_task, args=(lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main_task()
    print("{0}".format(x))