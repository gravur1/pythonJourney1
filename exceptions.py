import time
########
### Adding specific exceptions
#try:
#    print(variable)
#except NameError:
#    print("Variable is not defined")
#except:
#    print("An unknown error happened")

########
### Adding specific exceptions
#try:
#    file = open("/home/kali/ali")
#except FileNotFoundError:
#    print("File not found")
#except:
#    print("An unknown error has occurred")

########
### Input exceptions
#while value is true

#while True:
#    try:
#        inputValue = int(input("Please enter a number: "))
#        break
#    except ValueError:
#        print("That was not a valid number")


########
### keyboard interrupt
#try:
#    time.sleep(111)
#except KeyboardInterrupt:
#    print("Keyboard interrupt has occurred")


########
### else blocks in exceptions
#try:
#    file = open("/home/kali/newfiletest.txt", 'w')
#    file.write("Testing")
#    print("Adding one line to the file: ", file.name)
#except:
#    print("Something went wrong")
#else:
#    print("Everything worked just fine")


########
### Raising exception

number = int(input("Enter a number: "))

if number > 5:
    raise Exception("The number should not exceed 5. The number you entered was:  {}".format(number))



