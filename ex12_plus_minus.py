"""
12) Write a function that takes a list or tuple of numbers. Return the result of alternately 
adding and subtracting numbers from each other. So calling the function as 
plus_minus([10, 20, 30, 40, 50, 60]), you’ll get back the result of 
10+20-30+40-50+60, or 50.
modreate : 10 mins. 
"""

def plus_minus(list):
    if len(list) == 0: 
        return 0
    sum = list[0]
    try: 
        for i in range(1, len(list)):
            if i % 2 == 1:
                sum += list[i]
            else: 
                sum -= list[i]
        return sum
    except: 
        return("Error : Check if the list of numbers have been passed")


odd_even_sum=plus_minus([10, 20, 30, 40, 50, 60])
print(odd_even_sum)

odd_even_sum=plus_minus([])
print(odd_even_sum)

odd_even_sum=plus_minus("abc")
print(odd_even_sum)
