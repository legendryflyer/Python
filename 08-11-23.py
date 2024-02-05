# break with while
i=1
while(i<=5):
    print(i)
    i=i+1
    if(i==3):
        break


i=2
while(i<=20):
    print(i)
    i=i+2
    if(i==16):
        break


i=3
while(i<=30):
    if(i==18):
        break
    print(i)
    i=i+3


# while with continue
i=1
while(i<=5):
    if(i==3):
        i=i+1
        continue
    print(i)
    i=i+1



i=2
while(i<=20):
    if(i==14):
        i=i+2
        continue
    print(i)
    i=i+2
