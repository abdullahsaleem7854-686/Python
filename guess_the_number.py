import random
def play_game():
    lucky_number = random.randint(1,100)
    while True:
        user_guess = int(input("Enter a number: "))
        if user_guess == lucky_number:
            print("You have won. Game over!")
            break
        elif user_guess < lucky_number:
            print("too Low.")
        else:
            print("too High.")

    print("Thank You for playing.")

play_game()

