# [\w]--- [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# [\W] --- " " and special symbol
# [\w]* zero or more repetitions
# \d  -- represents only digits
# \b -- only blank space

# program 1    # seacrh()


import re
str = 'cat dog tav ana sun run moo'
# \w--->[A-Z a-z 0-9]
e = re.search(r'm\w\w',str)
f = re.search(r'\wun',str)

if e:
    print(e.group())
else:
    print("match not found !")

if f:
    print(f.group())
else:
    print("match not found")

# program 2
strB = "man sun mop run mat fat cat sat"
q = re.search(r'\w\wp',strB)

if q:
    print(q.group())
else:
    print("not found")

q2 = re.findall(r'm\w\w',strB)
q3 = re.findall(r'\wat',strB)

print(q2,q3)


# program 3           # match
strC = "mon tue wed thu fri sat sun "
q4 = re.match(r's\w\w',strC)

if q4:
    print(q4.group())
else:
    print("match not found")

# program 4
strD ="this is the 'core' python cammunity"
# \w --->[A-Z a-z 0-9]
# \W ---> non-alphanumeric
q5 = re.split(r"\W+",strD)
print(q5)



info = "I am tavish anade and I am not related to any thing"
print(re.split(r"\W+",info))

# program 5
strE = "I am learning JavaScript"
q6 = re.sub(r'JavaScript','Python.',strE)
print(q6)


#program 6
# [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# [\W] --- " " and special symbol
# [\w]* zero or more repetitions
# \d  -- represents only digits
# \b -- only blank space

str1 = "an apple a day keeps a doctor away"
e1 = re.findall(r"\ba[\w]*",str1)
print(e1)


# program 7
str2 = "the meeting will be conducted on 1st and 21st of each month"
e2 = re.findall(r'\d[\w]*',str2)
print(e2)


# program 8
str3 = "one two three four five six seven 8 9 10"
e3 = re.findall(r'\w\w\w\w\w',str3)
print(e3)
e4 = re.findall(r'\b\w{5}',str3)
print(e4)


# program 9
str4 = "one two three four five six seven 8 9 10 "
e5 = re.findall(r'\b\w{3,5}\b',str4)
print(e5)

# program 10
str5 = "one two three four five sir seven nineteen 8 9 10"
e6 = re.findall(r'\b\w{4,}',str5)
print(e6)


# program 11
str6 = "one two three four five six seven nineteen 8 9 10"
e7 = re.findall(r'\b\d{1,}\b',str6)
print(e7)
e8 = re.findall(r'\b\d+\b',str6)
print(e8)

# program 12
# a regular expression to find last word starting with 's'
# a regular expression to find last word starting with 'o'
str6 = "o one two three four five six seven seventeen two"
# '\Z' 0 end of string
# '\A' start of string

e9 = re.findall(r'\bs[\w]*\Z',str6)
e10 = re.findall(r'\A\bo[\w]*',str6)
print(e10)
print(e9)


# program 13
str = "tavish anade:828689631"
print(str)
e = re.search(r'\d+',str)
print(e.group())



#  '\w'  --> [A-Z a-z  0-9]
#   '\W' --> Non alphanumeric
#   '\d' --> digit
#   '\D' --> non-digit


e = re.search(r'\D+',str)
print(e.group())

f = re.search(r'[\w]* [\w]*',str)
if f:
    print(f.group())
else:
    print("pattern not found")


# program 14
str = " tavish ankit amit aman kirtish"
g = re.findall(r'\ba[am][\w]*',str)
print(g)

# program 15
str = 'chinmay 07-11-1989 amol 19-09-1990 mayuri 21-01-1989'
f = re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(f)

# program 16
str  = "hello world"
g = re.search(r'^he',str)
print(g.group())

# program 17
str  = "hello world"
g = re.search(r'world$',str)
print(g.group())

#program 19
str  = "hello World"
g = re.search(r'world$',str,re.IGNORECASE)
print(g.group())

# program 19
students = "I got 80 marks I got 100 marks"
print(re.findall(r'\d{2,3}',students))


students = "Amol got 80 marks Mayuri got 100 marks"
f = re.findall(r'[A-Z][a-z]*',students)
print(f)


# program 20
string= "the morning meeting will be at 8am or 9am , evening at 8pm or 9pm"
#output [8am,9am,8pm,9pm]
#h = re.findall(r'\b\d[/w]*',string)
#print(h)

l = re.findall(r'\b\d[ap][\w]*',string)
print(l)

