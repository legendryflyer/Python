#compile time error
#runtime error 
#logical error 

# program 1 
def add(x,y):
    print(x+y)
add(1,2)


# program 2
#x = input("Enter the number one")
#y = input("Enter the number two")
#print("hello")
#print(int(x)/int(y))
#print("bye")


# program 3
def calci(age):
    return age
a=calci(20)
print(a)

# program 4
#print("hell")
#print(10/0)
#print("bye")




print("hellow")
try:
    print(10/0)
except Exception:
    print("division by zero")
print("hellow")



print("shcjaef")
try:
    print(10/0)
except Exception:
    print("division  by  zero")
else:
    print("bye")
finally:
    print("tavish")




# error handling using try...catch


a = 100

try:
    b = 0
    c = a / b
    name = "TAVISH"
    print(c)
    print(name[1])
except ZeroDivisionError as e:
    print("Something went wrong", e)
except IndexError as e:
    print("Something went wrong", e)
else:
    print("Complete Code executed successfully")
finally:
    print("This will always be executed")
print(a)

print("Hello World")

# custom Exception
# raising  user defined Exceptions

# x = 11
# print(x%2!=0)

# if x%2!=0 :
#   raise Exception("Enter even Number Only")
# else:
#   print("Entered num is even")


current_year = 2023
year_born = 2990

# if year_born>current_year:
#   raise Exception("INVALID YEAR OF BIRHT")
# else:
#   age = current_year - year_born
#   print(age)


try:
    if year_born > current_year:
        raise Exception("INVALID YEAR OF BIRHT")
    else:
        age = current_year - year_born
        print(age)
except:
    print("Some Error Occured")






a = 100
b = 200
# b = 0 #user input
c = a/b #ZeroDivisionError: division by zero
print(a)
print(b)
print(c)

name = "PALLAVI"
print(name)
print(name[0])
# print(name[10])#IndexError: string index out of range

print("Hello World")


# syntax

# try:
#   code
# except:
#   code
# except:
#   code
# else: # if no error in the code i.e with no exceptions
#   code
# finally:
#  code

a = 100

try:
  b = 0
  c = a/b
  print(c)
except:
  print("Something went wrong !!!")




name = "PALLAVI"
print(name)

try:
  print(name[10])
except:
  print("Something went wrong !!!")

print("Hello World")


# https://docs.python.org/3.12/library/exceptions.html#exception-hierarchy


#  adding more info to the  user/code
try:
  b = 0
  c = a/b
  print(c)
except Exception as i_am_error:
  print("Something went wrong !!!", i_am_error)


try:
  print(name[10])
except Exception as e:
  print("Something went wrong !!!",e)

print("Hello World")



# catching multiple exceptions

try:
  b = 100
  c = a/b
  print(c)
  print(name[3])
except Exception as e:
  print("Something went wrong !!!",e)
except Exception as f:
  print("Something went wrong !!!",f)
else:
  print("No error found")
finally:
  print("This line will always get excecuted !!!")






