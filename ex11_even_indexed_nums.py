"""
1)
Write a function that takes a list or tuple of numbers. Return a two-element list, 
containing (respectively) the sum of the even-indexed numbers and the sum of 
the odd-indexed numbers. 
So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60]), 
you’ll get back [90, 120].
"""

def sum_even_odd_numbers(list):
    even_indexed_sum = 0
    odd_indexed_sum = 0
    for i in range(len(list)):
        if i %2 == 0:
            even_indexed_sum += list[i]
        else: 
            odd_indexed_sum += list[i] 
    return (even_indexed_sum, odd_indexed_sum)  


print(sum_even_odd_numbers([10, 20, 30, 40, 50, 60]))     
    
