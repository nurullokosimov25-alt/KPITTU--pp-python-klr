count = 0
number = int(input("Введите число: "))
while number != 0:
    if number > 0:
        count += 1
    number = int(input("Введите число: "))
print("Количество положительных чисел:", count)
