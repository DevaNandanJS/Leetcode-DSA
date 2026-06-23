# print numbers from 1 to 15
i=1
n=15
def counts(i,n):
    if i>n:
        return
    print(i)
    counts(i+1,n)

counts(i,n)