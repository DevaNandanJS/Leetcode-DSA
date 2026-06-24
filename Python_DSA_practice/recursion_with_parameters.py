# print numbers from 1 to 15

def func(n):
    if n==0: 
        return
    print(n)
    func(n-1)

func(5)