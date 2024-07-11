import random

life = 5

x = random.randrange(-1,11)



while life <=5:
    guess = int(input("Guess the number: "))
    if x == guess:
        print("You guessed it right")
        quit()
    elif life == 0:
        print("You lost")
        quit()
    elif x > 5:
        print("the number is greater than 5")
        life -= 1
    elif x < 5:
        print("the number is less than 5")
        life -= 1
    elif life == 0:
        print("You lost")
        quit()
        




