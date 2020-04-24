def player_choice(choice):
    if choice==1:
        player_choice="Rock"
    elif choice==2:
        player_choice="Paper"
    else:
        player_choice="Scissors"
    return player_choice

def computer_choice(n):
    if n==1:
        computer_choice="Rock"
    elif n==2:
        computer_choice="Paper"
    else:
        computer_choice="Scissors"
    return computer_choice
player_choice=player_choice(choice)
computer_choice=computer_choice(n)