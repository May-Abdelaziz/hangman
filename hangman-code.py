import random
def stick_figure(wrong_guesses):
    if wrong_guesses == 0:
        print("-----")
    if wrong_guesses == 1:
        print(" -----")
        print("|     |")
    if wrong_guesses == 2:
        print(" -----")
        print("|     |")
        print("|     |")
    if wrong_guesses == 3:
        print(" -----")
        print("|     |")
        print("|     |")
        print(" ----- ")
    if wrong_guesses == 4:
        print(" -----")
        print("|     |")
        print("|     |")
        print(" ----- ")
        print("   |   ")
    if wrong_guesses == 5:
        print(" -----")
        print("|     |")
        print("|     |")
        print(" ----- ")
        print("   |   ")
        print("---|---")
    if wrong_guesses == 6:
        print(" -----")
        print("|     |")
        print("|     |")
        print(" ----- ")
        print("   |   ")
        print("---|---")
        print("  / \\") 
    if wrong_guesses == 7: 
        print(" -----")
        print("|     |")
        print("|     |")
        print(" ----- ")
        print("   |   ")
        print("---|---")
        print("  / \\")
        print(" /   \\")
wrong_guesses = 0
knowledge_of_game = input("Hi, welcome to hangman! Do you know how to play hangman?")
if knowledge_of_game == 'no':
    print("The way you play hangman is the computer generates a word and you have to try to guess the letters in it. As you guess wrong letters, more parts of a stick figure are added. When the whole stick figure is complete, you lose the round. Ok, get ready to play!"
)
if knowledge_of_game == 'yes':
    print("Get ready to play!")
words = open('words.txt').read().split('\n')
chosen_word = words[random.randint(0,len(words))]
guessed_letters = "_" * len(chosen_word)
playing = True
while playing :


    guess_letter = input("Guess a letter that could be in the word.")
    if guess_letter in chosen_word:
        print("Correct!")
    else:
        print("No, that letter was not in the word.")
        wrong_guesses = wrong_guesses+1
    for i in range(0, len(chosen_word)):
        if guess_letter == chosen_word[i]:
            guessed_letters = guessed_letters[0:i]+guess_letter+guessed_letters[i+1:]
    
    print(guessed_letters)
    stick_figure(wrong_guesses)
    if guessed_letters == chosen_word:
        playing = False
        end_of_game = "Congratulations! You have completed the game!"
        print(end_of_game)
    elif wrong_guesses == 8:
        playing = False
        too_many_guesses = "Sorry, you have guessed too many incorrect letters! Game over. Better luck next time!"
        print(too_many_guesses)
        print("The word was" + " " + chosen_word + "!")