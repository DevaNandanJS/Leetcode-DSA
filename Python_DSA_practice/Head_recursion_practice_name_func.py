# thios is head recusrion cus the head (print function is called forst)
c = 0

def name():
    if c == 4:
        return
    
    print("Deva")
    c+= 1
    name()
    

name()
