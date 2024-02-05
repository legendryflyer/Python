#for loop
# only used with range

for x in range(0,5):
    print(x)

for x in range(0,5,2):
    print(x)

for x in range(50,0,-5):
    print(x)

# break statement with for loop

for x in range(10):
    if (x==5):
        break
    print(x)


for x in range(10):
    print(x)
    if(x==5):
        break

for x in range(20,0,-2):
    if (x==10):
        break
    print(x)

#continue statement with for loop
for x in range(10):
    if (x==5):
        continue
    print(x)


for x in range(10):
    print(x)
    if(x==5):
        continue

for x in range(20,0,-2):
    if (x==10):
        continue
    print(x)
