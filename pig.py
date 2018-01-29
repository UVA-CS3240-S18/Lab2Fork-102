# Mark Sherriff (mss2x)

import random

print("Welcome to Pig!")

done = False
player_1_temp_total = 0
player_1_total = 0
player_2_temp_total = 0
player_2_total = 0
comp_temp_total = 0
comp_total = 0
turn = "player_1"
winning_score = 50

while not done:
    while turn == "player_1" and not done:
        print()
        print("Player_1:", player_1_total, "Computer:", comp_total, "Player_2:", player_2_total)
        print("It's player_1's turn!")
        roll = random.randint(1,6)
        print("You rolled a", roll)
        if roll == 1:
            turn = "computer"
            player_1_temp_total = 0
            print("PIG! Too bad! Your total is currently:", player_1_total)
        else:
            player_1_temp_total += roll
            print("You currently have " + str(player_1_temp_total) + " banked.")
            choice = input("Do you wish to roll again (y/n)?: ")
            if choice == 'n':
                player_1_total += player_1_temp_total
                player_1_temp_total = 0
                print("Your total score is now:", player_1_total)
                turn = "computer"
        if player_1_total > winning_score:
            print("Player_1 wins! " + str(player_1_total) + " to " + str(comp_total) + " and " + str(player_2_total))
            done = True

    while turn == "computer" and not done:
        print()
        print("Player_1:", player_1_total, "Computer:", comp_total, "Player_2:", player_2_total)
        print("It's the computer's turn!")
        roll = random.randint(1,6)
        print("The computer rolled a", roll)
        if roll == 1:
            turn = "player_2"
            comp_temp_total = 0
            print("PIG! Too bad! The computer's total is currently:", comp_total)
        else:
            comp_temp_total += roll
            print("The computer has " + str(comp_temp_total) + " banked.")
            if comp_temp_total > 6 or comp_total + comp_temp_total > winning_score:
                print("The computer has chosen to end its turn.")
                comp_total += comp_temp_total
                comp_temp_total = 0
                print("The computer's score is now:", comp_total)
                turn = "player_2"
        if comp_total > winning_score:
            print("The computer wins! " + str(comp_total) + " to " + str(player_total + " and " + str(player_2_total)))
            done = True

    while turn == "player_2" and not done:
        print()
        print("Player_2:", player_2_total, "Computer:", comp_total, "Player_1:", player_1_total)
        print("It's player_2's turn!")
        roll = random.randint(1,6)
        print("You rolled a", roll)
        if roll == 1:
            turn = "player_1"
            player_2_temp_total = 0
            print("PIG! Too bad! Your total is currently:", player_2_total)
        else:
            player_2_temp_total += roll
            print("You currently have " + str(player_2_temp_total) + " banked.")
            choice = input("Do you wish to roll again (y/n)?: ")
            if choice == 'n':
                player_2_total += player_2_temp_total
                player_2_temp_total = 0
                print("Your total score is now:", player_2_total)
                turn = "player_1"
        if player_2_total > winning_score:
            print("Player_2 wins! " + str(player_2_total) + " to " + str(comp_total) + " and " + str(player_1_total))
            done = True