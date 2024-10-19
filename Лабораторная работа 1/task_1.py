numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum = 0
# TODO заменить значение пропущенного элемента средним арифметическим
for i in numbers:
    if i != None:
        sum += i
count = len(numbers)
numbers[4] = sum / count
print("Измененный список:", numbers)
