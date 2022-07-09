import random
number = random.randint(1,10)
player_name = input("Enter Player name")
number_of_guesses = 0
while number_of_guesses<5:
    guess = int(input("Enter The number"))
    number_of_guesses +=1
    if guess <number:
        print("Your Guess is too low")
    if guess>number:
        print("Your Guess is too high")
    if guess==number:
        print("You Win !! You guessed the number")
        break
if guess == number:
    print("You guessed the value in ",number_of_guesses,"Guesses")

else:
    print("You didn't guess the number")

   




