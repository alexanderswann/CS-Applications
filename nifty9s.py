from random import *
player1cards= []
player2cards=[]
player3cards=[]
playedcards=[]
turn = [0]
reverse = []
cards=[[0,"blue"],[0,"green"],[0,"yellow"],[0,"red"],[1,"blue"],[1,"green"],[1,"yellow"],[1,"red"],[2,"blue"],[2,"green"],[2,"yellow"],[2,"red"],[3,"blue"],[3,"green"],[3,"yellow"],[3,"red"],[4,"blue"],[4,"green"],[4,"yellow"],[4,"red"],[5,"blue"],[5,"green"],[5,"yellow"],[5,"red"],[6,"blue"],[6,"green"],[6,"yellow"],[6,"red"],[7,"blue"],[7,"green"],[7,"yellow"],[7,"red"],[9,"blue"],[9,"green"],[9,"yellow"],[9,"red"],["+4","any"],["+4","any"],["+4","any"],["+4","any"],["+2","blue"],["+2","green"],["+2","yellow"],["+2","red"],["reverse","blue"],["reverse","green"],["reverse","yellow"],["reverse","red"],["skip","blue"],["skip","green"],["skip","yellow"],["skip","red"],[0,"blue"],[0,"green"],[0,"yellow"],[0,"red"],[1,"blue"],[1,"green"],[1,"yellow"],[1,"red"],[2,"blue"],[2,"green"],[2,"yellow"],[2,"red"],[3,"blue"],[3,"green"],[3,"yellow"],[3,"red"],[4,"blue"],[4,"green"],[4,"yellow"],[4,"red"],[5,"blue"],[5,"green"],[5,"yellow"],[5,"red"],[6,"blue"],[6,"green"],[6,"yellow"],[6,"red"],[7,"blue"],[7,"green"],[7,"yellow"],[7,"red"],[8,"any"],[8,"any"],[8,"any"],[8,"any"],[9,"blue"],[9,"green"],[9,"yellow"],[9,"red"],["+4","any"],["+4","any"],["+4","any"],["+4","any"],["+2","blue"],["+2","green"],["+2","yellow"],["+2","red"],["reverse","blue"],["reverse","green"],["reverse","yellow"],["reverse","red"],["skip","blue"],["skip","green"],["skip","yellow"],["skip","red"],[8,"any"],[8,"any"],[8,"any"],[8,"any"]]
startcards = [[0,"blue"],[0,"green"],[0,"yellow"],[0,"red"],[1,"blue"],[1,"green"],[1,"yellow"],[1,"red"],[2,"blue"],[2,"green"],[2,"yellow"],[2,"red"],[3,"blue"],[3,"green"],[3,"yellow"],[3,"red"],[4,"blue"],[4,"green"],[4,"yellow"],[4,"red"],[5,"blue"],[5,"green"],[5,"yellow"],[5,"red"],[6,"blue"],[6,"green"],[6,"yellow"],[6,"red"],[7,"blue"],[7,"green"],[7,"yellow"],[7,"red"],[9,"blue"],[9,"green"],[9,"yellow"],[9,"red"]]
for i in range(7):
    randomcard = cards[randint(1, int(len(cards))-1)]
    cards.remove(randomcard)
    player1cards.append(randomcard)
for i in range(7):
    randomcard = cards[randint(1, int(len(cards))-1)]
    cards.remove(randomcard)
    player2cards.append(randomcard)
for i in range(7):
    randomcard = cards[randint(1, int(len(cards))-1)]
    cards.remove(randomcard)
    player3cards.append(randomcard)
for i in range(1):
    randomcard = startcards[randint(1, int(len(startcards))-1)]
    cards.remove(randomcard)
    playedcards.append(randomcard)
