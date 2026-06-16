s= [1, 2, 3, 4, 3, 3, 2, 1, 3, 4, 5, 6, 3, 4, 1, 2]
q= [1, 2, 3, 4, 5, 111]

hash_map= {}

for i in s:
    hash_map[i]= hash_map.get(i,0)+1

for i in q:
    if i in hash_map:
        print(f"the count for {i} is {hash_map[i]}")
    else:
        print(f"{i} does not have a count in the list")
