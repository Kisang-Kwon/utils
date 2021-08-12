import time


def get_time(text='', enter=False):
    if enter:
        return time.strftime(text + '%x %X\n', time.localtime(time.time()))
    else:
        return time.strftime(text + '%x %X', time.localtime(time.time()))