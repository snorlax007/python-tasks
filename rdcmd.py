import sys

wordcount = 0
f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents) 
lines = contents.split()
print(lines)

wordcount += len(lines) 

print(wordcount)