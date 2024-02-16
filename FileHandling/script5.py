#program 3
# search the name in the file

#import os
#reclen = 10
#size = os.path.getsize('name.bin')
#n = int(size/reclen)
#with open('name.bin','rb') as f:
#    name = input("enter the name: ")
#    name = name.encode()
#    position = 0
#    found = False
#    for x in range(n):
#        f.seek(position)
#        str = f.read(reclen)
#        if name in str:
#            found = True
#            position = position + reclen

#    if found:
#        print("user available")
#    else:
#        print("user not available")



import os
reclen = 10

size = os.path.getsize('name.bin')
n = int(size/reclen)
with open('name.bin','r+b') as f:
    newname = input("enter the name: ")
    replace = input("name to replace: ")
    newname = newname + (reclen - len(newname)) * " "
    replace = replace + (reclen - len(replace)) * " "
    newname = newname.encode()
    replace = replace.encode()
    position = 0
    found = False

    for x in range(n):
        f.seek(position)
        str = f.read(reclen)
        print(str)
        print(replace)
        if str == replace:
            found = True
            break
        else:
            position = position + reclen
    if found:
        f.seek(-10,1)
        f.write(newname)
        print("name successfully replaced")
    else:
        print("name not found")
