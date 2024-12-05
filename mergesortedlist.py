a=[7,22,45,53,189]
b=[24,42,89,131]
newlist = []
def sort():
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            newlist.append(a[i])
            i=i+1
        else:
            newlist.append(b[j])
            j=j+1
    newlist.extend(a[i:])
    newlist.extend(b[j:])

sort()
print(newlist)
