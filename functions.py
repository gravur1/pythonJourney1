def tiago():
    print("Hello dude, whats up")
    print("here I am")

#tiago()


#function documentation
def documented_function():
    """ This function does something that is well documented """
    print("Hello")

#documented_function()

#printing function documentation
#print(documented_function.__doc__)

def returnName(name):
    print("Your name is", name)

name = input("provide your name: ")

returnName(name)