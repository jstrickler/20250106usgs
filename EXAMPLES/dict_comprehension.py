import os
from pprint import pprint

FOLDER = "../DATA"

file_names = 'alice.txt', 'parrot.txt', 'words.txt'

file_info = {name: os.path.getsize(os.path.join(FOLDER, name)) for name in file_names}

pprint(file_info)

print('-' * 60)

capitals = {'NY': 'ALBANY', 'NC': 'RALEIGH', 'CA': 'SACRAMENTO', 'VT': 'MONTPELIER'}

caps = {state: capital.title() for state, capital in capitals.items()}
pprint(caps)

