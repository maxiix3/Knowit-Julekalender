
f = open("input.txt").readlines()

melk = 0
egg = 0
mel = 0
sukker = 0
for i in f:
    linje = i.strip().split(", ")
    linje = [i.split(":") for i in linje]
    for vare in linje:
        if vare[0] == "melk":
            melk += int(vare[1])
        if vare[0] == "mel":
            mel += int(vare[1])
        if vare[0] == "egg":
            egg += int(vare[1])
        if vare[0] == "sukker":
            sukker += int(vare[1])
print(min(melk/3, mel/3, egg/1, sukker/2))

