import sys

wordcount = 0
#reading filename from argument
f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents) 

#splitting each word from all the lines using split func()
lines = contents.split()
print(lines)

wordcount += len(lines) 

print(wordcount)