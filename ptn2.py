import re
string= "This   is  a   python  program.Indeed!"

def spacing(x):
    result = re.sub(r"\.(\w)", r". \1", string)
    
    result2 = re.sub("\s+"," ",result)
    if result2:
        print(result2)

spacing(string)
