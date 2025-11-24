print("ფინალური დავალება 2")

# 2.2 თამაში: გამოიცანი რიცხვი

from random import randint

 #გამოსაცნობი რიცხვების დიაპაზონია 1 დან 100 მდე

num = randint(1,100)

i = 1

print("guess the number from 1 to 100")

while True:
    try:
        guess = int(input(f"step #{i}. Your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess == num:
        print(f"You guessed it! The number was {num}.")
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")

    i += 1

    print()

print("Game over")