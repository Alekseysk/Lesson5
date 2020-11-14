"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""

with open("test2.txt", "r", encoding="utf-8") as test_file:
    file_content = test_file.readlines()
    
num_str = len(file_content)
print(f'В этом тексте {num_str} строк')
for ind, line in enumerate(file_content):
    num_words = len(line.split())
    print(f'В строке {ind} - {num_words} слов: {line.strip()}')
    
print('\nКак-то так...')