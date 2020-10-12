
things = ["mozzarella", "cinderella", "salmonella"]
things_using_for_loop = []
for thing in things:
    if thing == "cinderella":
        things_using_for_loop.append(thing.upper())
    else: 
        things_using_for_loop.append(thing)

print(" Things in upper case using for loop ", things_using_for_loop)


things_using_list_comprehension = [thing.upper() 
if thing == "cinderella"
 else thing for thing in things  ]
print(things_using_list_comprehension)



things_cheesy_using_for_loop = []
for thing in things:
    if thing == "mozzarella":
        things_cheesy_using_for_loop.append(thing.upper())
    else: 
        things_cheesy_using_for_loop.append(thing)

print("Cheesy elements in upper case using for loop ", things_cheesy_using_for_loop)

things_cheesy_using_list_comprehension = [thing.upper()
 if thing == "mozzarella" 
 else thing for thing in things  ]
print("Cheesy elements using list compreshension using for comprehsension", things_cheesy_using_for_loop)

things.remove("salmonella")
print("I won the Nobel Prize ", things)











































