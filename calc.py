#simple calc
print("Type 1 for Addition")
print("Type 2 for Multiplication")
print("Type 3 for Subtraction")
print("Type 4 for Division {Decimal}")
print("Type 5 for division {Remainder}")
x = int(input("Enter Your Choice    "))
print("Enter The Two Numbers")
a = float(input("Enter the First Number    "))
b = float(input("Enter the Second Number    "))
rem = 0
if x == 1:
    res = a + b
elif x == 2:
    res = a * b
elif x == 3:
    res = a - b
elif x == 4:
    res = a / b
elif x == 5:
    res = int(a/b)
    rem = a % b
print("The Answer is" , res)
if rem != 0:
    print("The remainder is " , int(rem))
                
