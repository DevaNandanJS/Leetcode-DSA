n= [1, 2, 3, 4, 3, 3, 2, 1, 3, 4, 5, 6, 3, 4, 1, 2]
m= [1, 2, 3, 4, 5, 111]

for i in m:
    count= 0

    for x in n:
        if i == x:
            count += 1

    print (f"the count of {i} is {count}")
