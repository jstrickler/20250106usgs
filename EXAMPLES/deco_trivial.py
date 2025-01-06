def void(thing_being_decorated):
    return 42  # replace function with 42

name = "Guido"
x = void(name)  # decorate 'name', which is now 42, not a string

@void  # decorate hello() function
def hello():
    print("Hello, world")

@void  # decorate howdy() function
def howdy():
    print("Howdy, world")

print(hello, type(hello)) # hello is now the integer 42, not a function
print(howdy, type(howdy)) # howdy is now the integer 42, not a function
print(x, type(x))
