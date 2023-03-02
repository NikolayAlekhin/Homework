#Задаем длину списка наполненного рандомными числами от 1 до 100.
#Вводим искомое число X
#Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
#которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению


import random
number = int(input('Введите число: '))
my_list = []
k = 0
closest_num = -1
for i in range(15):
    my_list.append(random.randint(1,101))
    min_d = max(my_list) - number

    if int(my_list[i]) == number:
         k += 1
for i in set(my_list):
     if abs(i - number) < min_d:
         min_d = abs(i - number)
         closest_num = i
print(f'{k} раз встречается в заданном списке число {number}')


print(f'максимально близкое число {closest_num}')

print(f'список {my_list}')

print(f'список без повторных чисел {set(my_list)}')