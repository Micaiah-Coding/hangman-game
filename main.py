# hangman game by Micaiah J.
print("\033[H\033[2J")
print("\033[1m-=Ξ Hangman Ξ=-\n\n\033[0m")

# ⋉import the ability to generate random words⋊

from random_word import RandomWords
r = RandomWords()

# ⊆functions⊇
    
def take_guess():
    # global lets you modify global variable
    global used_list
    while True:
        try:
            guess = input("Enter a letter: ")
            while len(guess) > 1:
                guess = input("Enter A letter: ")
            while guess.lower() not in "qwertyuiopasdfghjklzxcvbnm":
                guess = input("Enter a LETTER: ")
            while guess.strip() == "":
                guess = input("Actually enter a letter: ")
            while guess in used_list:
                guess = input("Enter a letter that you haven't guessed yet: ")
        except:
            print("Idk what you possibly could've tried to enter to get this message.. just enter a letter bro..")
            guess = input("Enter a letter: ")
        if len(guess) == 1 and guess.lower() in "qwertyuiopasdfghjklzxcvbnm":
            return guess

def check_guess(guess, state):
    global word
    global word_guesses
    global word_line
    global used_list
    global hangman_state
    
    while guess.lower() in word_guesses:
        guess_location = word_guesses.find(guess)
        if guess_location != -1:
            word_guesses = word_guesses[:guess_location] + "-" + word_guesses[guess_location + 1:]
            word_line = word_line[:guess_location] + guess.lower() + word_line[guess_location + 1:]
            if guess.lower() not in used_list:
                used_list = used_list + guess.lower() + ", "
    if guess.lower() not in word:
        hangman_state = state
        if guess.lower() not in used_list:
            used_list = used_list + guess.lower() + ", "
        
    """ 
    This code below is screwed up for some reason.. 
    I couldn't figure it out so i rewrote it differently above 
    """            
    
    # while guess.lower() in word_guesses:
    #     for i in range(len(word)):
    #         if word[i] == guess.lower() and guess.lower() not in used_list:
    #             word_line = word_line[:i] + guess.lower() + word_line[i+1:]
    #             word_guesses = word_guesses[:i] + "-" + word_guesses[i+1:]
    #             if guess.lower() not in used_list:
    #                 used_list = used_list + guess.lower() + ", "
                
    #         else:
    #             if guess not in word:
    #                 hangman_state = state
    #                 if guess.lower() not in used_list:
    #                     used_list = used_list + guess.lower() + ", "

# ⋖establish username⋗

username = input("Enter username: ")
username = username.lower()

for i in range(len(username)):
    if username[i] == " ":
        username = username[:i] + "_" + username[i + 1:]

change = input("\nConfirm username (Press enter. Type \"n\" for a username change.): " + username + "? ")

if change.lower == "n":
    username = input("\nEnter username: ")

print("\033[H\033[2J")

# ⦕main game⦖
game_num = 0
games_won = 0
word = r.get_random_word()
word_guesses = word
word_line = "-"*len(word)
used_list = ""
hangman_state = "full"
hangman = "     ________\n    |       |\n    |       O\n    |      _⊥_\n    |     / | \ \n    |       |\n    |       ⋀\n    |      / \ \n  ______\n"
while True:
    try:
        game_num_choice = int(input("How many times would you like to play? (enter -1 for until you lose): "))
        while game_num_choice <= 0 and game_num_choice != -1:
            game_num_choice = int(input("You can't enter that, Enter a positive whole number or -1."))
        break
    except:
        print("something went wrong with what you entered.. please enter a real whole number.\n")

while game_num != game_num_choice:
    #if the hangman hasn't lost anything
    if hangman_state == "full":
        print("\033[H\033[2J")
        print("\033[1mGame " + str(game_num+1) +"\033[0m")
        print(hangman)
        print(word_line)
        if used_list != "": 
            print("\nUsed letters: " + used_list)
        check_guess(take_guess(), "-leg1")
    
    #if the hangman doesn't have 1 leg
    elif hangman_state == "-leg1":
        print("\033[H\033[2J")
        print("\033[1mGame " + str(game_num+1) +"\033[0m\n")
        print(hangman[:100] + "⧵" + hangman[101:113] + " " + hangman[114:])
        print(word_line)
        print("\nUsed letters: " + used_list)
        check_guess(take_guess(), "-leg2")
    
    #if the hangman doesn't have legs    
    elif hangman_state == "-leg2":
        print("\033[H\033[2J")
        print("\033[1mGame " + str(game_num+1) +"\033[0m\n")
        print(hangman[:100] + " " + hangman[101:113] + "   " + hangman[116:])
        print(word_line)
        print("\nUsed letters: " + used_list)
        check_guess(take_guess(), "-leg2_-arm1")
        
    #if the hangman doesn't have legs and an arm
    elif hangman_state == "-leg2_-arm1":
        print("\033[H\033[2J")
        print("\033[1mGame " + str(game_num+1) +"\033[0m\n")
        print(hangman[:70] + "  " + hangman[73:100] + " " + hangman[101:113] + "   " + hangman[116:])
        print(word_line)
        print("\nUsed letters: " + used_list)
        check_guess(take_guess(), "-leg2_-arm2")
    
    #if the hangman doesn't have any arms/legs
    elif hangman_state == "-leg2_-arm2":
        print("\033[H\033[2J")
        print("\033[1mGame " + str(game_num+1) +"\033[0m\n")
        print(hangman[:66] + "  " + hangman[68:70] + "  " + hangman[73:100] + " " + hangman[101:113] + "   " + hangman[116:])
        print(word_line)
        print("\nUsed letters: " + used_list)
        check_guess(take_guess(), "-body")
    
    #if the hangman doesn't have a body
    elif hangman_state == "-body":
        print("\033[H\033[2J")
        print("\033[1mGame " + str(game_num) +"\033[0m\n")
        print(hangman[:41] + hangman[41:53] + "   " + hangman[56:67] + "     " + hangman[73:86] + " " + hangman[88:92] + "\n    |" + hangman[94:100] + "\n    |" + hangman[116:])
        print(word_line)
        print("\nUsed letters: " + used_list)
        check_guess(take_guess(), "game over")
        
    #if you lose the game
    elif hangman_state == "game over":
        print("\033[H\033[2J")
        print("\033[1mGGs\033[0m")
        print("Your word was: \"" + word +  "\"\n- " + username + ": " + str(games_won))
        break
    
    #if you win a round
    if word_line == word:
        used_list = ""
        games_won += 1
        hangman_state = "full"
        game_num += 1
        
        if game_num != game_num_choice:
            word = r.get_random_word()
            word_guesses = word
            word_line = "-"*len(word)

if game_num_choice == game_num:
    print("\033[H\033[2J")
    print("\033[1mGGs\033[0m")
    print("Your word was: \"" + word +  "\"\n- " + username + ": " + str(games_won))