seq_list = ["ATATACGCGTA, "CTTCGGNGGA"]

print("Начинаем перебор последовательностей...")
print("-" * 40)

for seq in seq_list:
    print(f"Последовательность: {seq}")
    print("Разбивка по символам:")
    
    for letter in seq:
        print(letter)
    
    print("-" * 20)

print("Цикл выполнен")