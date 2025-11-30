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

def play_hangman(max_wrong=None):
    #თამაშის ციკლი
    word = choose_word()
    guessed_letters = []
    wrong = 0
    max_wrong = max_wrong if max_wrong else len(Hangman) - 1

    while True:
        #ნახატი
        print(Hangman[wrong])

        #სიტყვა
        show_word(word, guessed_letters)

        #უკვე გამოცნობილი ასოების ჩვენება
        if guessed_letters:
            print("Guessed letters:", " ".join(guessed_letters))

        #შეყვანა
        guess = try_guess(guessed_letters)
        if not guess:
            continue  # ცარიელი შეყვანა იგნორირდება

        # განახლება
        wrong = update_game(word, guess, guessed_letters, wrong)

        # დასრულების შემოწმება
        if finished(word, guessed_letters, wrong, max_wrong):
            break

play_hangman(max_wrong=len(Hangman) - 1)







