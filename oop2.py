class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")
#inherit
class Cat(Pet):
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color

    #because the lower class has the method with same name as the higher
    #class so it overwrite the method
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p=Pet("Tim",19)
p.show()
#I am Tim and I am 19 years old
p.speak()
#I don't know what I say

c=Cat("Bill",34)
c.show()
#I am Bill and I am 34 years old
c.speak()
#I am Bill and I am 34 years old
#Meow

d=Dog("Jill",25)
d.show()
#I am Jill and I am 25 years old
d.speak()
#Bark

f=Fish("Bubbles",10)
f.speak()
#I don't know what I say  
#because there is no speak from the class Fish so it use the
#higher class method
