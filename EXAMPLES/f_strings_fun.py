# fun with strings
name = "Guido"

print(f"name: {name}")
# < left justify (default for non-numbers), 10 is field width, s formats a string
print(f"name: [{name:<10s}]") 
# > right justify
print(f"name: [{name:>10s}]")
# >. right justify and pad with dots
print(f"name: [{name:.>10s}]")
# ^ center
print(f"name: [{name:^10s}]")
# ^ center and pad with dashes
print(f"name: [{name:-^10s}]")
print()

# fun with integers
value = 2093
print(f"value: {value}")
print(f"value: [{value:10d}]")  # pad with spaces to width 10
print(f"value: [{value:010d}]")  # pad with zeroes to width 10
print(f"value: {value:d} {value:b} {value:x} {value:o}")  # d is decimal, b is binary, o is octal, x is hex
print(f"value: {value} {value:#b} {value:#x} {value:#o}")  # add prefixes
print()

result = 38293892
print(f"result: ${result:,d}")  # , adds commas to numeric value
print()

# fun with floats
amount = .325482039
print(f"amount: {amount}")
print(f"amount: {amount:.2f}")  # round to 2 decimal places
print(f"amount: {amount:.2%}")  # convert to percent
print()

# fun with functions
print(f"length of 'name': {len(name)}")  # function call OK
