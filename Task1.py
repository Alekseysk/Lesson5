"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("test.txt", "w", encoding="utf-8") as test_file:
    input_str = ' '
    while input_str:
        input_str = input('Введите новую строку, ввод для завершения:\n')
        test_file.writelines(input_str+'\n')