
"""
ex_10_evens.py
7.10 Use a list comprehension to make a list called even of the even numbers in range(10).
simple: 5 mins. 
"""
even_numbers = [ num for num in range(10) if num % 2 == 0 ]
print(even_numbers)
