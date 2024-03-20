import re #regular expression

txt = "rabbit doesnt like carrot"
rgx = "^r" #^ mathces first letter
rgx = "gr[a-z]y"#picks from a to z only one letter
rgx = "gr[a-z]y" # takes from a to z multiple charc 


result = re.findall(rgx , txt) #return list  of all
print(result)