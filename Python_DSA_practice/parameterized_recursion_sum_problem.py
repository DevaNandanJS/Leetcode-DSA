# sum of all the numbers till n 

def func(sum, i, N):
    if i>N:
        print(f"sum of numbers till {N} is {sum}") 
        return
    func(sum+i, i+1, N)

func(0,1,5)