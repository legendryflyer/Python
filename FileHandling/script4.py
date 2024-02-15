# tavish anade
# 'tavish    '
# 'anade     '

reclen = 10
with open('name.bin',"wb") as f:
    n = int(input("enter the number of users: "))
    for i in range(n):
        name = input("enter the names: ")
        name = name + (reclen - len(name)) * ' '
        name = name.encode()
        f.write(name)




#program 2

reclen = 10
with open('name.bin',"rb") as f:
    n = int(input("which record to read ? "))
    f.seek(reclen * (n-1))
    str = f.read(reclen)
    str = str.decode()
    print(str)




