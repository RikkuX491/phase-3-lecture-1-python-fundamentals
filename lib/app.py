import ipdb

print("Hello Flatiron! Class is in session!")

def add(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 + num2
    else:
        raise Exception("num1 and num2 must be numbers")
    
def subtract(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 - num2
    else:
        raise Exception("num1 and num2 must be numbers")
    
def multiply(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]):
        return num1 * num2
    else:
        raise Exception("num1 and num2 must be numbers")
    
def divide(num1, num2):
    if(type(num1) in [int, float]) and (type(num2) in [int, float]) and (num2 != 0):
        return num1 / num2
    else:
        raise Exception("Invalid input!")
    
def calculator(operator, num1, num2):
    if(operator == '+'):
        return add(num1, num2)
    elif(operator == '-'):
        return subtract(num1, num2)
    elif(operator == '*'):
        return multiply(num1, num2)
    elif(operator == '/'):
        return divide(num1, num2)
    else:
        raise Exception("Invalid operator!")
    
def print_greeting_loop(greeting):
    for character in greeting:
        print(character)

people = [
    {
        "first_name": "Alice",
        "last_name": "Baker",
        "age": 20
    },
    {
        "first_name": "Bruce",
        "last_name": "Wayne",
        "age": 34
    }
]

#ipdb.set_trace()
