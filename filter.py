num_list = [11, 8, 7, 12, 15]

#creating a filter with the numbers greater than 10
greater_than_10 = list(filter(lambda x: x > 10, num_list))

#print(greater_than_10)

#getting even numbers
even_list = list(filter(lambda x: x % 2 == 0, num_list))
print(even_list)

