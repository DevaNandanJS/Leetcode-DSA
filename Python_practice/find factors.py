from math import sqrt

a= 36 
result= []

for i in range(1, int(sqrt(a))+1):
    if  a%i==0:
        result.append(i)
        if i != a//i:
            result.append(a//i)

print(f"The factors of {a} are: {result}")