n = int(input("Сколько чисел вы введете? "))
max_val = float(input("Введите 1-е число: "))

for i in range(2, n + 1):
    current = float(input(f"Введите {i}-е число: "))
    if current > max_val:
        max_val = current

print("Максимум:", max_val)