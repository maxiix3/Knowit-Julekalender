def day7():
    f = open("luke7_data.txt")
    lines = f.readlines()
    x=0
    y=0
    for line in lines:
        splitted = line.strip().split(" ")
        a=int(splitted[1])
        if splitted[3] == "north":
            y += a
        elif splitted[3] == "east":
            x -= a
        elif splitted[3] == "south":
            y -= a
        elif splitted[3] == "west":
            x += a
    return x,y

x,y = day7()

print y,x
