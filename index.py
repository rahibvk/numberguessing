import random

life = 5

range_start = int(input("Enter the starting range: "))
range_end = int(input("Enter the ending range: "))

x = random.randrange(range_start, range_end)

near1 = x - 10



while life <=5:
    
    guess = int(input("Guess the number: "))
    if x == guess:
        print("You guessed it right")
        quit()
    elif guess == near1:
        print("You are near")
        life -= 1
    elif life == 0:
        print("You lost")
        quit()
    elif x > 5:
        print("the number is greater than 5")
        life -= 1
    elif x < 5:
        print("the number is less than 5")
        life -= 1
    




