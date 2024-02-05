# list comprihention
#[expression:loop:condition]
x=[1,2,3,4,5,6,7,8,9,10]
tableof2=[]
for item in x:
    tableof2.append(item*2)
print(tableof2)

table=[item*2 for item in x]
print(table)

#program 2
birthyear=[2000,2001,2002,2003,2004,2005,2006]
age=[]
for item in birthyear:
    age.append(2023-item)
print(age)
ages=[2023-item for item in birthyear]
print(ages)


#program 3
marks=[11,22,33,44,55,66,77,88,99,110]
above50=[]
for item in marks:
    if item>50:
        above50.append(item)
print(above50)

ab50=[item for item in marks if item>50]
print(ab50)


#program 4
names=["tavish","chainmay","aman","ankit","shryenshi","vaidahi","kirtish"]
first=[]
for item in names:
    first.append(item[0])
print(first)

fl=[item[0] for item in names]
print(fl)


#program 5
h1=[11,2,33,457,3795,89,98,77,88,99,400,839,98,9487,948,834808,49384,20]
a1=[]
for item in h1:
    if item % 2 == 0:
        a1.append("even")
    else:
        a1.append("odd")
print(a1)


h=["even" if item % 2==0 else "odd" for item in h1 ]
print(h)

