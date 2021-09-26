from typing import List

from classes import Thing

names_for_pers: List[str] = [
        'Крестьянин',
        'Солдат',
        'Морпех',
        'Капрал',
        'Танкист',
        'Чапаев',
        'Петька',
        'Охотник',
        'Ассасин',
        'Алладин',
        'Тони Старк',
        'Маленький принц',
        'Джокер',
        'Мегатрон',
        'Оптимус Прайм',
        'Эникен Скайвокер',
        'Чак Норис',
        'T-200',
        'Хэнкок',
        'Сара Керриган',
    ]

list_armoury: List[Thing] = [
    Thing('Короткий меч', 0.01, 20, 0),
    Thing('Средний меч', 0.02, 30, 0),
    Thing('Длинный меч', 0.03, 40, 0),
    Thing('Булава', 0, 35, 0),
    Thing('Световой меч джадая', 0, 90, 0),
    Thing('Деревяный легкий щит', 0.05, 0, 0),
    Thing('Деревяный тяжелый щит', 0.06, 0, 0),
    Thing('Стальной легкий щит', 0.07, 0, 0),
    Thing('Стальной тяжелый щит', 0.08, 0, 0),
    Thing('Сверхтяжелый титановый щит', 0.1, 0, 0),
    Thing('Кольцо здоровья', 0, 0, 100),
    Thing('Кольчуга Зевса', 0.1, 0, 50),
    Thing('Амулет Ахилеса', 0, 90, 50),
]
