import random

print("🎮 Rock Paper Scissors Game 🎮")
print("1. Rock  2. Paper  3. Scissor")


try:
    choice = int(input("Select your choice (1/2/3): "))
except ValueError:
    print("Invalid choice")
    exit()


rand = random.randint(1, 3)


choices = {1: "Rock", 2: "Paper", 3: "Scissor"}

if choice not in choices:
    print("Invalid choice")
else:
    print("Your choice:", choices[choice])
    print("System choice:", choices[rand])

    if rand == choice:
        print("Tie")
    elif rand == 1 and choice == 2:
        print("You won")
    elif rand == 1 and choice == 3:
        print("You lost")
    elif rand == 2 and choice == 1:
        print("You lost")
    elif rand == 2 and choice == 3:
        print("You won")
    elif rand == 3 and choice == 1:
        print("You won")
    elif rand == 3 and choice == 2:
        print("You lost")
