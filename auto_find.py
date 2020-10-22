#выводим все машины по списку
auto1 = {'title': 'Lada', 'price': 7.0}
auto2 = {'title': 'Mazda', 'price': 8.0}
auto3 = {'title': 'Volkswagen', 'price': 7.5}

list_auto = [auto1, auto2, auto3]

for auto in list_auto:
    print('=================')
    for k, v in auto.items():
        print(f'{k}: {v}')
