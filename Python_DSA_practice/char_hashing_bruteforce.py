s= "axanciebsksomecoemaancein"
q= ["a","b","c","e","i","o","s","m","n","k","x"]

hash_list= [0]*26

#since ascii values of alphas is from 97 to 122
for i in s:
    asci_val= ord(i)
    hash_list[asci_val-97]+= 1

for i in q:
    asci_val=ord(i)-97
    print(f"Count of {i} is {hash_list[asci_val]}")
    