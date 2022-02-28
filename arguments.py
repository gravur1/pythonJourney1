import argparse
import sys

#######
### Getting argument details


#argumentList = sys.argv

#print("The script has the name", '"', (sys.argv[0]), "'")
#print("The number of arguments is", (len(sys.argv)))
#print("The arguments are", argumentList)


#######
### Parsing arguments

#parser = argparse.ArgumentParser()
#parser.add_argument("-display")
#args = parser.parse_args()
#print(args.display)


#######
### Parsing arguments II
ap = argparse.ArgumentParser()

ap.add_argument("--a",
                "--first_operand",
                required=True,
                help="First operand")
ap.add_argument("--b",
                "--sec_operand",
                required=True,
                help="Second operand")
args = vars(ap.parse_args())

a = int(args['a'])
b = int(args['b'])

print("Sum is {}".format(a + b))
print("Sub is {}".format(a - b))
