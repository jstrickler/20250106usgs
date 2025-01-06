import operator as op

class fauxrange:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        self._start = start  # save separately
        self._current_value = start
        self._stop = stop
        self._step = step
        # if step is positive, use greater-than to check that new value 
        # is greater than stop; otherwise use less-than to check that 
        # new value is less than stop
        self._compare_op = op.gt if step >= 0 else op.lt


    def __next__(self):
        # check to see if end of range has been reached
        # using comparison operator selected in __init__()
        if self._compare_op(self._current_value + self._step,self._stop):
            raise StopIteration
            
        value = self._current_value
        self._current_value += self._step
        return value


    def __iter__(self):
        return self


    def __repr__(self):
        return f"fauxrange({self._start}, {self._stop}, {self._step})"
        

if __name__ == "__main__":    
    # example usage
    fr = fauxrange(5)
    print(fr)
    for x in fr:
        print(x)
    print('-' * 10)

    fr = fauxrange(1, 11)
    print(fr)
    for m in fr:
        print(m)
    print('-' * 10)

    fr = fauxrange(5, 101, 5)
    print(fr)
    for d in fr:
        print(d, end=" ")
    print('\n\n')
    print('-' * 10)
    fr = fauxrange(10, 0, -1)
    print(fr)
    print(list(fr))
    print()
    fr = fauxrange(1, 11, 2)
    print(fr)
    print(list(fr))
