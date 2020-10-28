#формируем список из чисел Фибоначчи для последующих действий
#т.к. первые два элемента вычесть нельзя, задаем их и их сумму вручную
fibonachi_list = [1, 1]
fib_sum = 2
i = 2
sum_even = 0 #т.к. первые два элемента нечетные, обнуляем сумму нечетных
fib_even_list = [] #а это пустой список для четных элементов
while fib_sum <= 10000000:
    fibonachi_list.append(fib_sum)
    fib_sum = fibonachi_list[i] + fibonachi_list[i - 1]
    #чтобы дважды не проходить цикл, сразу считаем сумму четных элементов
    if fibonachi_list[i] % 2 == 0:
        fib_even_list.append(fibonachi_list[i])
        sum_even += fibonachi_list[i]
    i += 1
print('1. Количество элементов последовательности Фибоначчи,',
        'которые меньше 10 000 000 =', len(fibonachi_list))
print('2. Сумму всех четных элементов =', sum_even)
print('3. Список всех четных элементов:', *fib_even_list)
print('4. Предпоследнее число последовательности =', fibonachi_list[-2])
