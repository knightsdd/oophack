import random
import time
from typing import List

from colorama import Back, Fore, Style

from classes import Person, Thing
from init_data import list_armoury, names_for_pers
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
        print(Fore.RED + 'К битве готовы!' + Fore.RESET)
        time.sleep(2)

    def battle():
        while len(army) > 1:
            attaker: Person = army.pop(random.randint(0, len(army) - 1))
            defender: Person = army.pop(random.randint(0, len(army) - 1))
            real_damage = defender.get_damage(attaker.attack_damage())
            print(Fore.BLUE + f'{attaker.name}' + Fore.RESET + ' наносит '
                  'удар по' + Fore.BLUE + f' {defender.name} ' + Fore.RESET +
                  'на ' + Fore.RED + f'{real_damage} урона.'
                  + Fore.RESET)
            army.append(attaker)
            if defender.isAlive():
                print('У ' + Fore.BLUE + f'{defender.name} ' + Fore.RESET +
                      'осталось ' + Fore.GREEN + f'{defender.get_hp()}' +
                      Fore.RESET + ' здоровья')
                army.append(defender)
            else:
                print(Fore.WHITE + Back.RED + f'☨ {defender.name} '
                      'пал на поле брани...' + Style.RESET_ALL)
            time.sleep(0.7)

        print(Fore.WHITE + Back.GREEN +
              f'{army[0].name} стал победителем арены!!!' + Style.RESET_ALL)

    def main():
        prepare_to_battle()
        while True:
            print('Подробнее о бойце (1, 2.. 10) или ')
            print('Начать сражение? (y)')
            key = str(input())
            if key == 'y':
                battle()
                print('Подготовиться к новой битве? (y)')
                if input() == 'y':
                    main()
                else:
                    print('До встречи на арене!')
                    exit()
            elif key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
                print(army[int(key) - 1])
            else:
                print('До встречи на арене!')
                exit()
    main()
