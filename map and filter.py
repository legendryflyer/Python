# program 1
lst=[2000,2001,2002,2003,2004,2005]
ages=[]
for x in lst:
    ages.append(2024-x)
print(ages)

print(list(map(lambda x:2024-x,lst)))

print([2024-x for x in lst])

# program 2
d=[12,32,454,-313,428,-214,-4124,394]
trans=[]
for x in  d:
    if x>0:
        trans.append("diposit")
    else:
        trans.append("withdrawal")
print(trans)

print(["diposit" if x>0 else  "withdrawal" for x in d ])

print(list(filter(lambda x: x>0,d)))
print(list(filter(lambda x: x<0,d)))
