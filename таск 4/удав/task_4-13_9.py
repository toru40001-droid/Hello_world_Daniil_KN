array = [10, 20, 30, 40, 50, 60] # Индексы: 0, 1, 2, 3, 4, 5
index_sum = 0
for i in range(len(array)):
    if i % 2 != 0: # Если индекс нечетный
        index_sum += array[i]
print("Сумма элементов с нечетными индексами:", index_sum)