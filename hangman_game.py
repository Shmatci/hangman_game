#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Hangman

# -----------------------------------
import random
import string
import os
# print(os.getcwd())


WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split(" ")
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def IsMatch():
    """Logical, returns true if letter is contained within randomly choosen
    word, False otherwise"""
    if letter in word1:
        return True
    else:
        return False


def State_of_word():
    """returns the word with correctly guesed characters at their position"""
    # Refer to variable outside the function
    global state_of_word
        
    list1=list(state_of_word)
    
    # Show correctly guessed letters
    if IsMatch():
        position = 0
        for char in word1:
            if char == letter:
                list1[position*2] = letter
            position+=1
            
    state_of_word=''.join(list1)
    
    return state_of_word


def Avail_letters():
    """Removes letter chosen by user from alphabet and returns
    available letters (string)
    """
    try:
        alphabet_list.remove(letter)
        
    # Warn if same letter is being tried
    except ValueError:
        print("")
        print("Enter a valid letter or try a different letter")
        
    available_letters="".join(alphabet_list)
    return available_letters


def Feedback():
    """Prints feedback, state of the word 
    and available letters"""
    if IsMatch():
        print("Good guess:",State_of_word())
    if not IsMatch():
        print("Not in my word:",State_of_word())
    print("Available letters:",Avail_letters())
    
    
# load words  
wordlist = load_words()

# Choose word
word1 = choose_word(wordlist)

# Number of gueses
error_tolerance =3
n_tries = len(word1)+ error_tolerance

# Progress of word being guessed
state_of_word=''
for lett in word1:
    state_of_word+="_ "
    
# Create a list of all the letters
alphabet = string.ascii_lowercase
alphabet_list =[]
for symbol in alphabet:
    alphabet_list.append(symbol)
        
# Greeting and start game
print("Welcome, human, to the game of Hangman, where you will be hanged!")
print("The word I am thinking about has",len(word1),"letters")
print("--------------------------------------------------")
        

while n_tries!=0:
            # Feedback
            print("You have",n_tries, "guesses remaining")
            letter = input('Please guess a letter:').lower()
            # Feedback
            Feedback()
            print("--------------------------------------------------")
            
            # Exit loop if guessed within trial limit
            if State_of_word().replace(" ","") == word1:
                print("Bravo, you guessed the correct word:",word1)
                break
        
            # Update variables
            n_tries=n_tries - 1
if n_tries==0:
        print("Sorry, you did not guess the correct word")
        print("The correct word was:", word1)
        print("Thank you for playing!")