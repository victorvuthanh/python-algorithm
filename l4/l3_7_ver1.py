'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

import cProfile

from random import random

def func():
    N = 50
    a = []
    for i in range(N):
        a.append(int(random() * 100))
        print("%3d" % a[i], end='')
    print()

    if a[0] > a[1]:
        min1 = 0
        min2 = 1
    else:
        min1 = 1
        min2 = 0

    for i in range(2, N):
        if a[i] < a[min1]:
            b = min1
            min1 = i
            if a[b] < a[min2]:
                min2 = b
        elif a[i] < a[min2]:
            min2 = i

    print("№%3d:%3d" % (min1 + 1, a[min1]))
    print("№%3d:%3d" % (min2 + 1, a[min2]))

cProfile.run('func()')

#timeit
#N=15, 1000 loops, best of 5: 7.26 nsec per loop
#N=100, 1000 loops, best of 5: 8.25 nsec per loop
#N=500, 1000 loops, best of 5: 9.79 nsec per loop

#cProfile
# N=50, 157 function calls in 0.000 seconds
# N=5000, 15007 function calls in 0.024 seconds
# N=500000, 1500007 function calls in 1.933 seconds

