from wordle import Wordle
from colorama import Fore
import random

def main():



    possible_wordlist = []
    valid_wordlist = []

    with open("valid_words.txt" , "r") as f:
        for line in f:
            valid_wordlist.append(line.split()[0])
    
    with open("possible_words.txt" , "r") as f:
        for line in f:
            possible_wordlist.append(line.split()[0])

    word = random.choice(possible_wordlist)

    wordle = Wordle(word.upper())
    
    while(True):
        guess = input("Enter your guess: ")
        while(True):
            if (len(guess) != 5):
                print("Word must be 5 letters")
                guess = input("Enter your guess: ")
            if guess not in valid_wordlist:
                print("Invalid word")
                guess = input("Enter your guess: ")
            else:
                break
        wordle.guess(guess.upper())
        if wordle.check_game() == False:
            break;

if __name__ == "__main__":
    main()