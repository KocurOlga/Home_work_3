def plural_form(num, *form_list):
    if 5 <= num <= 20:
        new_string = f'{num} {form_list[2]}'
    elif str(num)[-1] == '1' and num != '11':
        new_string = f'{num} {form_list[0]}'
    elif str(num)[-1] == '2' or str(num)[-1] == '3' or str(num)[-1] == '4':
        new_string = f'{num} {form_list[1]}'
    else:
        new_string = f'{num} {form_list[2]}'
    return new_string


print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
print(plural_form(11, 'студент', 'студента', 'студентов'))
print(plural_form(15, 'студент', 'студента', 'студентов'))
print(plural_form(3, 'студент', 'студента', 'студентов'))
