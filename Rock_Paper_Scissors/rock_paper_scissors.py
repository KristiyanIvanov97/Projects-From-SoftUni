import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input.Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")


if (player_move == "Rock" and computer_move == "Scissors") or \
        (player_move == "Paper" and computer_move == "Rock") or \
        (player_move == "Scissors" and computer_move == "Paper"):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")

