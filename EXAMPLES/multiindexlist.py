
class MultiIndexList(list):  # Define new class that inherits from list

    def __getitem__(self, item):  # Redefine __getitem__ which implements []
        if isinstance(item, tuple):  # Check to see if index is tuple
            if len(item) == 0:
                raise ValueError("Tuple must be non-empty")
            else:
                tmp_list = []
                for index in item:
                    tmp_list.append(
                        super().__getitem__(index)  # Call list.__getitem__() for each index in tuple
                    )
                return tmp_list
        else:
            return super().__getitem__(item)  # Call the normal __getitem__()


if __name__ == '__main__':
    fruits = 'banana peach nectarine fig kiwi lemon lime'.split()
    m = MultiIndexList(fruits)  # Initialize a MultiIndexList with a list
    m.append('apple')  # Add an element (works like normal list)
    m.append('mango')
    print(m)

    print(f"m[0]: {m[0]}")  # normal indexing
    print(f"m[5, 2, 0]: {m[5, 2, 0]}")  # multi-index with tuple
    print(f"m[:4]: {m[:4]}")  # normal slice
    print(f"len(m): {len(m)}")  # len() works normally
    print(f"m[5]: {m[5]}")  # get one item (normal behavior)
    print(f"m[5,]: {m[5,]}")  # get list with just one item [m[5]]
    print(f"m[:2,-2:]: {m[:2,-2:]}")  # get list with first two, last two items
    print()
    print(f"m: {m}")
    print(m)
    m.extend(['durian', 'kumquat'])
    print(m)
    print()
    for fruit in m:
        print(fruit)
