import random

# 1 for Snake
# -1 for Water
# 0 for Gun

computer = random.choice([1, -1, 0])

user = int(input("Enter 1 for Snake, -1 for Water, 0 for Gun: "))

print("Computer chose:", computer)

# Draw
if user == computer:
    print("It's a draw!")

# Winning conditions for user
elif (user == 1 and computer == -1) or \
     (user == -1 and computer == 0) or \
     (user == 0 and computer == 1):
    print("You win!")

# Otherwise computer wins
else:
    print("Computer wins!")
