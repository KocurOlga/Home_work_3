def sort_list(my_list, direction): #направление сортировки, если 1, то по возрастанию
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if (direction == 1 and my_list[i] > my_list[j]) or (direction != 1 and my_list[i] < my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list


list1 = [4, -2, 5, 3, -1 , 1, 0, 5, 2]
list2 = [5, 3, 2, 5, 6 , -1, 0, -5, 2]
list3 = [7, 2, 4, 1, -1 , 7, 3, -5, 0]
list4 = [2, -5, 6, 1, 0 , -1, -2, -3, 9]
list5 = [9, 0, 1, 2, 9 , 3, -1, 4, 2]

direct = int(input("Введите направление сортировки (1 - сортировка по возрастанию): "))

print(sort_list(list1, direct))
print(sort_list(list2, direct))
print(sort_list(list3, direct))
print(sort_list(list4, direct))
print(sort_list(list5, direct))
