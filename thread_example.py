import _thread
import time


def print_epoch(name_of_thread, delay):
    """ Which thread is executed and at which time is executed """
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name_of_thread, "-------------", time.time())


try:
    _thread.start_new_thread(print_epoch, ("thread 1", 1))
    _thread.start_new_thread(print_epoch, ("thread 2", 3))
except:
    print("error")



# threads need some time to be created

# input()

while 1:
    pass
