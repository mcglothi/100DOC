import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

# Vars
answer = random.choice(word_list)
word_length = len(answer)
guessed_letters = []
end_of_game = False
lives = 6

# Create blank spaces
display = []
for space in range(word_length):
    display += "_"

# Clear screen and print logo
os.system('clear')
print(logo)

# Main loop of program
while not end_of_game:

    # Testing hints
    print(f'Cheat mode enabled: The answer is {answer}')
    print (f'Guessed letters: {guessed_letters}')

    # User Input
    print(stages[lives])
    print (f"{' '.join(display)}")
    guess=input("Guess a letter: ").lower()
        
    # Check for duplicate guess
    if guess in guessed_letters:
        print(f"You've already guessed {guess}, try again.\n")
    
    # Incorrect guess
    elif guess not in answer:
        print(f'{guess} is not in the word! Try again...')
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("You lose.")
            end_of_game = True
    # Correct guess    
    else:
        for position in range(word_length):
            current_letter = answer[position]
            if current_letter == guess:
                display[position] = current_letter

    # Append current guess to guessed_letters array
    guessed_letters.append(guess)

    # Check for victory
    if "_" not in display:
        end_of_game = True
        print(f"You guessed {answer}, you Win!")

