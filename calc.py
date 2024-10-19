## Basic Calculator

## Input variables -- Get the numbers from user
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
## Input variable -- Get valid Operation 
op1=input("Choose operation (+,-,*,/) :")

## Array for valid operation
oper=[ '+' ,'-', '*', '/' ]

if op1 in oper:
    if op1 == '+':
        print(num1 ,"+", num2 ,"=", int(num1+num2))
    elif op1 == '-':
        print(num1 ,"-", num2 ,"=", int(num1-num2))
    elif op1 == '*':
        print(num1 ,"*", num2 ,"=", int(num1*num2))
    elif op1 == '/':
        print(num1 ,"/", num2 ,"=", int(num1/num2))
else:
    print("Wrong operation chosen!")
    