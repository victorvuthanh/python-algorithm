'''
Первый — с помощью алгоритма «Решето Эратосфена».
'''

import cProfile
N = 30

import math

''' 
    Решето Эратосфена. В списке bits сбрасываются биты,
    имеющие составные номера, биты с простыми номерами == 1.
    i-му по порядку элементу будет соответствовать 1, если 
    i -- простое и 0 иначе. Сложность: nloglog(n).
'''

def bit_sieve(n):
    if n < 2:
        return []
    bits = [1] * n  # <-- 11...1
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if bits[i - 2]:  # если i -- простое
            for j in range(i + i, n + 1, i):  # занулить все ему кратные
                bits[j - 2] = 0
    return bits

def sieve(k):
# k-ое простое не превосходит 1,5 k ln( k ) при k > 1:
    sieve = bit_sieve(int(1.5 * k * math.log(k)) + 1)
    i = 0
    while k:
        k -= sieve[i]
        i += 1
    return i + 1

cProfile.run('sieve(N)')
print(sieve(N))
# timeit
# N = 30, 1000 loops, best of 5: 7.28 nsec per loop
# N = 100, 1000 loops, best of 5: 7.29 nsec per loop
# N = 500, 1000 loops, best of 5: 6.89 nsec per loop
# N = 1000, 1000 loops, best of 5: 6.9 nsec per loop

# cProfile
# N = 30, 7 function calls in 0.000 seconds
# N = 300, 7 function calls in 0.001 seconds
# N = 3000, 7 function calls in 0.009 seconds
# N = 30000, 7 function calls in 0.149 seconds