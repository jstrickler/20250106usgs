"""
Temperature conversion functions

Usage:
c_temp = c2f(f_temp)
f_temp = f2c(c_temp)
"""
import sys


def c2f(cel: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit

    :param cel: Celsius temperature as int or float
    :return: Fahrenheit temperature as float
    """
    cel = float(cel)
    f = (9/5 * cel) + 32

    return round(f, 3)


def f2c(fahr: float) -> float:
    """
    Convert Fahrenheit temperature to Celsius

    :param fahr: Fahrenheit temperature as int or float
    :return: Celsius temperature as float
    """
    fahr = float(fahr)
    c = (fahr - 32) * (5/9)

    return round(c, 3)


if __name__ == '__main__':
    # informal testing
    for ctemp in 100, 0.0, 212.1, -40:
        ftemp = c2f(ctemp)
        print(f"{ctemp:6.2f}\u00B0 C is {ftemp:6.2f}\u00B0 F")


