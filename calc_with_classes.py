def add(a , b):
    result = a + b
    return result
def sub(a , b):
    result = a - b
    return result
def mult(a , b):
    result = a * b
    return result
def div(a , b):
    result = a/b
    return result
print("welcome to calculator")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
abc = int(input("Type your value "))
a = float(input("Enter the first value "))
b = float(input("Enter the second value "))
result=0
if abc == 1:
    result = add(a , b)
if abc == 2:
    result = sub(a , b)
if abc == 3:
    result = mult(a , b)
if abc == 4:
    if b == 0:
        print("Division by zero is error")
    result = div(a , b)
print("The result is " , result)
if abc != 1:
    if abc != 2:
        if abc != 3:
            if abc != 4:
                print("Enter Proper value")
