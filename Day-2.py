'''s1="be here be vibrant"
s2="bye"
s3=s1+s2
print(s1+"  "+s2+"   ")
print(len(s1+"  "+s2+"   "))
print(s3.find("th"))
print(s3.find("he"))
print(s3.find("l"))
print(s3.count("e"))    
print(s1.startswith("be"))
print(s1.endswith("vibrant"))
name = "Alice"
age = 20
print(f"my name is {name} and my age is {age}")'''
'''email = input("Enter your email:")
if "@" in email and email.endswith(".ac.in"):
    check=email.startswith("24030")
    print("Valid Email")
else:
    print("Invalid Email")'''

'''age = int(input("Enter your age:"))
if age >=18:
    print("You are eligible to vote")'''
    
'''marks=34
if marks >= 35:
    print("HooRayyy! You Passed!!!")
else:
    print("Chapal khayega ya Jhadoo")'''
  
'''age=int(input("Enter your age:"))
weight=int(input("Enter your weight:"))
alchol=(input("Are you drinking alchol?:"))
if(age>=18):
  if(weight>=40):
    if(alchol=="no"):
      print("Eligible")
    else:
      print("Not Eligible")'''
    

'''marks = int(input("Enter Your Marks:"))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B+")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
elif marks >= 35:
    print("Grade E")
else:
    print("Grade F")'''
    
#For Loop
'''for i in range(1,6):
    a=i**2
    print(a)'''
'''for i in range(1,6):
    for j in range(i):
        print("*",end=" ") 
    print()
    
for i in range(1,6):
    for j in range(6-i):
        print("*",end=" ") 
    print()
    
for i in range(1,6):
    for j in range(6-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")  
    print()'''
    
'''for i in range(1,6):
    for j in range(i):
        print(i,end=" ") 
    print()
for i in range(1,6):
    for j in range(i):
        print(j+1,end=" ") 
    print()'''

#While Loop
'''count = 1
while count <= 5:
    print(count)
    count += 1
    
#Break Statement
for i in range(1,6):
    if i==3:
        break
    print(i)
    
#continue Statement
for i in range(1,6):
    if i==3:
        continue
    print(i)'''

#Pass Statement
'''Used as a placeholder for future code
or an empty block
for i in range(5):
    pass
def future_function():
    pass'''
    
'''#Practice Questions
->Real-Life Example:ATM Simulation
->Write a Program to cheack if a number
is positive,negative or zero.
->Create a loop that skips multiples of 3.
->Create a loop to stop the loop if the
user inputs a negative number.
'''
#Functions and modules
#Defining Funtion
'''def greet():
    print("Hello,Welcome to python!")
#Calling of Funtion
greet()
def Sum():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a+b
    print(c)
#Calling of Funtion
Sum()'''
#Function Arguments(Paraments)
'''def greet_user(name):
    print("Hello!",name) 
greet_user(input("Enter Your Name:"))
#Types of arguments
#potional arguments
greet_user("Alice")
#keyword arguments
greet_user(name="Alice")
#Default arguments
greet(name="Guest")
#Variable length arguments
*args,**kwargs'''
'''def math(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
math(3,7)
#return values
def square(x):
    return x*x
result = square(3)
print(result)'''
#Python Modules
#Importing Modules
'''import math
print(math.sqrt(16))
print(math.pi)
print(math.pow(1024,3))
import random
print(random.randint(1,10))
import datetime as dt
print(dt.datetime.now())
from customModule import add,sub,mlt,div
add(3,5)'''
