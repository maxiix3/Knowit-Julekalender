def luke8():
    f = open("luke8_data.txt")
    lines = f.readlines()
    players = [1] * 1337
    stig = 0
    player = 0
    stairs = [[3,17], [8,10], [15,44], [22,5], [39,56], [49,75], [62,45], [64,19], [65,73], [80,12], [87,79]]
    for line in lines:
        players[player] += int(line)
        if players[player] > 90:
            players[player] -= int(line)
        elif players[player] == 90:
            print "Spiller %i vant stigespillet! Det ble gaatt i %i stiger" %(player+1,stig)
            print "svar = %i" %((player+1)*stig)
            return
        for stair in stairs:
            if players[player] == stair[0]:
                players[player] = stair[1]
                stig += 1
        player += 1
        if player == 1337:
            player = 0

luke8()
