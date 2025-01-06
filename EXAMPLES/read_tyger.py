with open("../DATA/tyger.txt", "r") as tyger_in:  # tyger_in is return value of open()
    for raw_line in tyger_in:  # tyger_in is iterable of lines in the file
        line = raw_line.rstrip()  # remove \n
        print(line)
