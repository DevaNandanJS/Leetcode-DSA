n= [1, 2, 3, 4, 3, 3, 2, 1, 3, 4, 5, 6, 3, 4, 1, 2]
m= [1, 2, 3, 4, 5, 111]

hash_list= {}
for i in n:
    hash_list[i]= hash_list.get(i, 0) + 1

    print (hash_list)
    print("hashing done")
for i in m:
    if i in hash_list:
        print(f"hash list of i is {hash_list[i]}")
    else:
        print("not in hash list")

        