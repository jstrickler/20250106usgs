OPERATORS = {}

def register_op(op):
    def inner_decorator(orig_function):
        OPERATORS[op] = orig_function
        return orig_function
    return inner_decorator

@register_op('+')
def add(x, y):
    return x + y

@register_op('-')
def subtract(x, y):
    return x - y

def calculate(x, op, y):
    if op in OPERATORS:
        return OPERATORS[op](x, y)
    else:
        print(f"Unknown operator {op}")

if __name__ == "__main__":
    print(calculate(5, '+', 7))