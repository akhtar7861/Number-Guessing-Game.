import random
# The Line Guess a Number Between 1 to 10 by Computer.
computer=random.randint(1,10)
user=0
attempts=0
print("Welcome My Guessed Number Game.")

# while loop will continue to run until the user guess matches the computer number.
while user!=computer:
    user=int(input("Guess a Number:"))
    # After each guess number, the attempts are increased by 1.
    attempts +=1

    if user<computer:
        print("Higher Number")
    elif user>computer:
        print("Lower Number")
# Print success. when the user guess a number correctly.        
print(f"success. computer choosed a {computer} number and You guessed in {attempts} attempts.")            