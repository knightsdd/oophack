from classes import Thing, Person, Paladin, Warrior

if __name__ == '__main__':

    thing1 = Thing('Короткий меч', 0.01, 20, 0)
    thing2 = Thing('Деревяный щит', 0.1, 0, 0)

    pers1 = Person('Крестьянин', 100, 5, 5)
    pers2 = Paladin('Молодой паладин', 100, 5, 5)
    pers3 = Warrior('Молодой воин', 100, 5, 5)

    print(thing1)
    print(thing2)
    print(pers1)
    print(pers2)
    print(pers3)
