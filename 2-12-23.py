#program 1
birthyear=[2000,2001,2002,2003,2004,2005]
ages=[]
for x in range (len(birthyear)):
    age=2023-birthyear[x]
    ages.append(age)
print(ages)




# program 2
marks=[11,2,33,44,55,22,66,77,88,99]
above50=[]
for x in marks:
    if x>50:
        above50.append(x)
print(above50)



# program 3
total=[11,22,33,44,55]
sum=0
for x in total:
    sum=sum+x
print(sum)




# program 4
cities = ["pune","banglore","kolkata"]
for item in cities:
    print("welcome   "+item)


