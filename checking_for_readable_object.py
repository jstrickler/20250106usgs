
class Foo:
    def __init__(self):
        self.color = "green"

    def read(self):
        return "wombat"

class Bar:
    pass

f = Foo()
b = Bar()

print(f"{hasattr(f, 'read') = }")
print(f"{hasattr(b, 'read') = }")

if hasattr(f, 'read'):
    result = f.read()
else:
    raise TypeError(f"Sorry, {type(f).__name__} objects are not readable")

if hasattr(b, 'read'):
    result = b.read()
else:
    print(f"Sorry, {type(b).__name__} objects are not readable")

read_function = getattr(f, 'read')
print(f"{read_function() = }\n")
print(f"{getattr(f, 'color') = }\n")

def scream(self):
    print("AIIIEEEEEEEEEEEEE")

setattr(Foo, 'scream', scream)

f.scream()


class Toast():
    def __call__(self):
        return "abc"

t = Toast()
result = t()
print(f"{result = }")
