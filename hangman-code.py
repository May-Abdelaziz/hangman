knowledge_of_game = input("Hi, welcome to hangman! Do you know how to play hangman?")
if knowledge_of_game == 'no':
    print("The way you play hangman is the computer generates a word and you have to try to guess the letters in it. First it starts off with the easy mode, then medium, then hard. As you guess wrong letters, more parts of a stick figure are added. When the whole stick figure is complete, you lose the round. Ok, get ready to play!"
)
if knowledge_of_game == 'yes':
    print("Get ready to play!")
