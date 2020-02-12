# coding: utf-8

import _thread as thread
import time


class callback_allowed_function():
    def __init__(self, fn):
        self.fn = fn
        pass

    def __getattr__(self, item):
        return getattr(self.fn, item)

    def __setattr__(self, key, value):
        return setattr(self.fn, key, value)


def allow_callback(function):
    return callback_allowed_function(function)


def bind_callback(do_function):
    if not isinstance(do_function, callback_allowed_function):
        raise ValueError("callback is not allowed on this function.")

    do_function: callback_allowed_function

    def deco(f):
        def compiled_function(*args, **kwargs):
            start_time = time.time()
            result = do_function.fn(*args, **kwargs)
            end_time = time.time()
            thread.start_new_thread(f, (), {
                "start_time": start_time,
                "end_time": end_time
            })
            return result

        return compiled_function


def callback_demo(start_time, end_time):
    pass
