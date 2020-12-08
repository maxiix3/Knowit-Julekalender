numbers = sorted(map(int, open("numbers.txt").read().split(",")))

for i in range(len(numbers)):
    if int(numbers[i]) != i+1:
        print("number missing: %d" % (i+1))
        break
