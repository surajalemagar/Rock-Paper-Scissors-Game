import random

def Result(player_choice,computer_choice):
    if player_choice==1:
        if  computer_choice==1:
            print("Your choice is Rock and Comuter choice is also Rock.\nMatch Tie!!!")    
        elif computer_choice==2:
            print("Your choice is Rock and Comuter choice is Paper.\nYou Lose the game!!!")    
        else:
            print("Your choice is Rock and Comuter choice is Scissors.\nYou Win the game!!!") 

    elif player_choice==2:
        if computer_choice==1:
            print("Your choice is Paper and Comuter choice is Rock.\nYou Win the game!!!")   
        elif computer_choice==2:
            print("Your choice is Paper and Comuter choice is also Paper.\nMatch Tie!!!")    
        else:
            print("Your choice is Paper and Comuter choice is Scissors.\nYou Lose the game!!!")
            
    else:
        if computer_choice==1:
            print("Your choice is Scissors and Comuter choice is  Rock.\nYou Lose the game!!!")   
        elif computer_choice==2:
            print("Your choice is Scissors and Comuter choice is Paper.\nYou Win the game!!!")  
        else:
            print("Your choice is Scissors and Comuter choice is also Scissors.\nMatch Tie!!!")


print("Player Choice!!!")
player_choice=int(input("Enter 1 for Rock,2 for Paper and 3 for Scissors:"))
computer_choice=random.randint(1,3)
Result(player_choice,computer_choice)