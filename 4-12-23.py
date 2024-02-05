# program 1
birthYear = [1989,1990,1991,1992]
ages = []
for x in range(len(birthYear)):
    x=2023-birthYear[x]
    ages.append(x)
print(ages)


# program 2
marks = [22,33,44,66,7,8,99,44,66,77]
if(99 in marks):
    print("99 is available")

above50=[]
for x in marks:
    if x>50:
        above50.append(x)
print(above50)



marks3 = [88,77,88,99,88,99,00,99,00,88]
indexOf88 = []
removeEvenIndexElement = []

for item in range(len(marks3)):
    if marks3[item] == 88:
        indexOf88.append(item)

for item in range(len(marks3)):
    if(item % 2 == 0):
        continue
    removeEvenIndexElement.append(marks3[item])
print(removeEvenIndexElement)