def uno():
    if len(reverse) % 2 == 0:
        turn[0] = int(turn[0])+1
    else:
        turn[0] = int(turn[0])-1

    if turn[0] % 3 ==1:

        start = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nit is player 1's turn press enter to start your turn")

        card = player1cards[(int((input('\nprevious card: '+str(playedcards[int(len(playedcards)-1)])+'\nplayer 1 enter a card from 1 to '+ str( int(len(player1cards)))+'\n'+str(player1cards) +'\n'+'\nplayer 1 has ' + str( int(len(player1cards))) +' cards\nplayer 2 has ' + str( int(len(player2cards))) +' cards\nplayer 3 has ' + str( int(len(player3cards))) +' cards\n')))-1) % (int(len(player1cards)))]
        if card[0] == "+4":
            if len(reverse) % 2 == 0:
                if (turn[0]+1) % 3 == 2:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player2cards.append(randomcard)
                else:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player3cards.append(randomcard)
            else:
                if (turn[0]-1) % 3 == 2:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player2cards.append(randomcard)
                else:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player3cards.append(randomcard)
            if len(reverse) % 2 == 0:
                turn[0] = int(turn[0])+1
            else:
                turn[0] = int(turn[0])-1
            player1cards.remove(card)
            playedcards.append(card)
            playedcards[int(len(playedcards)-1)][1] = input('enter a color ')
        elif card[0] == 8:
            player1cards.remove(card)
            playedcards.append(card)
            playedcards[int(len(playedcards)-1)][1] = input('enter a color ')
        elif card[0] == playedcards[int(len(playedcards)-1)][0] or card[1] == playedcards[int(len(playedcards)-1)][1]:
            player1cards.remove(card)
            playedcards.append(card)
            if card[0] == "reverse":
                reverse.append(1)
            elif card[0] == "+2":
                if len(reverse) % 2 == 0:
                    if (turn[0]+1) % 3 == 2:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player2cards.append(randomcard)
                    else:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player3cards.append(randomcard)
                else:
                    if (turn[0]-1) % 3 == 2:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player2cards.append(randomcard)
                    else:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player3cards.append(randomcard)
            elif card[0] == "skip":
                if len(reverse) % 2 == 0:
                    turn[0] = int(turn[0])+1
                else:
                    turn[0] = int(turn[0])-1
        else:
            randomcard = cards[randint(1, int(len(cards))-1)]
            cards.remove(randomcard)
            player1cards.append(randomcard)

    elif turn[0] % 3 ==2:
        start = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nit is player 2's turn press enter to start your turn")
        card = player2cards[(int((input('\nprevious card: '+str(playedcards[int(len(playedcards)-1)])+'\nplayer 2 enter a card from 1 to '+ str( int(len(player2cards)))+'\n'+str(player2cards) +'\n'+'\nplayer 1 has ' + str( int(len(player1cards))) +' cards\nplayer 2 has ' + str( int(len(player2cards))) +' cards\nplayer 3 has ' + str( int(len(player3cards))) +' cards\n')))-1) % (int(len(player2cards)))]
        if card[0] == "+4":
            if len(reverse) % 2 == 0:
                if (turn[0]+1) % 3 == 1:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player1cards.append(randomcard)
                else:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player3cards.append(randomcard)
            else:
                if (turn[0]-1) % 3 == 1:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player1cards.append(randomcard)
                else:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player3cards.append(randomcard)
            if len(reverse) % 2 == 0:
                turn[0] = int(turn[0])+1
            else:
                turn[0] = int(turn[0])-1
            player2cards.remove(card)
            playedcards.append(card)
            playedcards[int(len(playedcards)-1)][1] = input('enter a color ')
        elif card[0] == 8:
            player2cards.remove(card)
            playedcards.append(card)
            playedcards[int(len(playedcards)-1)][1] = input('enter a color ')
        elif card[0] == playedcards[int(len(playedcards)-1)][0] or card[1] == playedcards[int(len(playedcards)-1)][1]:
            player2cards.remove(card)
            playedcards.append(card)
            if card[0] == "reverse":
                reverse.append(1)
            elif card[0] == "+2":
                if len(reverse) % 2 == 0:
                    if (turn[0]+1) % 3 == 1:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player1cards.append(randomcard)
                    else:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player3cards.append(randomcard)
                else:
                    if (turn[0]-1) % 3 == 1:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player1cards.append(randomcard)
                    else:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player3cards.append(randomcard)
            elif card[0] == "skip":
                if len(reverse) % 2 == 0:
                    turn[0] = int(turn[0])+1
                else:
                    turn[0] = int(turn[0])-1
        else:
            randomcard = cards[randint(1, int(len(cards))-1)]
            cards.remove(randomcard)
            player2cards.append(randomcard)


    elif turn[0] % 3 ==0:
        start = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nit is player 3's turn press enter to start your turn")
        card = player3cards[(int((input('\nprevious card: '+str(playedcards[int(len(playedcards)-1)])+'\nplayer 3 enter a card from 1 to '+ str( int(len(player3cards)))+'\n'+str(player3cards) +'\n'+'\nplayer 1 has ' + str( int(len(player1cards))) +' cards\nplayer 2 has ' + str( int(len(player2cards))) +' cards\nplayer 3 has ' + str( int(len(player3cards))) +' cards\n')))-1) % (int(len(player3cards)))]
        if card[0] == "+4":
            if len(reverse) % 2 == 0:
                if (turn[0]+1) % 3 == 2:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player2cards.append(randomcard)
                else:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player1cards.append(randomcard)
            else:
                if (turn[0]-1) % 3 == 2:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player2cards.append(randomcard)
                else:
                    for i in range(4):
                        randomcard = cards[randint(1, int(len(cards))-1)]
                        cards.remove(randomcard)
                        player1cards.append(randomcard)
            if len(reverse) % 2 == 0:
                turn[0] = int(turn[0])+1
            else:
                turn[0] = int(turn[0])-1
            player3cards.remove(card)
            playedcards.append(card)
            playedcards[int(len(playedcards)-1)][1] = input('enter a color ')
        elif card[0] == 8:
            player3cards.remove(card)
            playedcards.append(card)
            playedcards[int(len(playedcards)-1)][1] = input('enter a color ')
        elif card[0] == playedcards[int(len(playedcards)-1)][0] or card[1] == playedcards[int(len(playedcards)-1)][1]:
            player3cards.remove(card)
            playedcards.append(card)
            if card[0] == "reverse":
                reverse.append(1)
            elif card[0] == "+2":
                if len(reverse) % 2 == 0:
                    if (turn[0]+1) % 3 == 2:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player2cards.append(randomcard)
                    else:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player1cards.append(randomcard)
                else:
                    if (turn[0]-1) % 3 == 2:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player2cards.append(randomcard)
                    else:
                        for i in range(2):
                            randomcard = cards[randint(1, int(len(cards))-1)]
                            cards.remove(randomcard)
                            player1cards.append(randomcard)
            elif card[0] == "skip":
                if len(reverse) % 2 == 0:
                    turn[0] = int(turn[0])+1
                else:
                    turn[0] = int(turn[0])-1
        else:
            randomcard = cards[randint(1, int(len(cards))-1)]
            cards.remove(randomcard)
            player3cards.append(randomcard)

    return('\n'+ str(playedcards[int(len(playedcards)-1)]))


while len(player1cards) != 0 and len(player2cards) != 0 and len(player3cards) != 0:
    if len(cards) < 6:
        playedcards = cards
    print(uno())

if len(player1cards) == 0:
    print("player 1 won the game")
elif len(player2cards) == 0:
    print("player 2 won the game")
elif len(player3cards) == 0:
    print("player 3 won the game")
