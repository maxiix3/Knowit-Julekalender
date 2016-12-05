f = open('luke3_data.txt') 
friends = {}
hates = {} 
for line in f:
    a = line.split()
    if a[0]=='friends':
        if a[1] not in friends:
            friends[a[1]]=[]
        if a[2] not in friends:
            friends[a[2]]=[]
        friends[a[1]].append(a[2])
        friends[a[2]].append(a[1])
    else:
        if a[0] not in hates:
            hates[a[0]]=[]
        hates[a[0]].append(a[2])

highestfriend = 'someone'
highesthate = 0

for  friend in hates:
    currenthates=0
    for hated in hates[friend]:

        if hated  in  friends[friend] and friend not in hates[hated]:
            currenthates=currenthates+1
    if currenthates>highesthate:
        highestfriend=friend
        highesthate=currenthates

print highestfriend
print highesthate

