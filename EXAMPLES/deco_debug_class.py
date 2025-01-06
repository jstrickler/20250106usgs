
class debugger():  # class implementing decorator

    function_calls = []

    def __init__(self, func):  # original function passed into decorator's constructor
        self._func = func

    def __call__(self, *args, **kwargs):  # __call__() is replacement function


        result = self._func(*args, **kwargs)  # call the original function

        self.function_calls.append(  # add function name and arguments to saved list
            (self._func.__name__, args, kwargs, result)
        )

        return result  # return result of calling original function

    @classmethod
    def get_calls(cls): # define method to get saved function call information
        return cls.function_calls


@debugger  # apply debugger to function
def hello(greeting, whom="world"):
    print(f"{greeting}, {whom}")
    return greeting


@debugger  # apply debugger to function
def bark(bark_word, *, repeat=2):
    print(f"{bark_word * repeat}! ")
    return bark_word


hello('hello', 'world')  # call replacement function
print()

hello('hi', 'Earth')
print()

hello('greetings')

bark("woof", repeat=3)
bark("yip", repeat=4)
bark("arf")

hello('hey', 'you')

print('-' * 60)

for i, info in enumerate(debugger.get_calls(), 1):  # display function call info from class
    print(f"{i:2d}. {info[0]:10s} {info[1]!s:20s} {info[2]!s:20s} {info[3]!s}")
