player_start_score = input('please type in the score for the players')
player_1 = int(player_start_score)
player_2 = int(player_start_score)
for x in range(0, 19):
    print ('score player 1 : ' + str(player_1))
    dart_1 = input('\n dart 1 : ')
    dart_1_per = input('\n multiply number...')
    dart_2 = input('dart 2 : ')
    dart_2_per = input('\n multiply number...')
    dart_3 = input('dart 3 : ')
    dart_3_per = input('\n multiply number...')
    temp = (int(dart_1) * int(dart_1_per)) + (int(dart_2) * int(dart_2_per)) + (int(dart_3) * int(dart_3_per))
    act_score = player_1
    if ((act_score - temp) < 0):
        print ('action NOT OK, return to default score')
    elif ((act_score - temp) == 0):
        print ('winner player1')
        break
    else:
        print ('Action OK! \n' + str(act_score) + '\n')
        player_1 =- act_score
    print ('score player 2 : ' + str(player_2))
    dart_1 = input('\n dart 1 : ')
    dart_1_per = input('\n multiply number...')
    dart_2 = input('dart 2 : ')
    dart_2_per = input('\n multiply number...')
    dart_3 = input('dart 3 : ')
    dart_3_per = input('\n multiply number...')
    temp = (int(dart_1) * int(dart_1_per)) + (int(dart_2) * int(dart_2_per)) + (int(dart_3) * int(dart_3_per))
    act_score = player_2
    if ((act_score - temp) < 0):
        print ('action NOT OK, return to default score')
    elif ((act_score - temp) == 0):
        print ('winner player2')
        break
    else:
        print ('Action OK! \n' + str(act_score) + '\n')
        player_2 =- act_score