"""
ex_7_89_things.py
7.8 Create a list called surprise with the elements "Groucho", "Chico", and "Harpo".
simple : 5 mins 
"""
surpirses = ["Groucho", "Chico", "Harpo"]


"""
ex_7_89_things.py
7.9 Lowercase the last element of the surprise list, reverse it, and then capitalize it.
simple : 5 mins. 
"""
surpirses[2] = surpirses[2].lower()[::-1].upper()
print(surpirses)

