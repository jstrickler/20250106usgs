MAX_SIZE_MESSAGE = "Maximum size reached"

class MaxList(list):
    def __init__(self, max_size):
        self._max_size = max_size

    def append(self, value):
        if len(self) == self._max_size:
            raise IndexError(MAX_SIZE_MESSAGE)
        else:
            super().append(value)

    def insert(self, index, value):
        if len(self) == self._max_size:
            raise IndexError(MAX_SIZE_MESSAGE)
        else:
            super().insert(index, value)

    def extend(self, values):
        if len(self) + len(values) > self._max_size:
            raise IndexError(MAX_SIZE_MESSAGE)
        else:
            super().extend(values)
