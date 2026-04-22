a= 20
result= []
n= 1
while n<= a:
    if a%n == 0:
        result.append(n)
    n= n+1
print(f"The factors of {a} are: {result}")