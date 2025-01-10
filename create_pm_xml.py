import lxml.etree as et

FILE_NAME = "DATA/primeministers.txt"

root = et.Element("primeministers")

with open(FILE_NAME) as pm_in:
    for raw_line in pm_in:
        line = raw_line.rstrip() # remove \n
        admin, fname, lname, dob, dod, birthplace, took_office, left_office, party = line.split(':')
        pm_tag = et.SubElement(root, "primeminister")
        if fname.startswith('Sir'):
            title = "Sir"
        else:
            title = "NONE"
        fname_tag = et.SubElement(pm_tag, "firstname", title=title)
        fname_tag.text = fname
        lname_tag = et.SubElement(pm_tag, "lastname").text = lname
        party_tag = et.SubElement(pm_tag, "party").text = party

raw_xml = et.tostring(root, xml_declaration=True, pretty_print=True)
xml_doc = raw_xml.decode()
print(xml_doc)

tree = et.ElementTree(root)
tree.write("prime_ministers.xml", pretty_print=True, xml_declaration=True)
