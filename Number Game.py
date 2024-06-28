import random
def guess_number():
    number_to_guess = random.randint(1,100)
    guessed = False
    print("Try to guess the number between 1 to 100")
    
    while not guessed:
        user_guess = input("Guess The Number: ")
        try:
            user_guess = int(user_guess)
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print("WOW! You have guessed the correct number.")
                guessed = True
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_number()
