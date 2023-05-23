import random
def play():
    user = input("Enter you choice 'r' for rock ,'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'OOpssssssss It\'s Tie'

    if is_win (user, computer):
        return 'Congratulationss  You Won'

    return 'Ohhhh You Lost'
def is_win(player, opponent):
    if (player =='r' and opponent == 's') or (player =='s' and opponent =='p')\
       or (player == 'p' and opponent == 'r'):
        return True
while True:
        answer = input("Would you like to try again?:Yes or NO")
        if answer == 'NO':
            break

(play())

    
