from random import randint
import pandas as pd 
import openpyxl as px

NUM_WORKSHEETS = 100
MAX_ROWS = 3

def get_ints(length):
    return [randint(0,100) for _ in range(length)]

for i in range(1, NUM_WORKSHEETS + 1)


if __name__ == "__main__":
    print(get_ints(10))