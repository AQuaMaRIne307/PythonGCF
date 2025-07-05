
# main.py

import mymodule


name = input("Enter your name: ")
message = mymodule.greet(name)
print(message)

print("\nLet's do some math!")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_result = mymodule.add(a, b)
diff_result = mymodule.subtract(a, b)

print(f"Addition of {a} and {b} is: {sum_result}")
print(f"Subtraction of {a} and {b} is: {diff_result}")


