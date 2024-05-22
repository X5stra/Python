import random

#changes the score for each win one person wins the get a point and the other stays the same
def update_scoreboard(result, scoreboard):
    if result == 'win':
        scoreboard['wins'] += 1
    else: 
        scoreboard['losses'] +=1
#gives the score after the win 
def print_scoreboard(scoreboard):
    print("wins:", scoreboard["wins"])
    print("losses:", scoreboard["losses"])



rules = ['rock', 'paper', 'scissors']
actions = random.choice(rules)
scoreboard = {
    'wins': 0,
    'losses': 0,
}

while True:
    user = input('Pick rock, paper or scissors: ')
    print('You chose', user, 'computer chose', actions)
    if user == actions:
        print(f'Both players selected {user}. It a tie')
    
    elif (user == 'rock' and actions == 'scissors') or \
    (user == 'rock' and actions == 'paper') or \
        (user == 'scissors' and actions == 'paper') or \
            (user == 'paper' and actions == 'rock'):
         print(f'{user} beats {actions} you win!')
         update_scoreboard("Win", scoreboard)
    else:
        print(f'{actions} beats {user} you lose!!! :)')
        update_scoreboard("Loss", scoreboard)

    print_scoreboard(scoreboard)
    
    play_again = input('Do you want to play again y/n: ')
    if play_again.lower() != 'y':
        break
