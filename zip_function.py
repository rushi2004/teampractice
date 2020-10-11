
def my_zip(iterable1, iterable2):
    tuple_list = []
    for i in range(0, len(iterable1)):
        tuple_list.append((iterable1[i], iterable2[i]))
    return tuple_list

print(my_zip([10,20,30], 'abc')) 