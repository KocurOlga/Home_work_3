def fizz_buzz(start, end):
    result = 0
    """Функция выводит сумму чисел из диапазона от start
    до end включительно, которые делятся на 3 и на 5, где:
    :param start: начало дипазона
    :param end: конец диапазона"""
    for i in range(start, end + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            result += i
    return result

range_start = int(input('Введите начальное значение диапазона: '))
range_end = int(input('Введите конечное значение диапазона: '))

print(fizz_buzz(range_start, range_end))
