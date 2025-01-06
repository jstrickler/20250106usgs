# deco without params
from enum import Enum, auto
import types

class BiteLevel(Enum):
    mild = auto()
    medium = auto()
    severe = auto()

BITE_METHOD_NAME = "bite"

class EnsureBite:
    def __init__(self, bite_level) -> None:
        self._bite_level = bite_level
        
    def __call__(self, original_class):
        
        if not hasattr(original_class, BITE_METHOD_NAME):
            def _(orig_self):
                print(f"Biting... (level {self._bite_level})")

            setattr(original_class,
                    BITE_METHOD_NAME, 
                    types.MethodType(_, original_class))

        return original_class

@EnsureBite(BiteLevel.mild)
class Dog:  # Dog = EnsureBite(BiteLevel)(Dog)
    pass

d = Dog()

d.bite()

@EnsureBite(BiteLevel.severe)
class Pooch:  # Pooch = EnsureBite(bitelevel)(Pooch)
    def bite(self):
        print(f"Biting... (level {BiteLevel.medium})")

p = Pooch()
p.bite()

