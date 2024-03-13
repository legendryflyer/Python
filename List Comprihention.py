#list comprihention

lst=[2000,2001,2002,2003,2004,2005]
ages=[]
for x in lst:
    ages.append(2024-x)
print("Ages are",ages)
#using list comprehension to make the code
ages_new=[2024-x for x in lst]
print(ages_new)


numbers=[1,2,3,4,5,6,7,8,9,10]
sq=[]
for x in numbers:
    sq.append(x*x)
print(sq)
sqr=[x*x for x in numbers]
print(sqr)


# print all even from sqr
even=[x for x in sqr if x%2==0]
print(even)

# print all odd from sqr 
odd=[x for x in sqr if x%2!=0]
print(odd)

# output should bee ["even,"odd","odd"]

a=["even" if x%2==0 else "odd" for x in sqr]
print(a)