'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

import cProfile

from random import randint

def func():
    N = 50
    array = [randint(1, 100) for i in range(N)]
    print(array)

    sort_list = []
    sort_list.extend(array)
    sort_list.sort()

    print(
        f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}'
        )

cProfile.run('func()')

#timeit
# N=15, 1000 loops, best of 5: 8.78 nsec per loop
# N=100, 1000 loops, best of 5: 9.83 nsec per loop
# N=500, 1000 loops, best of 5: 9.78 nsec per loop

#cProfile
# N=50, 274 function calls in 0.000 seconds
# N=5000, 26400 function calls in 0.015 seconds
# N=500000, 2640327 function calls in 1.018 seconds