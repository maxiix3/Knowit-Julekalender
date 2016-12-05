import roman
f = open("luke5_data.txt")
lines = f.readlines()
resultat = []
a = ""
for line in lines:
    line = line[1:-2].split(", ")
    for i in xrange(0,len(line)):
        if line[i] != '0':
            line[i] = roman.fromRoman(line[i])
    for i in xrange(0,(len(line)/2)):
        resultat.append(chr(int(int(line[i]) + int(line[-(i+1)]))+96))
    for i in xrange(0,len(resultat)):
        a += str(resultat[i])
    print a
