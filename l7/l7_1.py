'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы.

Примечания:

a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,

b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''

from random import randint

MAX_SIZE = 10

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print('Исходный массив:', numbers)
print('Обратная пузырьковая:', bubble_sort(numbers))

