"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open("test3.txt", "r", encoding="utf-8") as test_file:
    file_content = test_file.readlines()
    
num_employee = len(file_content)
income_average = 0
print(f'В базе данных {num_employee} сотрудников')
print('зарплата больше 20 000 у следующих:')
for line in file_content:
    family_name, income = line.strip().split()
    income = float(income)
    income_average += income / num_employee
    if income > 20000:
        print(f'{family_name}: {income}')
    
print(f'Средний доход сотрудников: {income_average:.2f}')