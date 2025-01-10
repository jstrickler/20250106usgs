from datetime import datetime
from functools import wraps

# the decorator
def timestamp(func):

    @wraps(func)
    def wrapper(*args, **kwargs): # the replacement function
        print(datetime.now().ctime())
        return func(*args, **kwargs)  # call the original function

    return wrapper

@timestamp
def spam(repeat_count):  # spam turns into cheese
    print("SPAM!!" * repeat_count)
# spam = doit(spam)

@timestamp
def ham():
    print("HAM!")

spam(1)
ham()
spam(3)
spam(5)
print(f"{spam.__name__ = }")
print(f"{ham.__name__ = }")
