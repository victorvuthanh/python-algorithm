'''
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

count = 0

seq = input("Введите последовательность цифр: ")
digit = input("Введите искомую цифру: ")

for c in seq:
    if c == digit:
        count += 1

print(f"Исковая цифра '{digit}' повторена в последовательности '{seq}' {count} раз")