import math 

print("\n\t 🤑 Calculator \n")

num_1 = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /, %, **, //, sqrt, sin, cos, tan): ")

if operation in ("+", "-", "*", "/", "%", "**", "//"):
    num_2 = int(input("Enter the second number: "))

    if operation == "+":
        result = num_1 + num_2 

    elif operation == "-":
        result = num_1 - num_2

    elif operation == "*":
        result = num_1 * num_2

    elif operation == "%" :
        result = num_1 % num_2

    elif operation == "**":
        result = num_1 ** num_2

    elif operation == "//":
        result = num_1 // num_2
 
    else:
        result = num_1 / num_2

elif operation == "sqrt":
    result = math.sqrt(num_1)

elif operation == "sin":
    result = math.sin(math.radians(num_1))

elif operation == "cos":
    result = math.cos(math.radians(num_1))

elif operation == "tan":
    result = math.tan(math.radians(num_1))

else:
    result = "Invalid operation!"

print(f"The result is: {result}")