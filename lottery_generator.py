# программа генератора лотерейных чисел

import random

# запрос ввода диапазона значений и количества чисел
start_num = int(input("Введите начальное значение диапазона: "))
end_num = int(input("Введите конечное значение диапазона: "))
num_count = int(input("Введите количество чисел для генерации: "))

# генерация лотерейных чисел
lottery_numbers = []
for i in range(num_count):
    num = random.randint(start_num, end_num)
    while num in lottery_numbers:
        num = random.randint(start_num, end_num)
    lottery_numbers.append(num)

# вывод результатов
print("Сгенерированные лотерейные числа:")
