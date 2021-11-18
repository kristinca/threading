import threading
import time


def print_epoch(name_of_thread, delay):
    """ Which thread is executed and at which time is executed """
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name_of_thread, "-------------", time.time())


def print_cube(num):
    print("Cube = {}".format(num*num*num))


def print_square(num):
    print("Square = {}".format(num*num))


if __name__ == '__main__':
    t1 = threading.Thread(target=print_cube, args=(2, ))
    t2 = threading.Thread(target=print_square, args=(2, ))

    # start the threads -> the start method
    t1.start()
    t2.start()

    # wait until the threads finish with execution
    t1.join()
    t2.join()

    print('done')
