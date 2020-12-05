import numpy as np

words = open("words.txt").read().splitlines()
words2 = open("words.txt").read().splitlines()

matrix = np.genfromtxt("input.txt", dtype='U', delimiter=1)

def findword(word):
    lenght = len(word)
    wordarray = list(word)

    # finner kordinater til første bokstaven av ordet.
    result = np.where(matrix == word[0])
    cordinates = list(zip(result[0],result[1]))

    print("########### Working on: " ,word)
    for cord in cordinates:
        # ned
        if cord[0]+lenght <= 1000:
            l = [matrix[cord[0]+i,cord[1]] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # opp
        if cord[0]-lenght+1 >= 0:
            l = [matrix[cord[0]-i,cord[1]] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # høyre
        if cord[1]+lenght <= 1000:
            l = [matrix[cord[0],cord[1]+i] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # venstre
        if cord[1]-lenght+1 >= 0:
            l = [matrix[cord[0],cord[1]-i] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # diagonal ned høyre
        if cord[0]+lenght <= 1000 and cord[1]+lenght <= 1000:
            l = [matrix[cord[0]+i,cord[1]+i] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # diagonal ned venstre
        if cord[0]+lenght <= 1000 and cord[1]-lenght+1 >= 0:
            l = [matrix[cord[0]+i,cord[1]-i] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # diagonal opp høyre
        if cord[0]-lenght+1 >= 0 and cord[1]+lenght <= 1000:
            l = [matrix[cord[0]-i,cord[1]+i] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break
        # diagonal opp venstre
        if cord[0]-lenght+1 >= 0 and cord[1]-lenght+1 >= 0:
            l = [matrix[cord[0]-i,cord[1]-i] for i in range(lenght)]
            if wordarray[:] == l:
                words.remove(word)
                print("--------------removed :",word)
                break

for word in words2:
    findword(word)

words.sort()
print("%s,%s,%s" %(words[0],words[1],words[2]))
