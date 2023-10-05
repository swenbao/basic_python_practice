string = "1, 2, 3, 4, 5, 6, 7, 8, 9"
numbers = [int(num) for num in string.split(", ")]

for i in range(len(numbers)):
    print(type(numbers[i]))

