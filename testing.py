cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]
tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]
city = input('Введите город: ')
city = city.capitalize()

if city in cities:
    if tourists[0]['city'] == city:
        user = 0
    if tourists[1]['city'] == city:
        user = 1
    if tourists[2]['city'] == city:
        user = 2
    print(f"Турист {users[user]['name']} возраст {users[user]['age']}. Посетил город {city}.")     
else:
    print('Такого города в списке нет.')
