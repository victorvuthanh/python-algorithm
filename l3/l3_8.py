'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

print('Полученная матрица')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))