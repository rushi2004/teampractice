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
        print(
            " ".join([ string.upper() + 
        "!" for string in start1 ]) + 
        " " + first.upper() + "!")
        print(start2 + " " + second + "."
        )
    except: 
        print("Error")
