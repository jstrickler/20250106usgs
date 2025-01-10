def annoy_cat(times: int | None) -> str:
    # This line generates the mypy output:
    # 'note: Right operand is of type "int | None"'
    return 'meow' * times

print(f"{annoy_cat(3) = }")

def print_times(phrase: str, times: int | None = None) -> None:
    """print the phrase some number of times, unless the number is not specified
    """
    if times is None:
        print(phrase)
    else:
        print(phrase * times)

print_times("spam", 5)
print_times("toast")