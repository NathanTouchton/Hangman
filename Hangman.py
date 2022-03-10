from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
import random

print(logo)
lives = 6
chosen_word = random.choice(word_list)
display = []
guessed_letters = []
for letter in chosen_word:
    display += "_"

while "_" in display:
    
    if lives < 1:
        print("You lose!")
        break
    guess= input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You've already guessed that. Please pick something else.")
    else:
        guessed_letters.append(guess)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
            print("That letter isn't in the word. You lose a life.")
    print(stages[lives])
    print(display)

if lives >= 1:
    print("".join(display))
    print("You Win!")
print("Game Over")