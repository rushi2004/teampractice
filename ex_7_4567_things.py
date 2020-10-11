"""
ex_7_4567_things.py
7.4 Make a list called things with these three strings as elements: 
"mozzarella", "cinderella", "salmonella".
simple : 5 mins 
"""
things = ["mozzarella", "cinderella", "salmonella"]


"""
ex_7_4567_things.py
7.5 Capitalize the element in things that refers to a person and then print the list. 
Did it change the element in the list? Do it two different ways using for loop and list comprehension.
modreate : 10 mins
"""
things_using_for_loop = []
for thing in things:
    if thing == "cinderella":
        things_using_for_loop.append(thing.upper())
    else: 
        things_using_for_loop.append(thing)

print(" Things in upper case using for loop ", things_using_for_loop)


things_using_list_comprehension = [thing.upper() if thing == "cinderella" else thing for thing in things  ]
print(things_using_list_comprehension)

"""
ex_7_4567_things.py
7.6 Make the cheesy element of things all uppercase and then print the list.
Do it two different ways using for loop and list comprehension. print statements must be clear. 
"""
things_cheesy_using_for_loop = []
for thing in things:
    if thing == "mozzarella":
        things_cheesy_using_for_loop.append(thing.upper())
    else: 
        things_cheesy_using_for_loop.append(thing)

print("Cheesy elements in upper case using for loop ", things_cheesy_using_for_loop)

things_cheesy_using_list_comprehension = [thing.upper() if thing == "mozzarella" else thing for thing in things  ]
print("Cheesy elements using list compreshension using for comprehsension", things_cheesy_using_for_loop)

"""
ex_7_4567_things.py
7.7 Delete the disease element from things, collect your Nobel Prize(print), and print the list.
modreate : 10 mins
"""
things.remove("salmonella")
print("I won the Nobel Prize ", things)
