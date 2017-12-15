#Hangman.py
#Connor Whiteside
import random
import os


limit = 7

def start_screen():
    with open("art/start.txt", 'r') as f:
        lines = f.read()

    print(lines)


def get_puzzle():
    
    file_names = os.listdir("data")
    for i, f in enumerate(file_names):
        print(str(i + 1) + ") " + f)

    choice = input("which one? ")
    choice = int(choice)

    file = "data/" + file_names[choice - 1]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    category = lines[0]
    puzzle = random.choice(lines[1:])

    print(category)
    return(puzzle)

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter.lower() in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(name):
    print()
    guess = input("Enter a letter " + name +": ")
    print()
    return guess

def display_board(solved):
    print(solved)

def play_again():
    while True:
        print()
        decision = input("Game Over, Would you like to play again? (y/n) ")
        decision = decision.lower()
        print()
        
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print()

def show_result():
    with open("art/end.txt", 'r') as f:
        lines = f.read()

    print(lines)
    print("Made by Connor")
    
def play():
    print("What is your name")
    name = input()
    tries = 0
    start_screen()
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    print(solved)

    while solved != puzzle and tries < limit:
        letter = get_guess(name)
        letter = letter.lower()
        if letter not in puzzle:
            tries += 1
            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
        
playing = True
while playing:
    play()
    playing = play_again()

show_result()
