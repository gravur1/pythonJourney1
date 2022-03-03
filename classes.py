########
#### Initial stuff

#class Student():
#    pass

#object1 = Student()
#print(type(object1))
#print(isinstance(object1, Student))


########
#### Class Methods
class Student:
    def __init__(self, name):
        print("Initialize called")
        self.name = name
        self.email = name + "." + "@company.com"
        print("your email is: ", self.email)

s1 = Student("Tiago")