from animal import Animal


class Reptile(Animal):
    '''
        An animal with scales
    '''

    def __init__(self, species, name, sound, has_legs=True):
        super().__init__(species, name, sound)  # call parent constructor
        self._has_legs: bool = has_legs

    @property
    def has_legs(self):  # add reptile-specific property
        return self._has_legs


if __name__ == '__main__':
    guido = Reptile('Burmese python', 'Guido', "SSssssss", False)  # create instance of reptile
    smaug = Reptile('dragon', 'Smaug', 'Roarrrrrrr')

    for reptile in guido, smaug:
        legs_status = 'have' if reptile.has_legs else "do not have"
        print(f"Hi! I am {reptile.name} the {reptile.species} and I {legs_status} legs!")
        reptile.make_sound()  # call instance method from parents
        print()
