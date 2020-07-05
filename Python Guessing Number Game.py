import random

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable

num = random.randint(1,100)

# Next, print an introduction to the game and explain the rules

print("\n WELCOME TO GUESS ME!")
print("\n I'm thinking of a number between 1 and 100")
print("\n If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("\n If your guess is within 10 of my number, I'll tell you you're WARM")
print("\n If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("\n If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("\n LET'S PLAY!")

guesses = [0]

# Write a while loop that asks for a valid guess.

while True:
    guess = int(input("\n I'm thinking of a number between 1 and 100.\n\n  What is your guess? \n"))

    if guess < 1 or guess > 100:
        print('\n OUT OF BOUNDS! Please try again: ')
        continue
    break

while True:
    guess = int(input("\n I'm thinking of a number between 1 and 100.\n\n  What is your guess? \n"))

    if guess < 1 or guess > 100:
        print('\n OUT OF BOUNDS! Please try again: ')
        continue

    # here we compare the player's guess to our number

    if guess == num:
        print(f'\n Congratulations, You Guessed It In Only {len(guesses)} guesses!! \n')
        break

    # if guess is incorrect, and guess to the list

    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('\n\tWarmer!')
        else:
            print('\n\tColder!')

    else:
        if abs(num-guess) <= 10:
            print('\n\tWarm')
        else:
            print('\n\tCold')
