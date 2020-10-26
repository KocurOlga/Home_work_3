def quantity(object_list, is_fruit = None):
    result = 0
    for i in object_list:
        if is_fruit is None or i['is_fruit'] == is_fruit:
            result += 1
    return result


def update_list(object_list, new_object):
    # в переменной result будем хранить результат выполнения функции
    # True - если элемент добавили в список
    # False - если не добавили
    # По умолчанию присваиваем в result значение False
    result = False
    # Ищем элемент в списке по ключу title у объекта new_object
    # Если нашли, то присваиваем переменной found значение True
    found = False
    for i in object_list:
        if i['title'] == new_object:
            found = True
    # Если такого элемента в списке нет (т.е. found == False), то добавляем объект new_object в список object_list
    # Если такой элемент там уже есть, то ничего не делаем
    if not found:
        object_list.append(new_object)
        result = True
    return result


item_list = [{'title': 'Яблоко', 'is_fruit': True},
             {'title': 'Апельсин', 'is_fruit': True},
             {'title': 'Банан', 'is_fruit': True},
             {'title': 'Автомобиль', 'is_fruit': False},
             {'title': 'Телефон', 'is_fruit': False},
             {'title': 'Груша', 'is_fruit': True}, ]

element_added = update_list(item_list, {'title': 'Груша', 'is_fruit': True})

# print(f'Количество фруктов = {quantity(item_list, is_fruit = True)}')
# print(f'Количество не фруктов = {quantity(item_list, is_fruit = False)}')
# print(f'Количество элементов всего = {quantity(item_list)}')
if element_added:
    print('Добавили новый элемент')
else:
    print('Такой элемент уже есть в списке')