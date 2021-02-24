#https://www.learncodewithmike.com/2020/01/python-attribute.html

#attribute (屬性)
#instance attribute (實體屬性)
#class attribute (類別屬性)

#method (方法)
#instance method (實體方法)
#class method (類別方法)
#static method (靜態方法)

#一 instance attribute (實體屬性)
class Car:
    def __init__(self,color,seat):
        self.color=color
        self.seat=seat
        self.weight=140

Mazda=Car("blue",4)
Mazda.color="yellow"
Mazda.seat=8
Mazda.weight=200

Toyota=Car("red",6)

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