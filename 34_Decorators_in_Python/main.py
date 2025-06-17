def greet(func):
    def mfunc(*args,**kwargs):
        print("Hello, how are you")
        func(*args, **kwargs)
        print("Thanks for using this program")
        mfunc


def multiply(a,b):
    return a*b

greet(multiply)(5,6)