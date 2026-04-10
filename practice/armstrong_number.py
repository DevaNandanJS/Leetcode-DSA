n= 153
total= 0
m= []
temp= n

while temp>0:
    m.append(temp%10)
    temp= temp//10

for i in range(0, len(m)):
    total= total+ m[i]**len(m)

if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
