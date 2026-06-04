researcher = input("Введите ФИО исследователя: ")
date = input("Введите дату (в формате ГГГГ-ММ-ДД): ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод по эксперименту: ")
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write("-" * 50 + "\n")
    
    file.write("*            ЛАБОРАТОРНЫЙ ЖУРНАЛ                  *\n")
    
    file.write("*" * 50 + "\n")
    
    file.write(f"*   Исследователь: {researcher}\n")
    file.write(f"*   Дата: {date}\n")
    file.write(f"*   Эксперимент: {experiment}\n")
    file.write(f"*   Вывод: {conclusion}\n")
    
    file.write("-" * 50 + "\n")

print("Данные успешно записаны в journal.txt с красивым оформлением!")