print("\nThis script receives two strings and returns the common characters between them \n")

string1 = input("Enter first string: ")
string2 = input("Enter sec string: ")


set1 = set(string1)
set2 = set(string2)

commonChar = set1.intersection(set2)
sortedValue = sorted(commonChar)

print("\nCommon letters: ", list(sortedValue))
