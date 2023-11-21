import sys

f = open(sys.argv[1],"r")
file1 = f.read()
f.close()
g = open(sys.argv[2],"r")
file2 = g.read()
g.close()
print(file1) 
print(file2)
 
if file1 == file2 :
    print(1)
else :
    print(0)    