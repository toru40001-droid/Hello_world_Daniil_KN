array = [2, 4, 6, 8, 10, 12]
even_idx_sum = 0
count = 0
for i in range(len(array)):
    if i % 2 == 0: # Если индекс четный
        even_idx_sum += array[i]
        count += 1
print("Среднее элементов с четными индексами:", even_idx_sum / count)