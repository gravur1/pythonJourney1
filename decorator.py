import math

def safe_calculate(func):
    #using *args so multiple arguments by other functions can be used
    def calculate(*args):
        for arg in args:            
            if arg <= 0:
                raise ValueError("Radius cannot be negative or zero")
        return func(*args)
    return calculate

@safe_calculate
def area_rectangle_fn(length, breadth):
    return length * breadth


area_rectangle_fn(5, -9)





def asterisk_highlight(func):
    def highlight():
        print("*" * 50)

        func()

        print("*" * 50)
    return highlight

@asterisk_highlight
def printMessage():
    print("Yoohoo! Decorators are fun!!")


printMessage()