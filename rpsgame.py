import random

def gorock(computer_choice):
    if  computer_choice==1:
        print("\nYour choice is Rock and Computer choice is also Rock.\nMatch Tie!!!")    
    elif computer_choice==2:
        print("\nYour choice is Rock and Computer choice is Paper.\nYou Lose the game!!!")    
    else:
        print("\nYour choice is Rock and Computer choice is Scissors.\nYou Win the game!!!") 

def gopaper(computer_choice):
    if computer_choice==1:
        print("\nYour choice is Paper and Computer choice is Rock.\nYou Win the game!!!")   
    elif computer_choice==2:
        print("\nYour choice is Paper and Computer choice is also Paper.\nMatch Tie!!!")    
    else:
        print("\nYour choice is Paper and Computer choice is Scissors.\nYou Lose the game!!!")

def goscissors(computer_choice):
    if computer_choice==1:
        print("\nYour choice is Scissors and Computer choice is  Rock.\nYou Lose the game!!!")   
    elif computer_choice==2:
        print("\nYour choice is Scissors and Computer choice is Paper.\nYou Win the game!!!")  
    else:
        print("\nYour choice is Scissors and Computer choice is also Scissors.\nMatch Tie!!!")

c='y'  
print("Welcome To Rock Paper And Scissors Game!!!")    
while c=='y' or c=='Y':
    print("\nYour Choice!!!")
    player_choice=int(input("Enter 1 for Rock,2 for Paper and 3 for Scissors:"))
    computer_choice=random.randint(1,3)
    if player_choice==1:
        gorock(computer_choice)
    elif player_choice==2:
        gopaper(computer_choice)
    else:
        goscissors(computer_choice)
    c=input("Do You Want To Play Again??(y/n)....")
print("\nThank You For Playing This Beautiful Game!!!")