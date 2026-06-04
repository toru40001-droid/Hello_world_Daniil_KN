a = float(input("Введите 1-е число: "))
b = float(input("Введите 2-е число: "))
c = float(input("Введите 3-е число: "))
d = float(input("Введите 4-е число: "))

min_val = a
if b < min_val: min_val = b
if c < min_val: min_val = c
if d < min_val: min_val = d

print("Минимум:", min_val)