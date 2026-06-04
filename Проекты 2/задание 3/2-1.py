
operator = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")
with open('sensor_log.txt', 'a', encoding='utf-8') as file:

    file.write(f"{operator}\t{pressure}.\n")

# Выводим сообщение об успехе
print("Данные успешно сохранены в sensor_log.txt")