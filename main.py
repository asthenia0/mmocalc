from pywebio.input import *
from pywebio.output import *
import check
from db import gun_name


demon = ([0, 0, 0, 0, 0, 0, 0],
         [1, 3, 2, 1, 3, 4, 25],
         [2, 6, 4, 2, 6, 8, 50],
         [3, 9, 6, 3, 7, 12, 75],
         [4, 12, 8, 4, 8, 16, 100],
         [5, 15, 10, 5, 9, 20, 125],
         [6, 18, 12, 6, 10, 24, 150],
         [7, 21, 14, 7, 11, 28, 175],
         [8, 24, 16, 8, 13, 32, 200],
         [9, 27, 18, 9, 14, 36, 225],
         [11, 30, 20, 10, 15, 40, 250],
         [12, 33, 22, 11, 16, 44, 275],
         [13, 36, 24, 12, 17, 48, 300],
         [14, 39, 26, 13, 18, 52, 325])

angel = (0, 100, 150, 200, 250, 350, 450, 400, 700, 900, 1000)

def mbcalculator():

    HP = 5
    uron = 0
    toch = 0
    armor = 0
    uvorot = 0
    glush = 0
    block = 0

    HP_pos = 6
    uron_pos = 1
    toch_pos = 0
    armor_pos = 5
    uvorot_pos = 4
    glush_pos = 3
    block_pos = 2

    data = input_group("Базовые характеристики",[
        input('Введите свой уровень', name='lvl', type=NUMBER, validate=check.check_lvl),
        input('Введите свой круг демона', name='loop', type=NUMBER, validate=check.check_demon_loop),
        input('Введите свой порядок ангела', name='order', type=NUMBER, validate=check.check_angel_order)
        ])

    equip = input_group("Снаряжение", [
        select('Оружие', options=gun_name[0], name='gun'),
        select('Щит', options=gun_name[0], name='shield'),
        select('Шлем', options=gun_name[0], name='helmet'),
        select('Перчатки', options=gun_name[0], name='gloves'),
        select('Доспех', options=gun_name[0], name='armor'),
        select('Поножи', options=gun_name[0], name='leg'),
        select('Сапоги', options=gun_name[0], name='boots'),
        select('Амулет', options=gun_name[0], name='amulet'),
        select('Кольцо 1', options=gun_name[0], name='ring1'),
        select('Кольцо 2', options=gun_name[0], name='ring2'),
        select('Пояс', options=gun_name[0], name='belt1')
        ])

    HP = HP + gun_name[(gun_name[0].index(equip["gun"]))+1][HP_pos]
    uron = uron + gun_name[(gun_name[0].index(equip["gun"]))+1][uron_pos]
    toch = toch + gun_name[(gun_name[0].index(equip["gun"]))+1][toch_pos]
    armor = armor + gun_name[(gun_name[0].index(equip["gun"]))+1][armor_pos]
    uvorot = uvorot + gun_name[(gun_name[0].index(equip["gun"]))+1][uvorot_pos]
    glush = glush + gun_name[(gun_name[0].index(equip["gun"]))+1][glush_pos]
    block = block + gun_name[(gun_name[0].index(equip["gun"]))+1][block_pos]

    HP = HP + (data['lvl'] * 5) + demon[data['loop']][HP_pos] + angel[data['order']]
    uron = uron + (data['lvl'] * 2) + demon[data['loop']][uron_pos]
    toch = toch + (data['lvl'] * 2) + demon[data['loop']][toch_pos]
    armor = armor + (data['lvl'] * 2) + demon[data['loop']][armor_pos]
    uvorot = uvorot + (data['lvl'] * 2) + demon[data['loop']][uvorot_pos]
    glush = glush + (data['lvl'] * 2) + demon[data['loop']][glush_pos]
    block = block + (data['lvl'] * 2) + demon[data['loop']][block_pos]
    put_row([
        put_table([
            ['Уровень', data['lvl']],
            ['Демон', data['loop']],
            ]),
        None,
        put_table([
            ['Статы', 'Значения'],
            ['Здоровье', HP],
            ['Урон', uron],
            ['Точность', toch],
            ['Броня', armor],
            ['Уворот', uvorot],
            ['Оглушение', glush],
            ['Блок', block],
            ]),
        ],
        size='50% 1px 50%')

if __name__=='__main__':
    mbcalculator()
    start_server(main, port=8080, debug=True)