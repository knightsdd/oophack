from typing import List
from classes import Person, Thing
from init_data import list_armoury, names_for_pers
import random
import time
from utils import (dress_up_persons, generate_persons, make_armoury,
                   print_persons_light)

if __name__ == '__main__':
    armory: List[Thing] = []
    army: List[Person] = []

    def prepare_to_battle():
        global armory, army
        print('Готовим арсенал!')
        armoury = make_armoury(list_armoury, 40)
        print('Собираем добровольцев!')
        army = generate_persons(names_for_pers)
        print('Снаряжаем бойцов!')
        dress_up_persons(armoury, army)
        print('Бойцы готовы:')
        print_persons_light(army)
        print('К битве готовы!')
        time.sleep(2)

    def main():
        while len(army) > 1:
            attaker: Person = army.pop(random.randint(0, len(army) - 1))
            defender: Person = army.pop(random.randint(0, len(army) - 1))
            defender.get_damage(attaker.attack_damage())
            print(f'{attaker.name} наносит удар по '
                  f'{defender.name} на {attaker.attack_damage()} урона.')
            army.append(attaker)
            if defender.isAlive():
                army.append(defender)
            else:
                print(f'{defender.name} пал на поле брани...')
            time.sleep(0.5)

        print(f'{army[0].name} стал победителем арены!!!')

    prepare_to_battle()
    print('Начать сражение? (y)')
    start = str(input())
    if start == 'y':
        main()
    else:
        print('До встречи на арене!')
