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

# # search()
# # findall()
# # match()
# # split()
# # sub()
# # group()

# # \w [a-z A-Z 0-9]
# # \W [not [a-z A-Z 0-9]]
# # \d - [0-9]
# # \D - not[0-9]
# # \b - blank space
# # \A - match only start of string 
# # \Z - match only at end 

# # program1 
# import re
# str = 'an apple a day keeps doctor away'
# # listA = re.findall(r'a[\w]*',str) #['an', 'apple', 'a', 'ay', 'away']
# listA = re.findall(r'\ba[\w]*',str)
# print(listA)

# # program 2
# import re 
# str = 'The meeting will be conducted on 1st and 21st of this month'
# # 1st  21st

# # program 3
# listB = re.findall(r'\b\d[\w]*',str)
# #listB = re.findall(r'\b\d[\d]*',str)
# print(listB)

# # program 4

# import re
# str = "one two three four five six seven 8 9 10"
# # [three,seven]
# listC = re.findall(r'\b\w{5}\b',str)
# print(listC)

# listC = re.search(r'\b\w{5}\b',str)
# print(listC.group())

# # listC = re.match(r'\b\w{5}\b',str)
# # print(listC.group())

# # program 5
# str = "one two three four five six seven 8 9 10"
# listD = re.findall(r'\b\w{4,}\b',str)
# print(listD)

# str = "one two three four five six seven aa 8 9 10"
# listD = re.findall(r'\b\w{3,5}\b',str)
# print(listD)


# str = "one two three four five six seven aa 8 9 10"
# listD = re.findall(r'\b\d{1,}\b',str)
# print(listD)


# str = "one two three four five six seven aa 8 9 10 two"
# listD = re.findall(r't[\w]*\Z',str)
# print(listD)


# str = "three one two three four five six seven aa 8 9 10 two"
# listD = re.findall(r'\At[\w]*',str)
# print(listD)



import re

# \w [a-z][A-Z][0-9]
# \b - blank space

# program 1
str = "an apple a day keeps doctor away"
e = re.findall(r'\ba[\w]*',str)
print(e)

# program 2
str2 = "The meeting will be conducted on 21st and 22nd and 1st"
#[21st,22nd,1st]
e2 = re.findall(r'\d[\w]*',str2)
e3 = re.findall(r'\d[\d]*',str2)
print(e2)
print(e3)

# program 3
str3 = "one two three four five aa bb six seven 8 9 10 ad44566m "
e4 = re.findall(r'\w{5}',str3)
e5 = re.findall(r'\w{4,}',str3)
e6 = re.findall(r'\w{3,5}',str3)
print(e4)
print(e5)
print(e6)

# program 4
e7 = re.findall(r'\d{1,}',str3)
e8 = re.findall(r'\b\d{1,}\b',str3)
print(e7)
print(e8)

#program 5 
str3 = "one two three four five six seven eight nine ten"
e9 = re.findall(r't[\w]*\Z',str3)
print(e9)
e10 = re.findall(r'\Ao[\w]*',str3)
print(e10)

# program 6

str4 = "ChinmayDeshpande:7709192441"
e5 = re.search(r'\d+',str4)
print(e5.group())

#a[\w]*   #a apple a day keeps doctor away  
#a\w+

a = 'apple a day keeps doctor away' 
print(re.findall(r'a\w+',a))
print(re.findall(r'a[\w]*',a))











# program 1
import re
str = "anil akhil anant an ak arun arati arundhanti abhjit ankur"
e = re.findall(r'\ba[nk][\w]*\b',str)
print(e)

# program 2
# dd-mm-yy

str = 'chinmay 7-11-1989 ,amol 19-08-1990 mayuri 21-2-1990 poorva 29-10-93 shivani 27 april 1994'
e = re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str)
d = re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(e)
print(d)

# program 3

str = "Hello world"
e = re.search(r'^he',str)
if e:
    print("string starts with He")
else:
    print("string does not starts with He")


str = "Hello world .. i am from India"
e = re.search(r'from India$',str)
if e:
    print("str ends with dia")
else:
    print("string does not end with dia")

# program 4 
str = "Hello WoRld"
e = re.search(r"world$",str,re.IGNORECASE)
if e :
    print("ends with world")
else:
    print('does not end with world')

# program 5
str2 = "Rahul got 95 marks , Vijay got 89 marks Chinmay got 60 marks"
f = re.findall(r'\d{1,2}',str2)
print(f)

g = re.findall(r'[A-Z][a-z]*',str2)
print(g)

# program 6
str3 = "The meeting will start at either 9am or 9pm else at evening 6pm"

# search - firstOccurence
# match - start of string 
# findall - all occurences