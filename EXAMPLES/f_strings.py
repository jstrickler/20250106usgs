city = 'Orlando'
temperature = 85
hit_count = 5
average = 3.4563892382

# variables inserted into string
print(f"It is {temperature}\u00B0 in {city}")
print()

# :03d means format (decimal) integer in 3 characters, 
#      left-padded with zeros
# :.2f means round a float to 2 decimal points
print(f"hit count is {hit_count:03d} average is {average:.2f}")
print()

# any expression is OK
print(f"2 + 2 is {2 + 2}")

