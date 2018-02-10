# Mark Sherriff (mss2x)

import random

print("Welcome to Pig!")

done = False
player_temp_total = 0
player_total = 0
comp_temp_total = 0
comp_total = 0
turn = "player"
winning_score = 50

def play(turn, done, player_temp_total, player_total):
    while turn == "player" and not done:
        print()
        print("Player:", player_total, "Computer:", comp_total)
        print("It's ", turn, " turn!")
        roll = random.randint(1,6)
        print(turn, " rolled a", roll)
        if roll == 1:
            if(turn == "player"):
                turn = "computer"
            else:
                turn = "player"
            player_temp_total = 0
            print("PIG! Too bad! Your total is currently:", player_total)
        else:
            player_temp_total += roll
            print("You currently have " + str(player_temp_total) + " banked.")
            if(turn == "player"):
                choice = input("Do you wish to roll again (y/n)?: ")
                if choice == 'n':
                    player_total += player_temp_total
                    player_temp_total = 0
                    print("Your total socre is now:", player_total)
                    turn = "computer"
            else:
                if player_temp_total > 6 or player_total + player_temp_total > winning_score:
                    print("The computer has chosen to end its turn.")
                    player_total += player_temp_total
                    player_temp_total = 0
                    print("The computer's score is now:", player_total)
                    turn = "player"
        if player_total > winning_score:
            print("You win! " + str(player_total) + " to " + str(comp_total))
            done = True

while not done:
    play(turn, done, player_temp_total, player_total)
    play(turn, done, comp_temp_total, comp_total)
done = True