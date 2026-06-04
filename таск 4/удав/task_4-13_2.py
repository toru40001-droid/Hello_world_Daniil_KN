n = int(input("Введите N: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал {n}! =", factorial)