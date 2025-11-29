import random

def play_again():
    answer = input("Would you like to play again? Y/N: ")
    while True:
        if answer == "Y" or answer == "y":  return True
        if answer == "N" or answer == "n": return False
        else: print("That's not a valid answer. Try again.")


number = random.randint(1, 100)

print("Random Number between 1 and 100 has been generated")

while True:

    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high.")
    if(guess == number):
        print("Congratulations, you guessed the number!")
        if(not(play_again())):
            break