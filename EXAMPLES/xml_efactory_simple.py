#
import lxml.etree as ET
from lxml.builder import E  # import E object

animal_list = [
    ('wombat', "Vombatus ursinus"),
    ('bushbaby', "Galago senegalensis"),
    ('dog', 'Canis domesticus'),
]

xml = (
    E.animals(  # use E to create nested tags
        *[E.animal(name, species=species) for name, species in animal_list]
    )
)

print(ET.tostring(xml, pretty_print=True).decode())
