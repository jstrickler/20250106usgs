from pprint import pprint  # import prettyprint function

# global variables
count = 42  
animal = 'Wombat'

def spam(fruit):  # function parameters are local
    knight = 'Lancelot'  # local variable
    print("Locals:")
    pprint(locals())  # locals() returns dict of all locals
    print()

spam('mango')

# globals() returns dict of all globals
print("Globals:")
pprint(globals())
print()

g = globals()
g['color'] = "blue"  # create a new variable
print("color:", color)
