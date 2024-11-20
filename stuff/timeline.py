import random
import json
print('hello')
#eventually seperate all the functions into different files i guess
#load cards grom json file
cards = []
with open('cards.json') as f:
    cards = json.load(f)
print(cards)

#play timeline
# 1. game menu
    # 1.1 select number of players.
    # 1.2 difficulty level
    # 1.3 [bots on/off]
    # 2. setup new game
    #2.1 deal starting card to each player
    # 2.2 show instructions ( tell how to play the game)
    # 2.3 pick starting player
        #new: player order
    # 3. play game (player turns)
        # 3.1 starting player turn
            # requires: players, bots
            # new: turn order?, current player turn?
        #3.2 select next player
            #requires: turn order, 
            #modifies: current players turn?.
            #new: next player's turn?
        # 3.3 take turn
            #Requires: cards, already played cards, current players turn
            #new: check points? 
    #3.4 check if player won/ game is over, if so goto 4.
        #requires: check_points 
    #3.5 goto 3.2

    # 4. show who winner is
def timeline():
    print("starting timeline game")
    showGameMenu()
    setupNewGame()
    play()
    showWinner()

def randomize(cards):
    new_list=[]
    for i in range(len(cards)):
        l = random.randrange(0,len(cards))
        new_list.append(cards[l])
        cards.remove(cards[l])

    return new_list
elements = randomize(cards)


    #while len(cards) != 0:

def showGameMenu(topic='ERROR',words='[1,1,1,1,1,1,1,1]'):
    print("Welcome to timeline, The topic is " + topic)
    number_players = int(input("Please type the number of players(): "))
    bot_check = input("do you want bots?(Y/N): ")
    if bot_check.lower() == "y":
        bot_number = int(input('Please input the number of bots: '))
        bot_difficulty = input('input difficulty of bots(0(easy), 1(medium), 2(hard)): ')
        return[number_players,bot_check,bot_number,bot_difficulty]
    print(' this would receive the game topic and presumably the words and dates')
    return [number_players,bot_check,0,-1,words]

def setupNewGame(number_players,bot_check,bot_number,bot_difficulty,elements):
    print("setting up game...")
    turn_order=[]
    print(type(turn_order))
    count = 0
    if number_players >= 1:# player names.
        player1 = input('What is player1\'s name? ')
    turn_order.append(player1)
    if number_players >= 2:
        player2 = input('What is player2\'s name? ')
        turn_order.append(player2)
    if number_players >= 3:
        player3 = input('What is player3\'s name? ')
        turn_order.append(player3)
    if number_players >=4:
        player4 = input('What is player4\'s name? ')
        turn_order.append(player4)
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
    return [turn_order, starting_player, turn_number,player_hands,card_index]
    


def make_bots(bot_number,bot_difficulty,turn_order = []):
    if bot_difficulty <=-1:
        pass
    elif bot_difficulty >=2:
        bot_1 = bot_hard()
        turn_order.append(bot_1)
        if bot_number == 2:
            bot_2 = bot_hard()
            turn_order.append(bot_2)
        if bot_number == 3:
            bot_3 = bot_hard()
            turn_order.append(bot_3)
        if bot_number == 4:
            bot_4 = bot_hard()
            turn_order.append(bot_4)
    elif bot_difficulty ==1:
        bot_1 = bot_med()
        turn_order.append(bot_1)
        if bot_number == 2:
            bot_2 = bot_med()
            turn_order.append(bot_2)
        if bot_number == 3:
            bot_3 = bot_med()
            turn_order.append(bot_3)
        if bot_number == 3:
            bot_3 = bot_med()
            turn_order.append(bot_3)
    else:
        bot_1 = bot_easy()
        turn_order.append(bot_1)
        if bot_number == 2:
            bot_2 = bot_easy()
            turn_order.append(bot_2)
        if bot_number == 3:
            bot_3 = bot_easy()
            turn_order.append(bot_3)
        if bot_number == 4:
            bot_4 = bot_easy()
            turn_order.append(bot_4)
    return turn_order
    


def bot_easy():
    # do now
    e= random.randrange(1,10)
    if e == 1 or e == 10:
        return True
    else:
        return False
def bot_med():
    e= random.randrange(1,10)
    if e == 1 or e == 10:
        return True
    elif e == 2 or e == 9:
        return True
    else:
        return False
    # do later
def bot_hard():
    e= random.randrange(1,10)
    if e == 1 or e == 10:
        return False
    else:
        return True
    # do later

        
