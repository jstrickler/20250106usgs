"""
Example of decorator implemented as class, decorating class, with no parameters

This is a callable class, that returns the actual decorator.

Syntax:

ensure_bark = EnsureBark()

@ensure_bark  # calling instance 
def FUNC():
    pass
"""

BARK_METHOD_NAME = "bark"
class EnsureBark:
        
    def __call__(self, original_class):
        if not hasattr(original_class, BARK_METHOD_NAME):
            def _(self):
                print("woof woof")

            setattr(original_class, BARK_METHOD_NAME, _)
        return original_class

eb = EnsureBark()

@eb
class Dog():  # Dog = Bark()(Dog)
    pass

d = Dog()
d.bark()

@eb
class Pooch():
    def bark(self):
        print("ruff ruff")

p = Pooch()
p.bark()
