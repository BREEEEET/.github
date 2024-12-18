import random

    


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
        bot_1 = 'bot1_easy'
        turn_order.append(bot_1)
        if bot_number == 2:
            bot_2 = 'bot2_easy'
            turn_order.append(bot_2)
        if bot_number == 3:
            bot_3 = 'bot3_easy'
            turn_order.append(bot_3)
        if bot_number == 4:
            bot_4 = 'bot4_easy'
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
#
#

def bot_turn(bot_difficulty,player_hands,card,elements,player_years,player):
    if bot_difficulty == 0:
        l = random.randrange(0,len(player_years))
        easy = random.randrange(0,10)
        if easy == 0 or easy== 9:
            print("The bot got it Wrong.(by chance  -_-) ")
            correct = False
            return[correct]
        year = player_years[l]
        condition = random.randrange(0,2)
        if condition ==0:
            contition='less'
            
            try:
                i = player_years[l-1]
            except IndexError:
                i = -1000000
            if l == player_years[0]:
                i = -1000000
            correct = check_guesses(card,i,l)
        elif condition==1:
            contition='greater'
            try:
                i = player_years[l+1]
            except IndexError:
                i=1000000000000000
    elif bot_difficulty == 1:
        l = random.randrange(0,len(player_years))
        normal = random.randrange(0,10)
        
        year = player_years[l]
        condition = random.randrange(0,2)
        if condition ==0:
            contition='less'
            
            try:
                i = player_years[l-1]
            except IndexError:
                i = -1000000
            if l == player_years[0]:
                i = -1000000
            correct = check_guesses(card,i,l)
        elif condition==1:
            contition='greater'
            try:
                i = player_years[l+1]
            except IndexError:
                i=1000000000000000
        correct = check_guesses(card,l,i)
    elif bot_difficulty==2:
        l = random.randrange(0,len(player_years))
        easy = random.randrange(0,10)
        if easy == 0 or easy== 9:
            print("The bot got it Right.(by chance  -_-) ")
            correct = True
            return[correct]
        year = player_years[l]
        condition = random.randrange(0,2)
        if condition ==0:
            contition='less'
            
            try:
                i = player_years[l-1]
            except IndexError:
                i = -1000000
            if l == player_years[0]:
                i = -1000000
            correct = check_guesses(card,i,l)
        elif condition==1:
            contition='greater'
            try:
                i = player_years[l+1]
            except IndexError:
                i=1000000000000000
        
    return [correct]

#
#
        
        
def pick_next_player(current_player,turn_order,index_number):
    index_number += 1
    try:
        new_player = turn_order[index_number]
    except IndexError:
        index_number=0
        new_player = turn_order[index_number]
    return [new_player,index_number]
    


    
def play(starting_player,turn_order,index_number,player_hands,card_index,bot_difficulty=-1,number_players=2,elements="somethin went worng"):
    a = False
    current_player = starting_player
    
    while not a:
        info =take_turn(current_player,player_hands,card_index,elements)
        card_index = info[1]

        next_p = pick_next_player(current_player,turn_order,index_number)
        current_player = next_p[0]
        index_number=next_p[1]
        a = game_over(card_index,player_hands,elements)
    win = findWinner(info[0])
    showWinner(win[1])



def check_guesses(card,guess=-10000000,guess2 = 'less'):
    #check if card is greater than guess
    #guess should be lower then guess2
    if type(guess)==str:
        if guess == 'less':
            if card['year'] < guess2:
                print('correct\n')
                return True
            else:
                print('Wrong\n')
                return False
        if guess == 'greater':
            if card['year']>guess2:
                print('correct\n')
                return True
            else:
                print('Wrong\n')
                return False
    else:
        if card > guess and card< guess2:
            print("nice job, Correct.\n ")
            return True
        elif not card>guess:
            print('You guessed to high\n')
            return False
        elif not card<guess2:
            print("You guessed too low\n")
            return False
        else:
            print("idk what you did wrong, but ill give you the card \n")
            return True


def guessing(player,player_hands,card_index,elements):
    player_years=[]
    
    card = elements[card_index]
    for i in range(len(player_hands[player])):
        player_years.append(player_hands[player][i]['year'])
    big = player_years[0]
    player_years.sort()
    
    print(card["discription"])

    if len(player_hands[player]) == 1:
        print(player_years)
        guess1 = input("Please enter greater or less based on your guess  ")
        if guess1 == '>':
            guess1 = 'greater'
        elif guess1 == '<':
            guess1='less'
        if guess1 =='stop':
            exit()
        if 'greater' not in guess1.lower():
            if 'less' not in guess1.lower():
                while 'greater' not in guess1.lower() and 'less' not in guess1.lower():
                    guess1 = input('Please enter greater or less. ')
        if 'greater' in guess1.lower():
            guess1 = 'greater'
        elif 'less' in guess1.lower():
            guess1 = 'less'
        correct = check_guesses(card,guess1.lower(),player_years[0])
        return [correct]
    #try to make the guessing work for more than the first hand
    else:
        print(player_years)
        try:
            guess1 = int(input('enter the first number you want to guess(Has to be a number): '))
        except ValueError:
            print("incorrect input_ Please put a Number, otherwise it will be a random one. ")
            try:
                guess1 = int(input('enter the first number you want to guess(Has to be a number): '))
            except ValueError:
                print('ok we\'ll pick randomly')
                guess1 = player_years[random.randrange(len(player_years))]

        while guess1 not in player_years:
            try:
                print(player_years)
                guess1 = int(input('enter the first number you want to guess(Has to be a number, and in your hand): '))
            except ValueError:
                print('ok we\'ll pick randomly')
                guess1 = player_years[random.randrange(len(player_years))]
        eue = input(' do you want less then or greater than this number: ')
        if eue == 'stop':
            exit()
        if 'greater' not in eue.lower():
            if 'less' not in eue.lower():
                while 'greater' not in eue.lower() and 'less' not in eue.lower():
                    eue = input('Please enter greater or less. ')
        for i in range(len(player_years)):
            if guess1 == player_years[i]:
                number = i
        if 'greater' in eue.lower():
            eue = 'greater'
        elif 'less' in eue.lower():
            eue = 'less'
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


        
def take_turn(player,player_hands,card_index,elements):
    #Todo: take player turn

    print(f"player {player[:-1]} is taking their turn")
    guesses = guessing(player,player_hands,card_index,elements)
    
    if guesses[0] != False:
        player_hands[player].append(elements[card_index])
        card_index +=1
    #print(player_hands)
    #print(card_index)
    
    return [player_hands,card_index]

def game_over(card_index,player_hands,elements):
    # TODO: check if game is over
    if card_index == len(elements):
        return True
    for key in player_hands:
        if len(player_hands[key]) > 7:
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
    print(winner +" had "+ len(player_hands[winner])+" cards,")
