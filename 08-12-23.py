# list comprihention
#[expression:loop:condition]
num=[1,2,3,4,5,6,7,8,9,10]
tableof2=[]
for item in num:
    tableof2.append(item*2)
print(num)
print(tableof2)


#by list comprihention
table=[item*2 for item in num ]
print(table)

# program 2
birthyear=[2000,2001,2002,2003,2004,2005,2006]
ages=[]
for x in range(len(birthyear)):
    ages.append(2023-birthyear[x])
print(ages)

ages2=[2023-x for x in birthyear]
print(ages2)


# program 3
marks=[11,2,33,44,55,66,77,889,99,110]
above40=[]
for item in marks:
    if item>40:
        above40.append(item)
print(above40)


aaabove40=[item for item in marks if item>40]
print(aaabove40)


# program 5
numbers=[2,4,6,8,10,12]
squere=[]
for item in numbers:
    squere.append(item*item)
print(squere)


sssquere=[item*item for item in numbers]
print(sssquere)







