import math
import os

#print("Pi: ", math.pi)

user = os.environ["USER"]
path = os.environ["PATH"]
print("User: ", user + "\nPath: " + path)
