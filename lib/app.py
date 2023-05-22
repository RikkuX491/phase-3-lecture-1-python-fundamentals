import ipdb

print("Hello Flatiron! Class is in session!")

def add(num1, num2):
    if (type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 + num2
    else:
        raise Exception("num1 and num2 must be integers or floats")

def subtract(num1, num2):
    if (type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 - num2
    else:
        raise Exception("num1 and num2 must be integers or floats")

def multiply(num1, num2):
    if (type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 * num2
    else:
        raise Exception("num1 and num2 must be integers or floats")

def divide(num1, num2):
    if (type(num1) in [int, float]) and (type(num2) in [int, float]) and (num2 != 0):
        return num1 / num2
    else:
        raise Exception("Invalid input!")

def calculator(operation, num1, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        raise Exception("Invalid operation!")
    
def print_greeting_loop(greeting):
    index = 0
    while(index < len(greeting)):
        print(greeting[index])
        index += 1