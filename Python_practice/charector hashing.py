s= "cehlbciENZvnmbslivcwe lzvzvlhzjv j v<Ckhr v;HI 00v,m cvkh"
n= ['a', 'b', 'c', 'd', 'v', 'z', 'l', 'h', 'j', 'k', 'r', 'i', 'e', 'n', 'm']

hasg_map= {}

for i in s.split():
    if i.split():
        for j in i:
            hasg_map[j]= hasg_map.get(j, 0) + 1

for i in n:
    if i in hasg_map:
        print(f"hash list of i is {hasg_map[i]}")
    else:
        print("not in hash list")