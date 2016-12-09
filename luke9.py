f = open("luke9_data.txt")
counter = 0
person = {}
lines = f.readlines()
for line in lines:
    line = line.strip().split(',')
    person[line[1]] = 0
    if line[0] != "None" : person[line[0]] = 0
for line in lines:
    line = line.strip().split(',')
    if line[0] == "None":
        person[line[1]] += int(line[2])
    else:
        person[line[0]] -= int(line[2])
        person[line[1]] += int(line[2])

for keys,values in person.items():
    if values > 10:
        counter += 1

print counter
