#ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"


# importing the module 
import re 
  
# opening and reading the file  
with open('test.txt') as f: 
   string = f.readlines() 
  
# declaring the regex pattern for IP addresses 
#re.compile() method is used to compile a regular expression pattern provided as a string into a regex pattern
#  object (re.Pattern). Later we can use this pattern object to search for a match inside different target 
# strings using regex methods such as a re.match() or re.search()

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 
  
# initializing the list object 
list=[] 
  
# extracting the IP addresses 
for line in string: 
   list.append(pattern.search(line)[0]) 
  
# displaying the extracted IP addresses 
print(list) 

# seperate RE
  
# opening and reading the file 
with open('ip.txt') as fh: 
  string = fh.readlines() 
    
# declaring the regex pattern for valid IP addresses  
pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.) 
{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''') 
  
# initializing the list objects 
valid =[] 
invalid=[] 
  
# extracting the IP addresses 
for line in string: 
    line = line.rstrip() 
    result = pattern.search(line) 
  
    # valid IP addresses 
    if result: 
      valid.append(line) 
  
    # invalid IP addresses   
    else: 
      invalid.append(line) 
  
# displaying the IP addresses 
print("Valid IPs") 
print(valid) 
print("Invalid IPs") 
print(invalid) 