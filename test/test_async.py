from threading import Thread
from time import sleep


def async_call(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


@async_call
def A():
    sleep(10)
    print("a function")


def B():
    print("b function")
    A()


A()
B()
