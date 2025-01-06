"""
    Provide the EnsureWag decorator
"""
WAG_METHOD_NAME = "wag"

class EnsureWag:
    """
    A decorator that ensures that a class contains at least a default wag() 
    """
    def __new__(cls, original_class):
        if not hasattr(original_class, WAG_METHOD_NAME):
            def _(self):
                print("wagging")
            setattr(original_class, WAG_METHOD_NAME, _)
        
        return original_class
              
@EnsureWag
class Dog:  # Dog = EnsureWag(Dog)
    pass

d = Dog()
d.wag()

@EnsureWag
class Pooch:
    def wag(self):
        print("wagging enthusiastically")

p = Pooch()
p.wag()
