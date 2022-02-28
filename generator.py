#generators are similar to functions but use the concept of yields other than return.
#For you to access the next object you need to use the builtin function next()

def generator():
    print("one")
    yield 1

    print("two")
    yield 2

    print("three")
    yield 3

g = generator()

print(g)

next(g)
next(g)
