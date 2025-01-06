from functools import singledispatch

@singledispatch
def add_number(number, list_object):  # define function to be called
    """Add a number to a list, converting from bool, str, bytes, 
    or None if needed

    :param number: number to add
    :type number: Union[int, float, bool, str, bytes, None]
    :param list_object: target of append operation
    :type list_object: list
    """
    source_type = type(number).__name__
    raise TypeError(f"Invalid arg: must be int, float, bool, str, or bytes, not {source_type}")


@add_number.register(int)
@add_number.register(float)
def _(number, list_object): # define handler for numeric types
    list_object.append(number)

@add_number.register(bool)
def _(number, list_object):
    list_object.append(int(number))

@add_number.register(type(None))
def _(number, list_object):
    list_object.append(0)

@add_number.register(str)
@add_number.register(bytes)
def _(number, list_object): # define handler for str and bytes
    if _has_dot(number):
        number_class = float
    else:
        number_class = int
    try:
        f = number_class(number)
    except Exception:
        raise TypeError("Cannot convert '{number}'")
    else:
        list_object.append(f)


def _has_dot(n):
    if isinstance(n, str) and '.' in n:
        return True
    elif isinstance(n, bytes) and b'.' in n:
        return True
    else:
        return False


if __name__ == "__main__":
    print('-' * 60)
    x = [1, 2, 3]
    add_number(10, x)
    add_number(20.0, x)
    add_number(True, x)
    add_number("30", x)
    add_number(b'40', x)
    add_number(None, x)
    print(f"x: {x}")
    
    print(add_number.dispatch(str))  # show handler function for str
    print()

    for arg_type, func in add_number.registry.items():
        # show functions for each registered type
        print(f"{arg_type!s:20} {func}")

    print(f"sum(x): {sum(x)}")  # every element is a number
    