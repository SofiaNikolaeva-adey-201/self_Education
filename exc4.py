#program to remove the dublicates from the list
num = [1, 2, 2, 2, 1, 2, 3, 4, 5, 3]
only = []

for i in num:
   if i not in only:
       only.append(i)
print(only)
