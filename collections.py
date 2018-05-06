#-------------------------------------------
'''
List functions
1. append()
2. pop()/pop(index) -> last or from index 
3. sort() 
4. reverse() 
5. copy() -> return a shallow copy
6. count(x) -> # of times x appears in list

Other things:
1. slicing 
    list[be:en] excludes en 
    list[be:] from be -> en
    list[:en] from be -> en - 1
    list[:] copy of entire array 
    
    list[be:step:en]
    
Additionally negative indices are used for slicing 
Slicing also works on string
'''
def stack_use():
    # Using a list as a stack 
    stack = [1, 2, 3, 4]

    stack.append(5)
    stack.pop()

'''
Using Queue as Dequeue 

1. append()
2. appendLeft()
3. pop()
4. popleft()
''' 

from collections import deque

def queue_use():
    q = deque(["Erlang", "Elixir", "Haskell"])
    q.append("OCaml")
    q.popleft()
    
    print(q)

#-------------------------------------------
'''
Priority queue 

By default is min heap.
To make a max heap user heapq._heapify_max

1. heapq.heappush(heap_obj, item)
2. headq.heappop(heap_obj)
3. heapq.heapify()
4. heapq.nlargest(n, iterable)
    iterable could be a list, tuple etc

'''
import heapq

def heap_use():
    heap = [2, 1, 3, 5]
    heapq.heapify(heap)
    print(heap)

#-------------------------------------------
'''
Sets 

Two ways to create a set - 

    set1 = {1, 2, 3, 3}
    set2 = set() #creates an empty set 

Functions 
1. element in set -> used to check membership
   element not in set
2. add() adds element to set 
3. union, intersection, difference
    You can also use -> |, &, - instead of function names 

FROZENSET - an immutable set 
'''
def sets_use():
    graph = {'AB', 'BC', 'CD'}
    edge = 'DA'
    print(edge in graph)
    graph.add(edge)
    print(edge in graph)
    
    graph_immutable = frozenset(graph)
    print(graph_immutable)
    
#-------------------------------------------
'''
Maps/Dictionaries

hashMap = {key: value}

key in hashMap -> check membership

hashMap[key] -> to access value at key. Use same
syntax to add new value in map
'''

def hashmap_use():
    weather_cache = {'today':'74', 'tomorrow':'85'}
    
    print('today' in weather_cache)
    weather_cache['yesterday'] = '72'
    print(weather_cache)
#-------------------------------------------

hashmap_use()
