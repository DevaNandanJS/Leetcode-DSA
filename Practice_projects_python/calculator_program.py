operator= input("Enter your operator (+,-,*,/)").strip()
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

if operator == "+":
    print(num1+num2)

elif operator == "-":
    print(num1-num2)

elif operator == "/":
    result= num1/num2
    print(round(result))
else:
    print(num1*num2)

