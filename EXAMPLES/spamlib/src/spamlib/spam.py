"""
Subjects for testing
"""
import re
from hamlib import ham  

class Spam():
    def __init__(self, number):
        self._value = ham(number)

    @property
    def value(self):
        return self._value


class SpamSearch():  # System under test
    def __init__(self, search_string, target_string):
        self.search_string = search_string
        self.target_string = target_string

    def findit(self):  # Specific method to test (uses re.search)
        return re.search(self.search_string, self.target_string)


