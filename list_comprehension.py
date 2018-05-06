#-------------------------------------------
# List Comprehension Examples 

# Generate a list of squares 
my_list = [1, 2, 3, 4] 
print([n for n in my_list])

# Generate a list of even numbers below 20 
print([n for n in range(20) if n%2 == 0])

# Above with map/filer
'''
Map/Filter usually have the first argument as the list, and the second 
argument is the function to be applied on the list 
Python kind of has this reversed
'''

my_list2 = filter(lambda n: n%2 == 0, range(20))
print(list(my_list2))

# List Comprehension more examples 
l = [n*n for n in range(20) if n%2 == 0]
# Nested loop
l2 = [(x,y) for x in range(3) for y in range(3)]
print(l2)