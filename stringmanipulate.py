list= ["Hello World","ggwp","radar","good morning","i have to go now","xerox"]
newlist=[]
def operations(list):
    count=0
    for string in list:
        if len(string)>2 and string[0]==string[len(string)-1]:
            count=count+1   
    
        if len(string)>=3:
            if string.endswith("ing"):
                string+= "ly"
        
            else:
                string+= "ing"  
        newlist.append(string)
    
operations(list)
print(newlist)
