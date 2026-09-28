unit= input("Enter your temprature unit(C or F): ").upper().strip()
temp= int(input("enter your temprature: "))

if unit == "C":
    temp= round((temp*9)/5 +32, 1)

elif unit == "F":
    temp= round((temp-32)*5/9, 1)

else:
    print("not a valid unit")

print(f"your temprature in {unit} is {temp}")