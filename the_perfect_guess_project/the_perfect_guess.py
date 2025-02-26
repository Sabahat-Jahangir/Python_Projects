from random import randint

print("----------------------------------")
print("        The Perfect Guess         ")
print("----------------------------------")

random_guess = randint(1, 50)
user_guess = -1
guesses = 0
while(random_guess != user_guess):
    user_guess = int(input("Guess the number :)"))
    guesses += 1
    if random_guess > user_guess:  
            print("Guess a higher number, please :) ")  
    elif random_guess < user_guess:  
            print("Guess a lower number, please :) ")  

print(f"You have guessed the number {random_guess} in {guesses} guesses :) ")

    