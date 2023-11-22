import sys
#filename from first argument is taken and opened in read mode
f = open(sys.argv[1],"r")
file1 = f.read()
f.close()

# second file taken in the same way
g = open(sys.argv[2],"r")
file2 = g.read()
g.close()
print(file1) 
print(file2)

 #comparing both files
if file1 == file2 :
    print(1)
else :
    print(0)    
