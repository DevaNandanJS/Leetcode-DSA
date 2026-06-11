n= 121
nums= n
N= 0

while nums>0:
    m=nums%10
    N= (N*10) + m
    nums= nums//10

if N == n:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")