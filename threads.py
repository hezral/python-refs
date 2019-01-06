from threading import Event, Thread

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

def somefunc(text):
    print(text)
    print("hahaha")

cancel_future_calls = call_repeatedly(5, somefunc, "Hello, World")

print("somethingelse")

cancel_future_calls() # stop future calls