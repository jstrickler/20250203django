from animal import Animal


class Insect(Animal):
    '''
        An animal with 2 sets of wings and 3 pairs of legs
    '''

    def __init__(self, species, name, sound, can_fly=True):  # constructor (AKA initializer)
        super().__init__(species, name, sound)  # call base class constructor
        self._can_fly: int = can_fly

    @property
    def can_fly(self):  # "getter" property
        return self._can_fly


if __name__ == '__main__':
    mon = Insect('monarch butterfly', 'Mary', None)  # defaults to can_fly being True
    scar = Insect('scarab beetle', 'Rupert', 'Bzzz', False)

    for insect in mon, scar:
        flying_status = 'can' if insect.can_fly else "can't"
        print(f"Hi! I am {insect.name} the {insect.species} and I {flying_status} fly!")
        insect.make_sound()  # .make_sound inherited from Animal
        print()
