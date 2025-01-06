def add_hello(old_class):
    def hello_(self):
        print("Hello!")
        
    old_class.hello = hello_
    return old_class

def add_index(old_class):
    old_class.__index__ = lambda self: 42
    return old_class

def add_pow(old_class):
    old_class.__pow__ = lambda self, x:f'I feel {x} times stronger!'
    return old_class

def add_str(old_class):
    old_class.__str__ = lambda self: type(self).__name__.upper()
    return old_class

if __name__ == '__main__':

    @add_hello
    @add_index
    @add_pow
    @add_str
    class Spam:
        pass

    @add_str
    @add_index
    class Ham:
        pass
    
    s = Spam()
    
    s.hello()
    print(int(s))
    print(pow(s, 10))
    print(s)

    h = Ham()
    print(h)
    print(hex(h))
    print(bin(h))
