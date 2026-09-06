#this project uses a while loop, if/else,and functions.

secret_number = 7

def play_game():
    print("___number guessing game___")
    print("guess a number between 1 and 10")

    while True:
        guess = int (input("enter your guess: "))
        if guess == secret_number:
            print("correct! you won!")
            break
        elif guess < secret_number:
            print("your guess is too small!")
        else:
            print("your guess is too large!")
play_game()