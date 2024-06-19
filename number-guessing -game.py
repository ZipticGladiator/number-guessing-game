import random

# Randomize an integer between 1 and 100
r = random.randint(1, 100)

guesses = 0

print("Please enter a number between 1 and 100: ")

# Loop until the user guesses the correct number
while True:
    try:
        # Take user input
        i = int(input())
        
        # Check if the integer is within range
        if i < 1 or i > 100:
            print("Your number is out of range. Please enter a number between 1 and 100.")
            continue
        
        guesses += 1  # Increment guesses
        
        if i == r:
            print('You have won!')
            print(f'It took you {guesses} guesses to find the answer.')
            break
        elif i < r:
            print('You have guessed too low. Try again:')
        else:
            print('You have guessed too high. Try again:')
    
    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 100.")
