s= "axanciebsksomecoemaancein"
q= ["a","b","c","e","i","o","s","m","n","k","x","p"]

hash_map= {}

for i in s:
    hash_map[i]= hash_map.get(i, 0)+1

for i in q:
    if i in hash_map:
        print(f"Count of {i} is {hash_map[i]}")
    else:
        print(f"Count of {i} is 0")