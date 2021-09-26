from typing import List


class Thing:

    def __init__(self, name: str, defence: float, damage: int, health: int):
        self.name = name
        self.defence = defence
        self.damage = damage
        self.health = health

    def __str__(self):
        return (f'Предмет: {self.name}, '
                f'защита: {self.defence}, '
                f'урон: {self.damage}, '
                f'повышает здровье на: {self.health}.')


class Person:

    def __init__(
        self,
        name: str,
        hp: float,
        base_attack: int,
        base_defence: float
    ):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.bag: List[Thing] = []

    def __str__(self):
        return(f'Персонаж: {self.name}, '
               f'единиц здоврья: {self.hp}, '
               f'базовая атака: {self.base_attack}, '
               f'базовая защита: {self.base_defence}.')

    def set_things(self, things: List[Thing]):
        self.bag = things

    def attack_damage(attacker):
        pass


class Paladin(Person):

    def __init__(
        self,
        name: str,
        hp: float,
        base_attack: int,
        base_defence: float
    ):
        super().__init__(name, hp * 2, base_attack, base_defence * 2)


class Warrior(Person):

    def __init__(
        self,
        name: str,
        hp: float,
        base_attack: int,
        base_defence: float
    ):
        super().__init__(name, hp, base_attack * 2, base_defence)
