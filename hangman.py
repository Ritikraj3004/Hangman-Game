import random
from list import list_of_words as value
def hangman():
    
    word = random.choice (value)

    count = 0
    for i in word:
        if i == " ":
            continue
        else:
            count += 1
    print("Hint:- Length of word",count)

    turns = 10
    guessmade = ''
    txt =  'abcdefghijklmnopqrstuvwxyz0123456789'
    valid_entry = txt.upper()

    while len(word)>0:
        main_word = ""
        
        for letter in word:
            if letter in guessmade:
                main_word += letter
            else:
                if letter in valid_entry:
                    main_word +="_"
                else:
                    main_word +=" " 
                             
        if main_word == word:
            print(main_word.center(30))
            print("You Won!!!".center(30))  
            break
        
        print ("Guess the bollywood movies name -", main_word)
        guess = input().upper()
        
        if guess in valid_entry:
            guessmade = guessmade+guess
        else:
            print ("enter valid character")
            guess = input().upper()
            
        if guess not in word:
            turns = turns-1
            
            if turns == 9:
                print("9 turns left!!!")
                print("-------------")
            if turns == 8:
                print("8 turns left!!!")
                print("-------------")
                print("      O      ")
            if turns == 7:
                print("7 turns left!!!")
                print("-------------")
                print("      O      ")    
                print("      |      ")
            if turns == 6:
                print("6 turns left!!!")
                print("-------------")
                print("      O      ")    
                print("      |      ")    
                print("     /       ")
            if turns == 5:
                print("5 turns left!!!")
                print("-------------")
                print("      O      ")    
                print("      |      ")    
                print("     / \     ")    
            if turns == 4:
                print("4 turns left!!!")
                print("-------------")
                print("     \O      ")    
                print("      |      ")    
                print("     / \     ")      
            if turns == 3:
                print("3 turns left!!!")
                print("-------------")
                print("     \O/     ")    
                print("      |      ")    
                print("     / \     ") 
            if turns == 2:
                print("2 turns left!!!")
                print("-------------")
                print("      |      ")
                print("     \O/     ")    
                print("      |      ")    
                print("     / \     ")
            if turns == 1:
                print("Only 1 turns left!!! Hangman on his last breath")
                print("-------------")
                print("      |      ")
                print("     \O      ")    
                print("      |\     ")    
                print("     / \     ")    
            if turns == 0:
                print("You loose".center(25))
                print("You let the good man die".center(20))
                print("------------------------")
                print("            |           ")
                print("            |           ")
                print("            O           ")    
                print("           /|\          ")    
                print("           / \          ")
                print("!!GAME OVER!!".center(25))
                print("!!GAME OVER!!".center(25))
                print("!!GAME OVER!!".center(25))
                break
            
            
Name = input("Enter your name -> ")
print("    Welcome To Hangman Game !!!")
print(Name.center(30))
print("---------------------------------------------------------------")
print("Try to guess the bollywood movies name in less than 10 attempts")
hangman()