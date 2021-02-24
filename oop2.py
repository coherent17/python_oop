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
    #initialize again in the lower class
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    #because the lower class has the method with same name as the higher
    #class so it overwrite the method
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    #if no defined the method then it will use the higher class method
    pass

p=Pet("Tim",19)
p.show()
p.speak()

c=Cat("Bill",34,"red")
c.show()
c.speak()

d=Dog("Jill",25)
d.show()
d.speak()

f=Fish("Bubbles",10)
f.speak()

