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
#translate function to add 'o' between consonants
def translate(str) :
    #taking vowels inside a string
    vowel= "aeiou "
    a =""
    #empty string a to generate the result
    for i in str:
       if i in vowel:
           #if the letter is a vowel then add it as it is
          a = a + i
       else:
           #else add letter 'o' in between
          a = a + i + "o" + i   
    print(a)
    #extra space is added in vowel funtion to take care of spaces in the string
translate("this is fun")          
