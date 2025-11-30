import random

Hangman = [""" 
____
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   ||
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   |||
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   |||
|    |
|   | 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   |||
|    |
|   | |
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   |||
|    |
|   | |
|
|_____
"""]

#გამოსაცნობი სიტყვების სია
words = ["PROGRAM", "COMPUTER", "DEVELOPER", "VARIABLE", "FUNCTION", "ALGORITHM"]

def choose_word():
    #სიტყვის შემთხვევით არჩევა სიიდან
    return random.choice(words)

def show_word(word, guessed_letters):
    #ვბეჭდავთ სიტყვას გამოცნობილი ასოებით (_R__RA_)
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    print("Word: ", displayed)

def try_guess(guessed_letters):
    while True:
        #მომხმარებელს შეჰყავს ასო და ხდება ინფუთის ვალიდაცია
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Invalid Input, please enter a single letter")
        elif guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Invalid Input, please enter a letter")
        elif guess in guessed_letters:
            print("You have already guessed that letter")
        else:
            return guess

def update_game(word, guess, guessed_letters, wrong):
    #ვინახავთ ყველა შეყვანილ ასოს, არასწორსაც რადგან ხელმეორედ აღარ მოხდეს შეყვანა
    guessed_letters.append(guess)

    if guess in word:
        print("Correct! The letter", guess, "is in the word")
    else:
        print("Letter", guess, "is not in the word")
        wrong += 1
    return wrong

def finished(word, guessed_letters, wrong, max_wrong):
    #ვამოწმებთ მოგებულია თუ არა თამაში, ვვარაუდობთ რომ მოთამაშემ მოიგო
    won = True
    #ვამოწმებთ სიტყვის ყველა ასოს, თუ რომელიმე გამოსაცნობია, თამაში ჯერ არ არის მოგებული
    for letter in word:
        if letter not in guessed_letters:
            won = False
            break
    #თუ ყველა ასო გამოცნობილია, მოგება
    if won:
        print("Congrats! You won! The word was:", word)
        return True
    #თუ შეცდომების რაოდენობამ მაქსიმუმს მიაღწია, წაგება
    if wrong >= max_wrong:
        print(Hangman[wrong])
        print("You lose! The word was:", word)
        return True
    #თუ არც მოგებულია და არც წაგებული, მაშინ თამაში გრძელდება
    return False

def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong = 0
    max_wrong = 6

    while True:
        # ნახატი
        print(Hangman[wrong])
        # სიტყვის ჩვენება
        show_word(word, guessed_letters)
        # უკვე შეყვანილი ასოების ჩვენება
        if guessed_letters:
            print("Guessed letters:", " ".join(guessed_letters))
        # შეყვანა
        guess = try_guess(guessed_letters)
        if not guess:
            continue
        # განახლება
        if guess not in word:
            wrong += 1
            print("Letter", guess, "is not in the word")
        else:
            print("Correct! The letter", guess, "is in the word")
        #შეყვანილი ასოს შენახვა
        guessed_letters.append(guess)
        # გამარჯვების შემოწმება
        won = all(letter in guessed_letters for letter in word)
        if won:
            print("Congrats! You won! The word was:", word)
            break
        # წაგების შემოწმება
        if wrong == max_wrong:
            print(Hangman[wrong])  # ბოლო ნახატი
            print("You lose! The word was:", word)
            break

play_hangman()







