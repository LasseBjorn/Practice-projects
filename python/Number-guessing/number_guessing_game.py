import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100) #Set the number between 1 and 100
    attempts = 10

    #Loop until correct or attempts hit 0
    while attempts > 0:
        guess = int(input("Guess a number between 1 and 100: "))

        #Check if guess is correct and break if correct
        if guess == number_to_guess:
            print(f"Correct! The number was {number_to_guess}")
            break

        #if not correct, reduce attempts and give hint
        attempts -= 1

        if guess < number_to_guess:
            print("Too low")

        else:
            print("Too high")
    #If no more attempts, print the correct number and end
    else:
        print(f"You have used all your attempts. The number was {number_to_guess}.")

number_guessing_game()