#imported files
import random
import hangman_word
import hangman_art


#Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")


#letter's already guessed
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print(f'Psssst. You have already used {guess.upper()}')
        if len(guessed_letters) > 1:
            print(f'You have also guessed these following letters:')
            for i in range(len(guessed_letters)):
                print(guessed_letters[i])
    guessed_letters.append(guess)

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        print(f'You guessed {guess.upper()}.That is not in the Word. You lose a life ')

    # if lives is equal to 0 you lose
    if lives == 0:
        print("You lose.")
        end_of_game = True
