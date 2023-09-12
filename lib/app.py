import ipdb

print("Hello Flatiron! Class is in session!")

def num1_and_num2_valid(num1, num2):
    if type(num1) in [int, float] and type(num2) in [int, float]:
        return True
    else:
        return False

def add(num1, num2):
    # if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
    if type(num1) in [int, float] and type(num2) in [int, float]:
    # if num1_and_num2_valid(num1, num2):
        return num1 + num2
    else:
        raise Exception('num1 and num2 must be either integers or floats')
    
def subtract(num1, num2):
    if type(num1) in [int, float] and type(num2) in [int, float]:
    # if num1_and_num2_valid:
        return num1 - num2
    else:
        raise Exception('num1 and num2 must be either integers or floats')
    
def multiply(num1, num2):
    if type(num1) in [int, float] and type(num2) in [int, float]:
    # if num1_and_num2_valid(num1, num2):
        return num1 * num2
    else:
        raise Exception('num1 and num2 must be either integers or floats')
    
def divide(num1, num2):
    if num2 == 0:
        raise Exception('num2 cannot be equal to 0')
    elif num1_and_num2_valid(num1, num2):
        return num1 / num2
    else:
        raise Exception('num1 and num2 must be either integers or floats')
    
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
        raise Exception('Operation must be either +, -, *, or /')
    
def print_greeting_loop(greeting):
    for char in greeting:
        print(char)