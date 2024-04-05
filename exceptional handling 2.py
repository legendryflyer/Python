#  logical errors 

def avg(list):
    total=0
    for x in list:
        total += x
    avg = total/len(list)
    return avg,total

print(avg([1,2,3,4,5,6,7,8]))


try:
    a = avg([1,2])
    print(a)
except TypeError:
    print(TypeError)
except ZeroDivisionError:
    print("The length of the input is zero.")
except  Exception as e:
    print("An error occurred:",e)
finally:
    print( "This is the end")


# program 2

try:
    x = int(input())
    y = 1/x

except ZeroDivisionError:
    print("enter the number other then zero",ZeroDivisionError )
except ValueError:
    print("value should be integer ")

else:
    print("inverse is", y)

finally:
    print("End of Program")
    
    
# handiling the assertions
# program 3
try:
    x = int(input("enter the number between 5 and 10: "))
    assert x>=5 and x<10,"Number should be in range of  5 to 10"
    print("You entered ",x)
except AssertionError:
    print("the condition is not fullfield ")
    


# program 4
class lowbalance:
    def __init__(self,msg):
        self.massage = msg
        
def check(dict):
    for k,v in dict.items():
        if (v < 20000):
            raise lowbalance("low balance") 
            
try:
    data={"raj":100000,"shivani":90000,"chinmay":100000,"tavish":50000}
    check(data)
    print("all are above  20000")
except lowbalance as me:
    print(me)

