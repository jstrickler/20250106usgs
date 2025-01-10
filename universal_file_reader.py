from ufr import Reader, register_reader

@register_reader("csv")
def read_csv():
    pass

@register_reader("yaml")
def read_yaml():
    pass

# register_reader(read_yaml, "yaml")

r = Reader("file_name")
data = r.read()