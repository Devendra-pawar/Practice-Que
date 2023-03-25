#Exercise 1: Calculator using Python 

num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
op = input("Enter the operator:")

if op == "+":
    print(f"{num1} + {num2} = {num1+num2}")
if op == "-":
    print(f"{num1} - {num2} = {num1-num2}")
if op == "/":
    print(f"{num1} / {num2} = {num1/num2}")
if op == "*":
    print(f"{num1} * {num2} = {num1*num2}")

    