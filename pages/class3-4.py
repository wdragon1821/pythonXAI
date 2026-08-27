import random

answer = random.randint(1, 100)

low = 1
high = 100

print("🎯 Guess the Number!")

while True:
    print(f"Pick a number from {low} to {high}.")

    number = int(input())

    if number == answer:
        print("🎉 Correct!")
        break

    elif number < answer:
        print("⬆️ Higher!")
        low = number

    else:
        print("⬇️ Lower!")
        high = number