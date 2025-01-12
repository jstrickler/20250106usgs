import typing as T

a: str

def triple(x: int) -> int:
    return x * 3

print(f"{triple(10) = }")
print(f"{triple("abc") = }")
print(f"{triple([1, 2, 3]) = }")
print(f"{triple(9.9) = }")

m: int = triple(5)

r: float = triple(6)


print()

a = "banana"
a = 123
print(f"{a = }")

print(f"{triple.__annotations__ = }")


class MyContainer(list):
    def __getitem__(index):
        return super().__getitem__(index)

def spam(names: T.Iterable) -> None:
    for name in names:
        print(name)

mc = MyContainer()
mc.append('Fred')
mc.append('Leopold')
print(f"{mc = }")

spam(mc)

def toast(x: T.Any) -> None:
    pass

def splat(x: T.Union[int, float]):
    pass
