pakker = list(map(int, open("godteri.txt").read().split(",")))
alver = 127
total = sum(pakker)
i = -1

while (total % alver != 0):
    total -= pakker[i]
    i -= 1

print(total)
print(total / alver)

