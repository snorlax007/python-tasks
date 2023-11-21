def rev(a):
    s= len(a)
    print(s)
    str=""
    for i in range(s-1,-1,-1): 
        str += a[i]    
    print(str)
    
rev("hello world")    