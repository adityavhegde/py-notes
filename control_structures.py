#-------------------------------------------
# FOR LOOPS 
def normal_increment():
    # this is like for(i = 0; i <6; i++)
    for idx in range(6):
        # Prints Hello 5 times 
        print("Hello", idx)

def increment_by_2():
    # The last argument to range is the increment by 
    for idx in range(0,6,2):
        print(idx)

def string_loop():
    # Iterate through each character in the string
    for ch in "Hello World":
        print(ch)

def list_iterate():
    list1 = ["a",1,3] # List
    tuple1 = ("a", 1, 2) # Tuple
    
    for elt in list1:
        print(type(elt))
    
    for elt in tuple1:
        print(elt)

def list_reverse():
    listL = [1, 2, 3]
    for l in reversed(listL):
        print(l)

def str_rev():
    str1 = "Hello"
    for c in reversed(str1): print(c)
    
def indexed_for():
    # Use enumerate to get index
    # Below map with list compr. [n+20 for n in range(10)]
    for index, val in enumerate(map(lambda n: n+20, range(10))):
        print(index, val)
#-------------------------------------------
# WHILE LOOPS   

def sum_counter():
    '''
    Above while loop is probably not Python best used 
    An alternative way could be: 
        print(sum(range(5,10)))
    '''
    sumVals = 0
    pos = 5
    # You can skip the brackets here 
    while (pos < 10):
        sumVals += pos 
        pos += 1

    print(sumVals)

#-------------------------------------------
# IF/ELSE
def make_sandwich(preference = ''):
    preference = preference.lower()
    if preference == 'vegan':
        print('Skip chicken and dairy')
    elif preference == 'vegetarian':
        print('Skip chicken')
    else:
        print('Add an extra chicken tender')
      
#-------------------------------------------
# ITERABLE

'''
dir(list/tuple) gives a list of functions on that variable 
For lists, we have iter(), next()

These are like Iterator and hasNext() in Java 

iter(list/tuple) gives the iterator, which at any point, points to 
one element of the list/tuple 

next(iter) -> calling next on iter advances this.

Defining these functions for a class, enables you to create an iterator 
''' 

#-------------------------------------------
# GENERATORS

'''
Generators allow you to write functions that behave as 
iterators 

To write a generator function we use the yield statement

LAZY EVALUATION
The yield statement, does not generate and store all values in 
memory, but does a lazy evaluation -- bringing in values in memory 
when required

NOTE: Iterators are also a generator pattern

next() can be used to get next value of a generator

Use () in list comprehension to create a generator 

Use list(gener_obj) to convert generator to list 
'''

# Without generator
inputs = [10, 20, 30, 35, 45]

def without_generator():
    #find numbers divisible by 2 
    ret_val = []
    for val in inputs:
        ret_val.append(val%2)
    return ret_val

def with_generator():
    for val in inputs:
        yield(val%2)

def use_generator():
    for val in with_generator():
        print(val)
#-------------------------------------------
# EXECUTION SECTION    
make_sandwich()
indexed_for()

