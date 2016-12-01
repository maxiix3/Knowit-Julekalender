for i in range(6,100000000,10):
    s = str(i)
    fin = s[len(s)-1]
    fin += s[:(len(s)-1)]
    if int(fin) == i*4:
        print i
        break
