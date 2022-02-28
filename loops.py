
#for letter in ['a', 'b', 'c', 'd']:
#    print(letter)

#str="Hello World"

#for char in str:
#    print(char)

#for country in "Germany", "India", "Israel":
#    print(country)

#scan the list and print the dogs name and weight
dog_weight = (("Pug", 20),
               ("Doberman", 80),
               ("Golden", 55))

for i, (dog, weight) in enumerate(dog_weight):
    print("The dog at index %d is a %s and it weigths %s pounds" % (i, dog, weight))


#for i in range(6):
 #   print(i)

#for i in reversed("welcome"):
#    print(i)

#break statement
#for letter in "python":
#    if letter == "h":
#        break
#    print(letter)


#continue statement
#for letter in "string":
#    if letter == "i":
#        continue
#
#    print(letter)
#
#print("\nThe end")


numDays = [31,28,31,30,31,30,31,31,31,30,31,30,31]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dez"]

newDict = dict()

for i,j in zip(months, numDays):
    newDict.update({i:j})

    if newDict[i] < 29:
        continue

    else:
        print(i, "has", newDict[i], "days")


#pass statement
x=5
if(x == 5):
    pass #the pass does not do anything, but it is useful when something needs to be added to a condition for ex.




