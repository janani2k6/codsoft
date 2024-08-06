import random

def game():
    choices = ["rock", "paper", "scissors"]
    score_user = 0
    score_computer = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = int(input("Enter your choice (1/2/3/4): "))

        if user_choice == 4:
            print(f"Final Score - You: {score_user}, Computer: {score_computer}")
            break

        user_choice = choices[user_choice - 1]

        computer_choice = random.choice(choices)

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                score_user += 1
            else:
                print("Paper covers rock! You lose.")
                score_computer += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                score_user += 1
            else:
                print("Scissors cuts paper! You lose.")
                score_computer += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                score_user += 1
            else:
                print("Rock smashes scissors! You lose.")
                score_computer += 1

        print(f"Score - You: {score_user}, Computer: {score_computer}\n")

game()
