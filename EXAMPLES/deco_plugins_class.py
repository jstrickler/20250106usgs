from operator import pow


class calculator:
    OPERATORS = {}

    @classmethod    
    def register_op(cls, op):
        def inner_decorator(orig_function):
            cls.OPERATORS[op] = orig_function
            return orig_function
        return inner_decorator
    
    @classmethod
    def calculate(cls, x, op, y):
        if op in cls.OPERATORS:
            return cls.OPERATORS[op](x, y)
        else:
            raise TypeError(f"Unknown operator {op}")

    @classmethod
    def show_ops(cls):
        for op, function in cls.OPERATORS.items():
            print(f"{op:2} {function.__name__}")

if __name__ == "__main__":
    @calculator.register_op('+')
    def my_add(x, y):
        return x + y
    # or do it with a lot more typing,
    # typing 'my_add' 2 extra times
    # my_add = calculator.register_op('+')(my_add)

    @calculator.register_op('-')
    def my_subtract(x, y):
        return x - y

    @calculator.register_op('*')
    def my_multiply(x, y):
        return x * y

    # decorate existing function from a module
    pow = calculator.register_op('**')(pow)


    print(calculator.calculate(5, '+', 7))
    print(calculator.calculate(100, '-', 72))
    try:
        print(calculator.calculate(3, '*', 14))
    except TypeError as err:
        print(err)
    print(calculator.calculate(2, '**', 5))

    calculator.show_ops()