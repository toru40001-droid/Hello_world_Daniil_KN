array = [1, 2, 3, 4, 5, 6]
odd_sum = 0
for x in array:
    if x % 2 != 0: # Проверка на нечетность
        odd_sum += x
print("Сумма нечетных элементов:", odd_sum)