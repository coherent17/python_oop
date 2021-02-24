#https://www.learncodewithmike.com/2020/01/python-class.html
#class (類別)
#object (物件)
#attribute (屬性)
#constructor (建構式)
#method (方法)

#汽車類別
class Car:
    #建構式
    def __init__(self,color,seat):
        self.color=color #顏色屬性
        self.seat=seat #座位屬性

    #方法
    def drive(self):
        print(f"My car is {self.color} and {self.seat} seats")

#Mazda是Car類別中的物件
Mazda=Car("red",4)

#use isinstance to judge the relationship between the class and the object
print(isinstance(Mazda,Car)) #True

