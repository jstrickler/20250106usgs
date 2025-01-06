class Incrementer:
    def __init__(self):
        self._value = 0

    def __call__(self):
        self._value += 1

    @property
    def value(self):
        return self._value
    
if __name__ == "__main__":
    inc = Incrementer()
    inc()
    inc()
    inc()
    print(f"inc.value: {inc.value}")
    
