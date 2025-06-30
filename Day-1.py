#a=5
#b='hello'
#c=12.5
#print(type(a))
#print(type(b))
#print(type(c))
#print(d)
#fruits = ["apple","Orange","Strawberry",-1,2,0,3.5]
#fruits.insert(3,"Mango")
#fruits.remove("Orange")
#SaakBhaji = []
#SaakBhaji.append("Tamata")
#SaakBhaji.insert(1,"Bhinda")
#SaakBhaji.extend(["Bateka","Dungri"])
#SaakBhaji.pop(0)
#print(SaakBhaji)
#print(len(SaakBhaji))
#add without using '+' addition operator
#a=4
#b=5
#c=a-(-b)
#print(c)
#print(SaakBhaji[1:3])
#Tuple
#number = (1,2,3,4)
#person = ("Alice",20,"Engineer")
#colors="Red","Grey"
#print(number)
#print(len(number))
#print(person)
#print(colors)
#print(person+colors)#concatenation
#print(number*2)#repition
#print(number.count(2))
#print(colors.index("Red"))
#Tuple Unpacking
#name,age,profession = person
#print(name)
#print(age)
#print(profession)
#Sets
#vowels = {'a','e','i','o','u'}
#vowels2 = (['a','e','i','o','u'])
#print(vowels)
#print(vowels2)
#Empty Set
#empty_set = set()
#print(empty_set)
#empty_set.add(1)
#empty_set.add(2)
#empty_set.add(3)
#empty_set.add(4)
#mpty_set.add(5)
#empty_set.remove(2)
#empty_set.discard(3)
#print(empty_set)
#print(4 in empty_set)
#print(len(empty_set))
#print(empty_set.copy())
#Mathematical Set Theory
#A = {1,2,3,4,5}
#B = {3,4,5,6,7}
#Union
#print(A|B)
#print(A.union(B))
#Diffenece
#print(A-B)
#print(A.difference(B))
#symmetric Difference
#print(A^B)
#set comprehension and frozen sets
#squares = {x**2 for x in range(1,6)}
#print(squares)
#Dictionary
student = {
    "name":"Alice",
   "age":20,
    "course":"Python"
}
print(student)
#using dict() constructor
person = dict(name="john",age=25) 
print(person)
#Empty Dictionary
empty_dict = {}
print(person.keys())
print(person.values())
print(person.items())
print(person.pop("age"))
students = {
    "101":{"name":"Tom","grade":"A"},
    "102":{"name":"jerry","grade":"A+"}
}
print(students["102"]["name"])
#User Input
#a=int(input("Enter a:"))
#b=int(input("Enter b:"))
#c=a+b
#print(c)
