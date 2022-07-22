from colorama import Fore


class Wordle:

    num_attempts = 0;
    attempts = []
    correct_pos = []
    in_word = []

    def __init__(self, word):
        self.word = word
        self.attempts = []
        pass

    def check_game(self) -> bool:
        if self.num_attempts > 0:
            if self.attempts[len(self.attempts) - 1] == self.word:
                print("Congratulations! You won in", self.num_attempts, "tries")
                return False
        if (self.num_attempts > 5):
            print("Sorry, you lost, the word was" , self.word)
            return False
        return True

    def guess(self, guess):
        self.num_attempts = self.num_attempts + 1
        self.attempts.append(guess)
        self.correct_position(guess)
        self.inside_word(guess)
        self.print()
    
    def correct_position(self, guess):
        temp = []
        for i, j in zip(guess, self.word):
            if i == j:
                temp.append(True)
            else:
                temp.append(False)
        self.correct_pos.append(temp)
    
    def inside_word(self, guess):
        temp = []
        for i, j in zip(guess, self.word):
            if (self.word).find(i) != -1:
                if (i != j):
                    temp.append(True)
                else:
                    temp.append(False)
            else:
                temp.append(False)
        self.in_word.append(temp)

    def print(self):
        print("Turn", self.num_attempts)
        print(Fore.MAGENTA + "-------------" + Fore.RESET)
        counter = 0
        for x in range(self.num_attempts):
            print(Fore.MAGENTA + "| " + Fore.RESET, end = "")
            counter1 = 0
            for y in self.attempts[counter]:
                if (self.correct_pos[counter][counter1] == True):
                    print(Fore.GREEN + y + " " + Fore.RESET, end = "")
                elif (self.in_word[counter][counter1] == True):
                    print(Fore.YELLOW + y + " " + Fore.RESET, end = "")
                else:
                    print(Fore.LIGHTWHITE_EX + y + " " + Fore.RESET, end = "")
                counter1 = counter1 + 1
            print(Fore.MAGENTA + "|" + Fore.RESET)
            counter = counter + 1
        print(Fore.MAGENTA + "-------------" + Fore.RESET)
          
    
    
    

    