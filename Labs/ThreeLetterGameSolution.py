# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 15:58:17 2014

@author: Evan
"""

# Get word list
wordlist = ['the', 'and', 'for',
 'you', 'say', 'but', 'his',
 'not', 'she', 'can', 'who',
 'get', 'her', 'all', 'one',
 'out', 'see', 'him', 'now',
 'how', 'its', 'our', 'two',
 'way', 'new', 'day', 'use',
 'man', 'any', 'may', 'try',
 'ask', 'too', 'own', 'put',
 'old', 'why', 'let', 'big',
 'few', 'run', 'off', 'lot',
 'eye', 'job', 'far', 'yes',
 'sit', 'yet', 'end', 'bad',
 'pay', 'law', 'car', 'set',
 'kid', 'ago', 'add', 'art',
 'war', 'low', 'win', 'guy',
 'air', 'boy', 'age', 'buy',
 'die', 'cut', 'six', 'son',
 'arm', 'tax', 'hit', 'eat',
 'oil', 'red', 'per', 'top',
 'bed', 'hot', 'lie', 'dog',
 'cup', 'box', 'lay', 'sex',
 'act', 'ten', 'gun', 'leg',
 'fly', 'bit', 'sea', 'bar',
 'bag', 'gas', 'Mrs', 'nor',
 'key', 'sky', 'fan', 'ice',
 'sun', 'ear', 'fit', 'cry',
 'egg', 'hey', 'bus', 'tie',
 'map', 'nod', 'dry', 'fat',
 'lip', 'mom', 'aid', 'mix',
 'cat', 'due', 'dad', 'fee',
 'row', 'fix', 'era', 'fun',
 'tip', 'aim', 'Jew', 'hat',
 'gay', 'lab', 'sir', 'gap',
 'sad', 'tea', 'cop', 'pot',
 'cap', 'toy', 'dig', 'wet',
 'pan', 'CEO', 'pop', 'mad',
 'via', 'hip', 'bet', 'odd',
 'raw', 'joy', 'DNA', 'tap',
 'rub', 'net', 'ill', 'owe',
 'ski', 'rid', 'cow', 'etc',
 'sue', 'jet', 'god', 'nut',
 'ban', 'pet', 'sin', 'pie',
 'lap', 'toe', 'log', 'beg',
 'pig', 'van', 'bay', 'rat',
 'hay', 'rip', 'pen', 'mud',
 'pad', 'bat', 'wow', 'sum',
 'pit', 'hug', 'gym', 'huh',
 'kit', 'pro', 'bid', 'jaw',
 'bow', 'bug', 'ass', 'cab',
 'web', 'bee', 'jar', 'gut',
 'pin', 'dam', 'shy', 'oak',
 'tag', 'dot', 'dip', 'pat',
 'rib', 'rod', 'ash', 'rim',
 'lid', 'fur', 'opt', 'ego',
 'spy', 'cue', 'fog']

class TLGame:
    def __init__(self, wordlist, guesses_allowed = 3):
        self.wordlist = wordlist
        self.guesses = []
        self.word_to_guess = ""
        self.guesses_allowed = guesses_allowed
        self.player_name = ""
        self.guess_word = ""
        
    @property
    def Wordlist(self):
        return self.wordlist

    @property
    def Guesses(self):
        return self.guesses

    @property
    def WordToGuess(self):
        return self.word_to_guess
    
    @property
    def GuessesAllowed(self):
        return self.guesses_allowed

    @property
    def GuessesTaken(self):
        return len(self.Guesses)

    @property
    def PlayerName(self):
        return self.player_name

    @property
    def GuessWord(self):
        return self.guess_word

    def NewGame(self, new_player):
        self.guesses = []
        self.word_to_guess = self.pickword()
        self.guesses_allowed = 3
        if new_player:
            self.getname()
        self.start_game()

    @staticmethod
    def pickword():
        import random
        word = wordlist[random.randint(0,len(wordlist))].lower()
        return word
    
    @staticmethod
    # Get name and Welcome the User
    def getname():
        print( "Welcome to the three letter word game!")
        name =  input("What is your name? ")
        print( "Welcome, " + name) 
        return name
            
    # Prompt User for Guess, check it is correct length
    def ask_for_guess(self):
        while True:
            word_guess = input("Hello " + self.PlayerName.capitalize() + ". \n Please enter the three letter word you would like to guess (or type quit): ")
            if word_guess.lower() == "quit":
                return word_guess
            elif len(word_guess) != 3:
                print( "Please enter a THREE letter word.")
            elif any([i.isdigit() for i in word_guess]):
                print( "Do not enter numbers.")
            else:
                return word_guess
        
        
    # Compare the words
    def compare_words(self):
        if self.GuessWord.lower() == "quit":
            return ("quit", "", 0)
        if self.GuessWord == self.WordToGuess:
            return ("match", "", 0)
        
        number_in = 0
        for letter in self.GuessWord:
            if letter in self.WordToGuess:
                number_in += 1
        return("no match", self.GuessWord, number_in)
        
    def start_game(self):
        while True:
            self.guess_word = self.ask_for_guess()
            result, guess, num_correct = self.compare_words()
            if result == "match":
                print( "You won!")
                break
            elif result == "quit":
                print( "Goodbye")
                break
            else:
                # Store Data Like this
                # guesses = [("cab",1),("fed",2)]
                self.guesses.append([guess, num_correct])
                print( "You have guessed the following:\n")
                for i in self.Guesses:
                    print( i[0] + " had " + str(i[1]) + r" letter(s) in common.")
                if self.GuessesTaken < self.GuessesAllowed:
                    print( "You have " + str(self.GuessesAllowed - self.GuessesTaken) + " guesses remaining.")
                else:
                    print( "Sorry, you ran out of guesses. The word was: " + self.WordToGuess)
                    break

    
# test game
new_game = TLGame(wordlist)
#new_game.Wordlist
#new_game.Guesses
new_game.NewGame(True)
#new_game.WordToGuess
#new_game.start_game()
new_game.NewGame(False)


     
# J-Raj version
def CommonLetters(s1, s2):
    return [x for x in list(s1) if x in list(s2)]
CommonLetters("goo","god")
