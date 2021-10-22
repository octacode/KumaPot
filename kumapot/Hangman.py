from replit import clear
import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo,stages

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    
    if guess in display:
      print(f"You've already guessed {guess} letter")

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        if guess not in display:
          print(f"You've guessed {guess} wrong.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

  
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])