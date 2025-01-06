class RingList(list):
    def __init__(self, max_size):
        self._max_size = max_size

    def append(self, value):
        if len(self) == self._max_size:
            super().pop(0)
        super().append(value)

    def insert(self, index, value):
        raise TypeError("Insert not allowed")
    
