city = input('where do you live: ')
city = city.upper()
#print(city)
#check=city.startswith("G")
#print(check)

#
#if check == True: 
#	print("yep")
#else:
#	print("no")


#checking finding string

findCheck=city.find('VAT')
print(findCheck)
if findCheck > 0 :
	print("VAT is present in your string")
else:
	print("VAT is not present in your string")
