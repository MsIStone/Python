# Edited on 12th August. testing github
# coding: utf-8

# ## COMP47560 
# ## Coding & Software Engineering
# ## Assignment 1
# ## Hangman

# ## 28th Feb 2018


def hangman():
    
    print ('************************')
    print ('***Welcome to Hangman***')
    print ('************************')
    print ('*******Good luck********')
    print ('************************')

    candidate_words = ['fantastic', 'read', 'television', 'computer', 'laptop', 'school', 'grass', 'hospital', 'university', 'estate', 'movie', 'country', 'amazing', 'country']
 
    import random
    word = random.choice(candidate_words)

    word_list = []
    state_play = []     
    

    for character in word:
        word_list.append(character)  #making chosen word into a list (string to list)
        state_play.append("*")       #creating a list with stars same length as word
 
    x = 0
#    total_guesses = len(word) + 4    #sets the number of guesses to be 4 more than the length of the word
    total_guesses = 6
    
    print ('Word       Number of Guesses Left       Guess a Letter')
    print ('---------------------------------------------------------------------------------------------')


    while x < total_guesses:

        for i in state_play:  # looking at each item in star_list
            print(i, end='') # The end=' '  a space after the end of the statement instead of a new line character.

        print("    You have", total_guesses, "guesses left      ", end='      ')
        guess = input(" What is your guess?:   " )
        
        if guess == '99':
            break 
        
        check = False
        for index, item in enumerate(word_list):    # for item in word_list:
            if item == guess:
                state_play[index] = guess
                check = True
        
        if not check:
            total_guesses = total_guesses - 1  #only decrement by 1 if the guess is incorrect

        if state_play == word_list:
            print ('\n')
            print ('*******************************************')
            print("You win, the word was", word, '. Well done!')
            print('*******************************************')
            break
            
    if state_play != word_list:
        print ('--------------------------------')
        print ("Try again, the word was......", word)




hangman()



