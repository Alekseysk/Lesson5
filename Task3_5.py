"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

translator = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

with open("test3_5.txt", "r", encoding="utf-8") as test_file, \
        open("test3_5_out.txt", "w", encoding="utf-8") as test_file_out:
    line_readed = ' '
    while line_readed:
        line_readed = test_file.readline().strip()
        if line_readed:
            words = line_readed.split()
            words[0] = translator[words[0].lower()].capitalize()
            line_to_write = ' '.join(words)+'\n'
            test_file_out.writelines(line_to_write)
    