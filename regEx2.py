import re


str = "man sun mop run"
result = re.search(r'm\w\w',str)
#print(result.group())
if result:
    print(result.group())


# program 2

str2 = "python is a good language to learn"
q = re.match(r'p\w\w',str2)
if q:
    print(q.group())
    
    
# program 3

str3 = "man ran sun fun map rap shape mate fate"
q2 = re.findall(r'a\w*', str3) # findall return a list. 
print(q2)


# program 4
str3 = "This ; is the : 'Core' python's book"
res = re.split(r'\w+',str3)
print(res)


# program 5
str4 = "i am learning javascriet and javascriet"
q4 = re.sub(r"javascriet","javascript",str4)
print(q4)    