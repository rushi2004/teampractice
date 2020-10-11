"""
13) Write a function that partly emulates the built-in zip function . 
taking any number of iterables and returning a list of tuples. Each tuple will 
contain one element from each of the iterables passed to the function. 
Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20, 'b'), (30, 'c')]. 
You can return a list (not an iterator) and can assume that all of the iterables 
are of the same length.
moderate : 10 mins
"""

def myzip(iterable1, iterable2):
    tuple_list = []
    for i in range(0, len(iterable1)):
        tuple_list.append((iterable1[i], iterable2[i]))
    return tuple_list
        


print(myzip([10, 20,30], 'abc'))
