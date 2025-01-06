people = [ # list of 4-element tuples
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Brown', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]

def display_person(first_name, last_name, city, state): # function with four parameters
    print(f"{first_name:10} {last_name:10} {city:10} {state}")

display_person("Wanda", "Lefkowitz", "Albany", "NY")  # requires four arguments

for person in people:  # person is a tuple (one element of people list)
    display_person(*person)  # *person unpacks the tuple into four individual arguments
