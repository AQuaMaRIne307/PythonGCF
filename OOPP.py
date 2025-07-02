#Object Oriented Programming Python
'''1.Classes And Objects
->Class
-> a class is a blueprint for creating objects.
it defines attributes and methods.'''
'''
class Person:
    def __init__(self,name,age):
        self.name = name   #attribute
        self.age = age   #attribute
    def greet(self):    #method
      print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
p1 = Person("Alice",25)
p1.greet()#Output:Hi,I'm Alice and I'm 25 years old.
'''
'''
class Account:
    def __init__(self):
        self.__balance = 1000
    def show_balance(self):
        print("Balance is",self.__balance)
a = Account()
a.show_balance()
print(a.__balance)
'''
#Inheritance allows one class (child) to 
# inherit attributes and methods from another 
# class(parent)
'''class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.speak()
d.bark()'''
#Polumorphism
#polymorphism allows differnt classes to define 
# methods with the same name that behave differently.
'''
class Bird:
    def sound(self):
        print("Chirp")
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")
def make_sound(animal):
    animal.sound()
b = Bird()
c = Cat()
cw = Cow()
make_sound(b)
make_sound(c)
make_sound(cw)
#Method Overriding
class Parent:
    def show(self):
        print("Parent's method")
        
class Child(Parent):
    def show(self):
        print("Child's method")

obj = Child()
obj.show()
'''
