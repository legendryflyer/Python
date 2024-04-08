#  program 1
f = open(input("enter the file name: "),'+a')
print("enter '@' to exit")
while str != '@':
    str = input("names to add in the file: ")
    if str != '@':
        f.write("\n" + str + "\n")
print(str)
f.close 
     