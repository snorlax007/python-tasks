""" def translate():
    str = "this is fun"
    consonant = "bcdfghijklmnpqrstvwxyz"
    str2 =[]
    for i in str:
        if i not in consonant:
            str2.append(i)
        else :
            str2.append(i)
            str2.append('o')
            str2.append(i)
    print(str2)    

translate()    
"""

def translate(str) :
    vowel= "aeiou"
    a =""
    for i in str:
       if i in vowel:
          a = a + i
       else:
          a = a + i + "o" + i   
    print(a)
translate("this is fun")          