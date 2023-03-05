import random

#pick what you want to use
#computer picks between three options
#show the outcome

guess = 0

while guess == 0:
    computer_pick = random.randint(1, 3)
    user_pick = int(input("Type 1 for Rock, 2 for Paper and 3 for Scissors: "))
    if user_pick == computer_pick:
        print("It's a draw. Pick again.")
    elif user_pick == 2 and computer_pick == 3:
        guess += 1
        print("Computer picked scissors. You lose.")
    elif user_pick == 1 and computer_pick == 2:
        guess += 1
        print("You lose. Computer picked paper.")
    elif user_pick == 3 and computer_pick == 1:
        guess += 1
        print("You lose. Computer picked rock.")
    else:
        guess += 1
        print("You win!!")




