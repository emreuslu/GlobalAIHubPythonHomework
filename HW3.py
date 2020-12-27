"""HANGMAN GAME"""
import time
import random


usernameList = ["admin"]
passwordList = ["admin"]

HANGMAN = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

def add_user(username,password):

    usernameList.append(username)
    passwordList.append(password)
    print(f"Username and password saved. You can login")

def start_game():
    print("Loading...")
    time.sleep(2)
    health =  100 

    wordlist_file = open("wordlist.txt","r")
    wordlist = wordlist_file.readlines()
    wordlist = [i.replace("\n","") for i in wordlist]

    rndm = random.randrange(len(wordlist)+1)

    computer_choice = wordlist[rndm]
    computer_choice_list = list(computer_choice)

    print(f"************* GAME IS ON {username.upper()} *************")   

    underscore_list = []

    for i in range(len(computer_choice)):
        underscore_list.append("_")

    underscore_str = " ".join(map(str,underscore_list))
    print(underscore_str)

    indexes = []
    health = len(HANGMAN)
    false = 0

    while health > 0:
        user_choice = input(f"Guess?: ")
        if user_choice in computer_choice_list:    
            for i in range(len(computer_choice_list)):
                if user_choice == computer_choice_list[i]:
                    indexes.append(i)
                    for j in indexes:
                        underscore_list[j] = user_choice
                        indexes.clear()
            underscore_str = " ".join(map(str,underscore_list))
            print(underscore_str)   

            if "_" not in underscore_list:
                print("Congratsss!!!!")
                break
        else:
            print(HANGMAN[false])
            print(f"{underscore_str}\nTry again {username.upper()}! \n")
            false += 1
            health -= 1        
        
    if health == 0:
        print(f"Word was {computer_choice}")
        print("You lost! Bye Looser...  HAHAHHAHAHAHAHAHAHAHAHAHAHAHAHA")



def log_in(username,password):

    if username in usernameList and password in passwordList:
        print(f"Welcome {username.upper()}!")
        start_game()
    elif username in usernameList and password not in passwordList:
        print("Login failed! Wrong password!")
    elif username not in usernameList and password in passwordList:
        print("Login failed! Wrong username")
    elif username not in usernameList and password not in passwordList:
        print("User couldn't find! Please register!")        
    else:
        print("Login failed try again")

print("******************** WELCOME TO HANGMAN GAME! *********************")
print("Please sign in or register to play game!")

decision = input("SIGN IN Press 1\nREGISTER Press 2:")


if decision == "1":

    username = input("Username:")
    password = input("Password:")
    log_in(username,password)

elif decision == "2":

    username = input("Username:")
    password = input("Password:")

    add_user(username,password)
    log_in(username,password)

else:
    print("Upss.. Try again!")


