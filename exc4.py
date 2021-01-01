#program to remove the dublicates from the list
num = [1, 2, 1, 2, 3, 4, 5, 3]
num.sort()
for i in num:
    amount = 0
    amount = num.count(i)
    if amount > 1:
        num.remove(i)
print(num)
