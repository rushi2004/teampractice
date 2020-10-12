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
        return(" Error : Check the list of numbers that have been passed the test ")


odd_even_sum=plus_minus([10, 20, 30, 40, 50, 60])
print(odd_even_sum)

odd_even_sum=plus_minus([])
print(odd_even_sum)

odd_even_sum=plus_minus("abc")
print(odd_even_sum)