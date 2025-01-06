CONFIG_FILE_PATH = "../DATA/sample.cfg"

g = globals()  # get access to dictionary of global names

with open(CONFIG_FILE_PATH) as config_in:
    for raw_line in config_in:
        line = raw_line.rstrip()
        name, value = line.split('=')
        g[name] = value  # create a new global variable

print(animal, color, detective, language)