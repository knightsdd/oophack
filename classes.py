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
        thing_info: str = ''
        for thing in self.bag:
            thing_info += str(thing) + '\n'
        return('-----Iformation about person------\n'
               f'Персонаж: {self.name},\n'
               f'Класс: {self.__class__.__name__}, \n'
               f'единиц здоровья: {self.hp},\n'
               f'базовая атака: {self.base_attack},\n'
               f'реальная атака: {self.attack_damage()},\n'
               f'базовая защита: {self.base_defence},\n'
               f'реальная защита: {self.finalProtection()}.\n'
               'Экипировка: \n'
               f'{thing_info}'
               '----------------------------------\n')

    def set_things(self, things: List[Thing]):
        self.bag = things
        self.update_health()

    def attack_damage(self):
        additional_damage = 0
        for thing in self.bag:
            additional_damage += thing.damage
        return (self.base_attack + additional_damage)

    def finalProtection(self) -> float:
        additional_defence: float = 0
        for thing in self.bag:
            additional_defence += thing.defence
        return round(self.base_defence + additional_defence, 2)

    def update_health(self):
        additional_health = 0
        for thing in self.bag:
            additional_health += thing.health
        self.hp += additional_health

    def get_hp(self):
        return round(self.hp, 2)

    def get_damage(self, damage: int):
        real_damage = round(damage - damage * self.finalProtection(), 2)
        self.hp = self.get_hp() - real_damage
        return real_damage

    def isAlive(self) -> bool:
        if self.get_hp() > 0:
            return True
        else:
            return False


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
