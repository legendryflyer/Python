#  types of error 
# compile error 
# runtime error 
#  logical error 




# compile time
# def add(x, y):
#     return x + y

# print(add(1,2))


# Run time error 
# a=int(input())
# b=int(input())
# x=a/b

# if b=0 it will throw the error |  ArithmeticError: division by zero one of the runtime error

# def calculateBonusPlusSalary(salary):
#     return 0.10 * salary
# print(calculateBonusPlusSalary(1000))
# print("hello")
# try:
#     x = int(input("Enter the value 1 "))
#     y = int(input("Enter the value 2 "))
#     print(x/y)
# except Exception:
#     print('Invalid input')
# print("bye")    






# print("hiiii")
# try:
#     names = ["tavish","ankit","amit"]
#     x = int(input("Enter the value 1 "))
#     y = int(input("Enter the value 2 "))
#     print(x/y)
#     print(names[2])
#     print(a)

# except ArithmeticError:
#     print('Invalid input')
# except IndexError:
#     print("increase value of your list")
# except NameError:
#     print("not defined")
# except Exception:
#     print("something went wront")
# print("bye")



print("hiiii")
try:
    names = ["tavish","ankit","amit"]
    x = int(input("Enter the value 1 "))
    y = int(input("Enter the value 2 "))
    print(x/y)
    print(names[2])
    print(a)

except ArithmeticError:
    print('Invalid input')
except IndexError:
    print("increase value of your list")
except NameError:
    print("not defined")
except Exception:
    print("something went wront")
else:
    print("if try is not executed i will  execute")
    
finally:
    print("i will always execute")
    
    
    
    
#  a single try block  can have multiple except blocks.
#  multiple except blocks  can handle different types of errors.
#  finally block is always executed whether an error occurs or not.
#  we can not write except block without try block.
#  if there are no errors in try block then it will directly go to else part and then to the end part
#  if there are any errors in try block then it will first check for which type of exception it matches with the except block.
#  finally block is always  executed whether an error occurs or not.

