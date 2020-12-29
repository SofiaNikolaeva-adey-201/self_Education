numbers = [2, 10, 99, 1, 0, 37]
max = numbers[0]
for i in numbers:
    if max < i:
        max = i
print(max)
