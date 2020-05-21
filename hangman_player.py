import hangman_creator

hangman = hangman_creator.Hangman('M:\\wordlist.txt')
hangman.choose_the_word()
hangman.fill_the_word_status()

while True:
    hangman.get_word_status()
    hangman.guess_the_letter()


    if(hangman.attempts_remaining == 0):
        print("Gamer Over")

        break

    elif(hangman.chosen_word == ''.join(hangman.word_status)):
        print("You Won The Game")


