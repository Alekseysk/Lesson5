"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import random


def rand_num():
    yield random() * 100
    

with open("test4.txt", "w", encoding="utf-8") as test_file:
    for i in range(10):
        line = ''
        for j in range(10):
            line += f'{next(rand_num()):.3f} '
        line += '\n'
        test_file.writelines(line)

with open("test4.txt", "r", encoding="utf-8") as test_file:
    lines = test_file.readlines()
    summ = 0
    for line in lines:
        line = line.strip().split()
        for number in line:
            summ += float(number)
    
print(f'Общая сумма цифр, записанных в файле: {summ:.2f}')