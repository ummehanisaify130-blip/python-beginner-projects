import random

choices = ["rock", "paper", "scissors"]

print("--- ROCK PAPER SCISSORS ---")
print("Type rock, paper or scissors")
print("Type 'exit' to quit\n")

while True:
    user = input("Your choice: ").lower()
    
    if user == 'exit':
        print("Thanks for playing!")
        break
    
    if user not in choices:
        print("Invalid! Type rock, paper or scissors\n")
        continue

    computer = random.choice(choices)
    print("computer chooses:",computer)

    if user == computer:
        print("It's a Tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win! 🎉\n")
    else:
        print("You Lose! 😢\n")
