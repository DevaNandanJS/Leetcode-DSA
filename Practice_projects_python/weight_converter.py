#  weight converter script
weight= int(input("Enter your weight: "))
unit= input("Enter your unit(kg or lbs): ").lower().strip()

if unit == "kg":
     weight= weight* 2.205
     unit= "lbs"

elif unit == "lbs":
     weight= weight/2.205
     unit= "kg"

else:
     print("you did not enter a valid weight unit")

print(f"your weight is {weight} in {unit}")
