import random

print("🎮Welcome to Guess the number game!")
secret = random.randint(1,100)
attempts=0


while True:

    guess=int(input("🤔Enter your guess(1-100): "))
    attempts +=1

    if guess < secret:
        print("📉Your guess is too low!",guess)

    elif guess > secret:
         print("📈Your guess is too high!",guess)

    else:
        print("🎉Congratulations! you guess the correct number.:",guess)
        print("✅You guessed it in ",attempts,"attempts")
        break

 