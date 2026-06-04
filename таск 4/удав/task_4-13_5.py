n = int(input("Введите N: "))
sq_sum = 0
for i in range(1, n + 1):
    sq_sum += i**2
print("Сумма квадратов:", sq_sum)