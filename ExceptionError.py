#Exception Handling in Python
#An Exception is an event that disrupts 
#the normal flow of a program's execution.
'''
x = 10
y = 0
print(x/y) #zeroDivisionError
try:
    x = 10/0
except :
    print("You can't divide by zero")
try:
    y = int(input())
    result = 10/y
    print(result)
except ZeroDivisionError:
    print("Division by Zero is not allowed")
except ValueError:
    print("Enter a valid number")
else:
    print("Success:",result)

#Finally Block
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file...")

#Raising Exception manually
age = int(input("Enter Your Age:"))
if age < 18:
    raise ValueError("Age must be 18 or older.")
else:
    print("Access to vote")'''

