class Spam():  # create normal class

    def __init__(self, name):
        self._name = name

    def eggs(self):  # add normal method
        print(f"Good morning, {self._name}. Here are your delicious fried eggs.")


s = Spam('Mrs. Higgenbotham')  # create instance of class
s.eggs()  # call method


def scrambled(self):  # define new method outside of class
    print(f"Hello, {self._name}. Enjoy your scrambled eggs")


setattr(Spam, "eggs", scrambled)  # monkey patch the class with the new method

s.eggs()  # call the monkey-patched method from the instance
