import random
def randomize(cards):
    new_list=[]
    for i in range(len(cards)):
        l = random.randrange(0,len(cards))
        new_list.append(cards[l])
        cards.remove(cards[l])

    return new_list
def setupNewGame(number_players,bot_check,bot_number,bot_difficulty,elements):
    print("setting up game...")
    print("Rules: In Chronology, each player builds his or her own timeline of cards. On your turn, someone will read you a historical event from a card. You decide where that event falls in your timeline. If you are right, you keep the card and your timeline grows.")
    turn_order=[]
    print(type(turn_order))
    count = 0
    if number_players >= 1:# player names.
        player1 = input('What is player1\'s name? ')
    turn_order.append(player1+'1')
    if number_players >= 2:
        player2 = input('What is player2\'s name? ')
        turn_order.append(player2+'2')
    if number_players >= 3:
        player3 = input('What is player3\'s name? ')
        turn_order.append(player3+'3')
    if number_players >=4:
        player4 = input('What is player4\'s name? ')
        turn_order.append(player4+'4')
    if number_players >= 5:
        print('I\'ll do this later')
    """if bot_check.lower() == 'n':
        turn_order = make_bots(bot_number,bot_difficulty,turn_order)
        print(turn_order)"""# do bots later
    player_hands = {}
    card_index = 0
    for person in turn_order:
        player_hands[person]=[elements[card_index]]
        card_index += 1
    #for i in range(len(cards1))
    starting_player = turn_order[0]
    turn_number = 0
    print(type(turn_order))
    x = randomize(elements)
    return [turn_order, starting_player, turn_number,player_hands,card_index,bot_difficulty,number_players,x]
