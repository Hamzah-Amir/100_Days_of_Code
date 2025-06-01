try:
    l = [5,6,1,8,0]
    i = int(input("Enter your number: "))
    print(l[i])
except:
    print("Error occured")
finally:
    print("I will execute on any cause")

# Why to do this we can write that finally block of code like this & it will execute
    
# print("I will execute on any cause")

# It is used when we are using try except block inside a function liek this
def func1():
    try:
        l = [5,6,1,8,0]
        i = int(input("Enter your number: "))
        return print(l[i])
    except:
        return print("Error occured")
    finally:
        print("I will execute on any cause")  #Now it will execute the finally block on any cause
    
    print("I will execute on any cause") # This will not run in this case

func1()