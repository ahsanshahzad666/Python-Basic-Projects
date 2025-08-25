"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random

item_list = ['rock', 'paper', 'scissor']
your_choice = input("Enter your Choice = ('rock', 'paper', 'scissor'):- ")
computer_choice = random.choice(item_list)

print(f"Your Choice = {your_choice}")
print(f"computer Choice = {computer_choice}")

# A- Rock cases
if your_choice == computer_choice:
    print("Both are same, Match Tie")
    
elif your_choice.lower() == 'rock':
    if computer_choice .lower() == 'paper':
        print("Computer Win 😭")
        
    elif computer_choice.lower() == 'scissor':
        print("You Win 😎")
        
elif your_choice.lower() == 'paper':
    if computer_choice .lower() == 'scissor':
        print("Computer Win 😭")
        
    elif computer_choice.lower() == 'rock':
        print("You Win 😎")
        
        
elif your_choice.lower() == 'scissor':
    if computer_choice .lower() == 'rock':
        print(f"computer Win 😭")
        
    elif computer_choice.lower() == 'paper':
        print(f"You Win 😎")

