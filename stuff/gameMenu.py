import json
cards = []
with open('cards.json') as f:
    cards = json.load(f)
def showGameMenu(topic='ERROR',words='[1,1,1,1,1,1,1,1]'):
    print("Welcome to timeline, The topic is " + topic)
    number_players = int(input("Please type the number of players(): "))
    bot_check = input("do you want bots?(Y/N): ")
    if bot_check.lower() == "y":
        bot_number = int(input('Please input the number of bots: '))
        bot_difficulty = input('input difficulty of bots(0(easy), 1(medium), 2(hard)): ')
        return[number_players,bot_check,bot_number,bot_difficulty]
    print(' this would receive the game topic and presumably the words and dates')
    print("you get card and you have to guess greater or lowers.")
    return [number_players,bot_check,0,-1,cards]
