#  1.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# v - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

some_num = int(input('Input some number: '))
set_num = []
set_sum = 0
print(f'Для n={some_num}: (', end = ' ')
for i in range(1, some_num):
    set_num.append((1+1/i)**i)
    set_sum += set_num[i-1]
    print(f' {i}: {round(set_sum, 2)},', end = ' ')
print(f' {some_num}: {round((set_sum+(1+1/some_num)**some_num), 2)} )')