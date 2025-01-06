class NormalStringDict(dict):

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(value, str):
            raise TypeError("Value must be a string")

        key = key.strip().lower()
        value = value.strip().lower()
        super().__setitem__(key, value)

