"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

import json

with open("test6.txt", "r", encoding="utf-8") as test_file:
    lines = test_file.readlines()
    
business = {}
aver_prof = {}
profits = []
for line in lines:
    firm, form, incomes, expenses = line.strip().split()
    profit = float(incomes) - float(expenses)
    if profit > 0:
        profits.append(profit)
    business[firm] = profit
aver_prof['average_profit'] = sum(profits) / len(profits)

result = [business, aver_prof]

with open('test6.json', 'w', encoding="utf-8") as fout:
    json.dump(result, fout, ensure_ascii=False)