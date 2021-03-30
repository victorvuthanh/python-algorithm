'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

import cProfile

from random import randint

def func():
    N = 500000
    array = [randint(1, 100) for i in range(N)]
    print(array)

    min1 = min(array)
    array.remove(min1)
    min2 = min(array)

    print(min1)
    print(min2)

cProfile.run('func()')

#timeit
# N=15, 1000 loops, best of 5: 7.31 nsec per loop
# N=100, 1000 loops, best of 5: 7.27 nsec per loop
# N=500, 1000 loops, best of 5: 7.95 nsec per loop

#cProfile
# N=50, 284 function calls in 0.000 seconds
# N=5000, 26419 function calls in 0.014 seconds
# N=500000, 2639839 function calls in 0.978 seconds
