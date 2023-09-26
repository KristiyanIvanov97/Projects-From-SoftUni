import random
moves = ["rock", "paper", "scissors"]
player_counter = 0
computer_counter = 0

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()

    if player_move == "r":
        player_choice = moves[0]
    elif player_move == "p":
        player_choice = moves[1]
    elif player_move == "s":
        player_choice = moves[2]
    else:
        print("Invalid choice.Try again...")
        continue

    computer_choice = random.choice(moves)
    print(F"You chose : {player_choice.upper()} \nComputer chose : {computer_choice.upper()}")

    if player_choice == computer_choice:
        print(F"You both chose : {player_choice.upper()} \nIt's a tie!")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            player_counter += 1
        else:
            print("Rock smashes scissors! You loose!")
            computer_counter += 1
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            player_counter += 1
        else:
            print("Scissors cuts paper! You loose!")
            computer_counter += 1
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("Rock crushes scissors! You win!")
            player_counter += 1
        else:
            print("Paper covers rock! You loose!")
            computer_counter += 1

    if player_counter == 3:
        print(F"You won the game with {player_counter} points!")
        continue_game = input("If you want to continue playing type [y] for 'Yes' or [n] for 'No'\n").lower()
        if continue_game != "y":
            break
    elif computer_counter == 3:
        print(F"You lost the game with {computer_counter} points!")
        continue_game = input("If you want to continue playing type [y] for 'Yes' or [n] for 'No'\n").lower()
        if continue_game != "y":
            break


