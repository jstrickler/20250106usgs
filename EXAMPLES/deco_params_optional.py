from functools import wraps, partial
from datetime import datetime

def logger(func=None, **kwargs):
    if func:
        verbose = kwargs.get('verbose_time')
        @wraps(func)
        def _(*func_args, **func_kwargs):
            if verbose:
                print(f"function {func.__name__}() called at {datetime.now().ctime()}")
            else:
                print(f"{func.__name__}:{datetime.now().strftime('%x%X')}")
            return func(*func_args, **func_kwargs)
        return _
    else:
        return partial(logger, **kwargs)


@logger    # spam = logger(spam)
def spam():
    print("SPAM")

@logger(verbose_time=True)  # ham = logger(verbose_time=True)(ham)
def ham():
    print("HAM")

@logger()  # toast = logger()(toast)
def toast():
    print("TOAST")

@logger(verbose_time=False)  # eggs = logger(verbose_time=False)(eggs)
def eggs():
    print("EGGS")

spam()
print('-' * 60)
ham()
print('-' * 60)
toast()
print('-' * 60)
eggs()