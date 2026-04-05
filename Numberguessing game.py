import random

secret = random.randint(1,100)
guess = None
attempt = 0

while (guess != secret):
    guess = int(input("Guess the number Between 1 - 100 : "))
    attempt += 1

    if guess > secret:
        print("High")
    elif guess < secret:
        print("Low")
    else:
        print("Found Correct")
    print("Total Attempts: ",attempt)
