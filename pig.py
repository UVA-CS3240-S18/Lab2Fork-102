# Mark Sherriff (mss2x)

import random

print("Welcome to Pig!")

done = False
temp_total = 0
player_total = 0
comp_total = 0
player_turn = True
winning_score = 10

while not done:
    print()
    print("Player:", player_total, "Computer:", comp_total)
    if player_turn:
        print("It's your turn!")
    else:
        print("It's the computer's turn!")
    roll = random.randint(1,6)
    print("You" if player_turn else "The computer", "rolled a", roll)
    if roll == 1:
        player_turn = not player_turn
        temp_total = 0
        print("PIG! Too bad! Your total is currently:", player_total)
    else:
        temp_total += roll
        print("You currently have " if player_turn else "The computer has ",str(temp_total) + " banked.")
        if player_turn:
            choice = input("Do you wish to roll again (y/n)?: ")
            if choice == 'n':
                player_total += temp_total
                temp_total = 0
                print("Your total score is now:", player_total)
                player_turn = not player_turn
        else:
            if temp_total > 6 or comp_total + temp_total > winning_score:
                print("The computer has chosen to end its turn.")
                comp_total += temp_total
                temp_total = 0
                print("The computer's score is now:", comp_total)
                player_turn = not player_turn
    if not player_turn and player_total > winning_score:
        print("You win! " + str(player_total) + " to " + str(comp_total))
        done = True
    if player_turn and comp_total > winning_score:
        print("The computer wins! " + str(comp_total) + " to " + str(player_total))
        done = True
