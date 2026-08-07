n= 1,2,3,4,5,6,7,8,9
t= 6
out= []
for i in range(0,len(n)):
    for j in range (i+1,len(n)):
        if n[i] + n[j] == t:
            out.append(n[i])
            out.append(n[j])
print(out)