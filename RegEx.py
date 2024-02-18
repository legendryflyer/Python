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