def pick_next_player(current_player,turn_order,index_number):
    index_number += 1
    try:
        new_player = turn_order[index_number]
    except IndexError:
        index_number=0
        new_player = turn_order[index_number]
    return [new_player,index_number]
    


    
def play(starting_player,turn_order,index_number,player_hands,card_index):
    a = False
    current_player = starting_player
    
    while not a:
        info =take_turn(current_player,player_hands,card_index)
        card_index = info[1]

        next_p = pick_next_player(current_player,turn_order,index_number)
        current_player = next_p[0]
        index_number=next_p[1]
        a = game_over(card_index)
    win = findWinner(info[0])
    showWinner(win[1])



def check_guesses(card,guess=-10000000,guess2 = 10000000):
    #check if card is greater than guess
    #guess should be lower then guess2
    if type(guess)==str:
        if guess == 'less':
            if card['year'] < guess2:
                print('correct')
                return True
            else:
                print('Wrong')
                return False
        if guess == 'greater':
            if card['year']>guess2:
                print('correct')
                return True
            else:
                print('Wrong')
                return False
    else:
        if card > guess and card< guess2:
            print("nice job, Correct. ")
            return True
        elif not card>guess:
            print('You guessed to low')
            return False
        elif not card<guess2:
            print("You guessed too high")
            return False
        else:
            print("idk what you did wrong, but ill give you the card ")
            return True


def guessing(player,player_hands,card_index):
    player_years=[]
    
    card = elements[card_index]
    for i in range(len(player_hands[player])):
        player_years.append(player_hands[player][i]['year'])
    big = player_years[0]
    player_years.sort()
    print(player_years)
    print(card["discription"])

    if len(player_hands[player]) == 1:
        guess1 = input("Please enter greater or less based on your guess  ")
        if 'greater' not in guess1.lower():
            if 'less' not in guess1.lower():
                while 'greater' not in guess1.lower() and 'less' not in guess1.lower():
                    guess1 = input('Please enter greater or less. ')
        correct = check_guesses(card,guess1.lower(),player_years[0])
        return [correct]
    #try to make the guessing work for more than the first hand
    else:
        print(player_years)
        guess1 = int(input('enter the first number you want to guess(Has to be a number): '))
        while guess1 not in player_years:
            guess1 = int(input('enter the first number you want to guess(Has to be a number, and a year in your hand): '))#try to make it so that you can check for a number.
        eue = input(' do you want less then or greater than this number: ')
        if 'greater' not in eue.lower():
            if 'less' not in eue.lower():
                while 'greater' not in eue.lower() and 'less' not in eue.lower():
                    eue = input('Please enter greater or less. ')
        for i in range(len(player_years)):
            if guess1 == player_years[i]:
                number = i
        if eue == 'greater':
            if player_years[number] == player_years[-1]:
                guess2 = 100000000000
            else:
                guess2 = player_years[number+1]
            correct = check_guesses(card['year'],guess1,guess2)
        if eue == 'less':
            if player_years[number] == player_years[0]:
                guess2 = -1000000000
            else:
                guess2 = player_years[number-1]
            correct = check_guesses(card['year'],guess2,guess1)
        return [correct]
        

                


                

    """
    if player_years[i] == player_years[0]:
                pass
    if len(player_hands[player]) == 1:
        print(f"is the number less than {player_hands[player][0][year]} or greater than it")
        guess = input("Greater then or less then ")

        if 'greater' in guess.lower():
            greater_check(card,guess)"""
    return [card,player_years]


        
def take_turn(player,player_hands,card_index):
    #Todo: take player turn

    print(f"player {player} is taking their turn")
    guesses = guessing(player,player_hands,card_index)
    
    if guesses[0] != False:
        player_hands[player].append(elements[card_index])
        card_index +=1
    #print(player_hands)
    #print(card_index)
    
    return [player_hands,card_index]

def game_over(card_index):
    # TODO: check if game is over
    if card_index == len(elements):
        return True
    return False
def findWinner(player_hands):
    win = 0
    winner = ''
    for thing in player_hands:
        if len(player_hands[thing]) > win:
            win = len(player_hands[thing])
            winner=thing
    return [win,winner]
def showWinner(winner):
    print("wow, "+winner+" won")

stuff = showGameMenu('table',elements)
other = setupNewGame(stuff[0],stuff[1],stuff[2],stuff[3],stuff[4])
print(other)
play(other[1],other[0],other[2],other[3],other[4])
#print(showGameMenu())
#timeline()
