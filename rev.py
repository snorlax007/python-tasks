def rev(a):
    #taking leangth of a string
    s= len(a)
    print(s)
    str=""
    #using range function traversing from the end till -1 position (exclusive)
    for i in range(s-1,-1,-1): 
        #copying each letter
        str += a[i]    
    print(str)
    
rev("hello world")    