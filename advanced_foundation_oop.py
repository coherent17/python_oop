#https://www.learncodewithmike.com/2020/01/python-attribute.html

#attribute (屬性)
#instance attribute (實體屬性)
#class attribute (類別屬性)

#method (方法)
#instance method (實體方法)
#class method (類別方法)
#static method (靜態方法)

#一 instance attribute (實體屬性)
class Car1:
    def __init__(self,color,seat):
        self.color=color
        self.seat=seat
        self.weight=140

Mazda=Car1("blue",4)
Mazda.color="yellow"
Mazda.seat=8
Mazda.weight=200

Toyota=Car1("red",6)

print("Mazda color: ", Mazda.color)
print("Mazda seat: ", Mazda.seat)
print("Mazda weight: ", Mazda.weight)

# Mazda color:  yellow
# Mazda seat:  8
# Mazda weight:  200

print("Toyota color: ", Toyota.color)
print("Toyota seat: ", Toyota.seat)
print("Toyota weight: ", Toyota.weight)
# Toyota color:  red
# Toyota seat:  6
# Toyota weight:  140

#if we change one of the object attribute
# another object of the attribute will not change


#二 class attribute (類別屬性)
class Car2:
    door=4

    def __init__(self,color,seat):
        self.color=color
        self.seat=seat
        self.weight=140
    
mazda=Car2("blue",4)
toyota=Car2("red",6)
print("mazda original door:", mazda.door)
print("toyota original door:", toyota.door)
#mazda original door: 4
#toyota original door: 4

#the attribute defined outside the constructor 
#can be change in all object
#ex:
Car2.door=8
print("mazda new door:", mazda.door)
print("toyota new door:", toyota.door)
# mazda new door: 8
# toyota new door: 8

#三 property (屬性)
class Car3:
    def __init__(self,weight):
        self.weight=weight

Tida=Car3(-200)
#however the weight can not be less than 0
#how can we fixed?

#First way:
class Car4:
    def __init__(self,weight):
        self.set_weight(weight)

    def get_weight(self):
        return self.__weight

    def set_weight(self,value):
        if value<=0:
            raise ValueError("Car weight can't be 0 or less")
        self.__weight=value

#tida=Car4(-200)
#ValueError: Car weight can't be 0 or less
#non-pythonic

class Car5:
    def __init__(self,weight):
        self.weight=weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,value):
        if value<=0:
            raise ValueError("Car weight can't be 0 or less")
        self.__weight=value

# Nissan=Car5(100)
# print(Nissan.weight) #100
Nissan=Car5(-100)
#ValueError: Car weight can't be 0 or less