import random
from typing import List

from classes import Paladin, Thing, Warrior


def generate_persons(names: List[str]) -> List:
    persons: List = []
    for i in range(10):
        race = random.randint(0, 1)
        if race == 0:
            persons.append(
                Paladin(
                    name=names.pop(random.randint(0, len(names) - 1)),
                    hp=100,
                    base_attack=random.randint(10, 20),
                    base_defence=random.randint(0, 10) / 100,
                )
            )
        else:
            persons.append(
                Warrior(
                    name=names.pop(random.randint(0, len(names) - 1)),
                    hp=100,
                    base_attack=random.randint(10, 20),
                    base_defence=random.randint(0, 10) / 100,
                )
            )
    return persons


def print_persons_full(persons: List):
    for person in persons:
        print(person)


def print_persons_light(persons: List):
    count = 1
    for person in persons:
        print(f'{count}. {person.name}')
        count += 1


def sort_key(thing: Thing) -> float:
    return thing.defence


def make_armoury(weapons, count) -> List:
    armoury = []
    for _ in range(0, count):
        armoury.append(weapons[random.randint(0, len(weapons) - 1)])
    armoury = sorted(armoury, key=sort_key)
    return armoury


def dress_up_persons(things: List, persons: List):
    for person in persons:
        limit = random.randint(1, 4)
        bag: List[Thing] = []
        for _ in range(limit):
            bag.append(things.pop(random.randint(0, len(things) - 1)))
        person.set_things(bag)
