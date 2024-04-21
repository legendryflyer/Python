# program 1
# reclan = 20
# with open ('cities.bin','wb')  as f:
#     n = int(input("enter the number of cities: "))
#     for x in range(n):
#         city = input('Enter City name : ')
#         city = city + (reclan - len(city)) * " "
#         city = city.encode()
#         f.write(city)
        
# program 2
# reclan = 20
# with open ("cities.bin",'rb') as f:
#     n = int(input("record number: "))
#     f.seek(reclan * (n-1))
#     str = f.read(reclan)
#     str = str.decode()
#     print(str)
    
    
    
# import os
# reclen = 20
# size = os.path.getsize('cities.bin')
# totalRecord = int(size/reclen)
# print("Total records available are ", totalRecord)
# with open('cities.bin', 'ab+') as filehandle:
#     city = input('enter the  city') 
#     city = city + (reclen - len(city))*" "
#     city = city.encode()
#     found = False
#     position = 0
#     for x in range(totalRecord):
#         filehandle.seek(position)
        
#         actCity = filehandle.read(reclen)
#         if city in actCity:
#             print('city found')
#             found = True
#             break
#         position = position + reclen
#     if not found:
#         print("city not found")


import os
reclen = 20
size = os.path.getsize('cities.bin')
totalRecord = int(size/reclen)
print("Total records available are ", totalRecord)
with open('cities.bin', 'r+b') as filehandle:
    rep = input('Enter record to be replaced : ')
    rep = rep + (reclen - len(rep))* " "
    rep = rep.encode()
    new_data = input('Enter the data to replace it : ')
    new_data = new_data + (reclen - len(new_data)) * " "
    new_data = new_data.encode()
    
    position = 0 
    found = False
    
    for x in range(totalRecord):
        filehandle.seek(position)
        actCity = filehandle.read() 
        if actCity == rep :
            filehandle.seek(-20,1)
            filehandle.write(new_data)
            print("Data Replaced Successfully ")
            found = True
            break
        position = position + reclen
        if not found:
            print('city not found')
