'''
Второй — без использования «Решета Эратосфена».
'''

import cProfile

N = 30

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def prime(n):
    cnt = 0
    i = 2
    while cnt < n:
        if isPrime(i):
            cnt += 1
        i += 1

    return i - 1

cProfile.run('prime(N)')
print(prime(N))

# timeit
# N = 30, 1000 loops, best of 5: 7.28 nsec per loop
# N = 100, 1000 loops, best of 5: 6.87 nsec per loop
# N = 500, 1000 loops, best of 5: 6.71 nsec per loop
# N = 1000, 1000 loops, best of 5: 7.28 nsec per loop

# cProfile
# N = 30, 116 function calls in 0.000 seconds
# N = 300, 1990 function calls in 0.002 seconds
# N = 3000, 27452 function calls in 0.038 seconds
# N = 30000, 350380 function calls in 1.004 seconds