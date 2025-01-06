class TrimmedFile:
    def __init__(self, file_name):  # constructor is passed file name
        self._file_in = open(file_name)

    def __iter__(self):  
        # An iterator must implement iter(), which must return an iterator. 
        # Typically it returns 'self', as the generator IS the iterator
        return self

    def __next__(self):  # next() returns the next value of the iterator
        line = self._file_in.readline()
        if line == '':
            raise StopIteration  # Raise StopIteration when there are no more values to generate
        else:
            return line.rstrip('\n\r')  # The actual work of this iterator -- remove the end-of-line char(s)


if __name__ == '__main__':
    # To use the iterator, create an instance and iterate over it.
    trimmed = TrimmedFile('../DATA/mary.txt')  
    for line in trimmed:
        print(line)
