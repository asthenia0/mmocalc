def check_lvl(lvl):
    if lvl < 0:
        return 'Слишком низкий уровень (минимум 0)'
    if lvl > 99:
        return 'Слишком высокий уровень (максимум 99)'

def check_demon_loop(demon_loop):
    if demon_loop < 0:
        return 'Слишком низкий круг (минимум 0)'
    if demon_loop > 15:
        return 'Слишком высокий круг (максимум 15)'

def check_angel_order(angel_order):
    if angel_order < 0:
        return 'Слишком низкий порядок (минимум 0)'
    if angel_order > 10:
        return 'Слишком высокий порядок (максимум 10)'