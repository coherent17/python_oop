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
#mazda original door: 4
print("toyota original door:", toyota.door)
#toyota original door: 4


