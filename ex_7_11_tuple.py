"""
7.11 Let’s create a jump rope rhyme maker. You’ll print a series of 
two-line rhymes. Start with this program fragment:

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

For each tuple (first, second) in rhymes:

For the first line:

Print each string in start1, capitalized and followed by an exclamation point and a space.
Print first, also capitalized and followed by an exclamation point.

For the second line:
Print start2 and a space.
Print second and a period.
moderate : 20 mins
"""
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"
for (first, second) in rhymes:
    try : 
        print(" ".join([ string.upper() + "!" for string in start1 ]) + " " + first.upper() + "!")
        print(start2 + " " + second + ".")
    except: 
        print("Error")



