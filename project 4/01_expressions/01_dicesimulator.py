import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1:", die1, "Die 2:", die2)

def main():
    print("Rolling two dice, three times:\n")
    roll_dice()  # First roll
    roll_dice()  # Second roll
    roll_dice()  # Third roll

main()