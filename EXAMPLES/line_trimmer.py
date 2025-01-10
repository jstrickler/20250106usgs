def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object
            # next() runs function to the 'yield' line 

mary_in = trimmed('../DATA/mary.txt')
print(f"{type(mary_in) = }")
print(f"{dir(mary_in) = }\n")

for trimmed_line in mary_in:
    print(trimmed_line)
