from init_data import list_armoury, names_for_pers
from utils import (dress_up_persons, generate_persons, make_armoury,
                   print_persons)

if __name__ == '__main__':

    def main():
        armoury = make_armoury(list_armoury, 40)
        army = generate_persons(names_for_pers)
        dress_up_persons(armoury, army)
        print_persons(army)

    main()
