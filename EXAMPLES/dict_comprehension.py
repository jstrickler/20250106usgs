import os
from pprint import pprint

FOLDER = "../DATA"

file_names = 'alice.txt', 'parrot.txt', 'words.txt'

#      {k:v for x in ITERABLE if CONDITION}
file_info = {name: os.path.getsize(os.path.join(FOLDER, name)) for name in file_names}

pprint(file_info)

print('-' * 60)

capitals = {'NY': 'ALBANY', 'NC': 'RALEIGH', 'CA': 'SACRAMENTO', 'VT': 'MONTPELIER'}

caps = {state: capital.title() for state, capital in capitals.items() if state.startswith('N')}
pprint(caps)

colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'RED', 'Red', 'red', 'red', 'Brown', 'GREEN', 'green', 'BLACK', 'Pink', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

unique_colors = {c.lower() for c in colors}
print(f"{unique_colors = }\n")
