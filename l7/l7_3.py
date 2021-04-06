'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''


import statistics

import random


def median(array, k):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return median(right_el, k - len(left_el) - len(pivots))


M = random.randint(1, 9)
lst = [random.randint(0, 20) for _ in range(2 * M + 1)]
print(f'M = {M}, 2 * M + 1 = {2 * M + 1}')
print(f'Исходный список:\n{lst}')
print(f'Медианой списка является: {median(lst, len(lst) / 2)}')


print('Медиана statistics:', statistics.median(lst))