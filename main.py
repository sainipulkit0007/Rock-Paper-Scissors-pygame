import random

def play():
    user = input("Enter Your Choice \n'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a Tie!!!'
    if win(user,computer):
        return 'You Won!!!'
    return 'You Lost!!!'

def win(player,comp):
    #Returns True if player Wins.
    # r > s, s > p , p > r.
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp == 'r'):
        return True

print(play())