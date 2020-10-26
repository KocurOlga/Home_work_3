def print_ingredients(pizza, *ingredients):
    print(f'все ингредиенты пиццы: {pizza}')
    for i in ingredients:
        print(i)
    print('-----------------------')


print_ingredients('Маргарита', 'тесто', 'сыр', 'помидоры')
print_ingredients('Диабло', 'тесто', 'сыр', 'помидоры', 'колбаса', 'перец чили')
