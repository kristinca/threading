import threading
import time


def print_epoch(name_of_thread, delay):
    """ Which thread is executed and at which time is executed """
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name_of_thread, "-------------", time.time())


class MyThread(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)

        self.name = name
        self. delay = delay

    def run(self):
        print("start thread: ",self.name)
        print_epoch(self.name, self.delay)
        print("end thread: ", self.name)


if __name__ == '__main__':
    # thread 1 will be executed faster than thread 2 because of the delay !
    t1 = MyThread("Thread 1", 1)
    t2 = MyThread("Thread 2", 2)

    t1.start()
    t2.start()

    #
    print(t1.getName())
    print(t2.getName())

    # returns the number of threads inside this program
    print(threading.active_count())

    # print the current thread which is active atm
    print(threading.current_thread())

    # enumerate the number of active threads
    print(threading.enumerate())


    t1.join()
    t2.join()

    print("done")