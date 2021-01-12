class Person:
    def __init__(age = 10, height = 150, weight, name):
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__name = name

    def getAge(self):
        print(self.__age)

    def getHeight(self):
        print(self.__height)

    def setWeight(self):
        self.__weight = int(input)
        print(self.__weight)

    def setName(self):
        self.__name = input
        print(self.__name)

    person1 = Person()
    person1.getAge()
    person1.getHeight()
    person1.setName()
    person1.setWeight()

    def 

