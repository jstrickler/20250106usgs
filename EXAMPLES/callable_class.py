class TagWrapper():
    def __init__(self, tag):
        self._tag = tag

    def wrap(self, text):
        return f'<{self._tag}>{text}</{self._tag}>'

class HTMLWrapper():

    def __init__(self, tag):
        self._tag = tag

    def __call__(self, text):  # Define function to be called when instance is called
        return f'<{self._tag}>{text}</{self._tag}>'

if __name__ == '__main__':
    # non-callable class
    t = TagWrapper('h1')
    print(t.wrap('foo'))
    print(t.wrap('bar'))
    print()

    # callable class
    h1 = HTMLWrapper('h1')  # Create instance of "callable class"
    print(h1('spam'))  # Instance is callable -- essentially  h1.call('spam')
    div = HTMLWrapper('div')
    print(div('ham'))
    print(div('toast'))
    print(div('jam'))
