phone = int(input('Введите ваш номер: '))
numbers = {1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           0: 'zero',
    }
list = []
while phone > 0:
    num = phone % 10
    list.append(num)
    phone = phone // 10
list.reverse()
for i in list:
    print(numbers[i])
