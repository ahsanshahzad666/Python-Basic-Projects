import tkinter as tk
from tkinter import messagebox
 
def check_winner():
     global winner         ## chnages 
     for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
       if  buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
         # Highlight winning button
             buttons[combo[0]].config(bg="green")
             buttons[combo[1]].config(bg="green")
             buttons[combo[2]].config(bg="green")
             messagebox.showinfo("Tic-Tac-Toe", f"player {buttons[combo[0]]['text']} wins!")
            #  root.quit()    ## changes
             winner = True
             return
             
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:  # Only switch player if no one has won   ## changes
            toggle_player()
        # toggle_player()
        
        

        
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"player {current_player}'s turn") 



game_window = tk.Tk()      
game_window.title("Tic-Tac-Toe")


# Create buttons (grid 3x3)
buttons = [tk.Button(game_window, text="", font=("normal", 30), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i,button in enumerate(buttons):
    button.grid(row=i //3, column=i %3)
    
    
# Game state
current_player = "X"
winner = False


# Turn label
label = tk.Label(game_window, text=f"player {current_player}'s11 turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

game_window.mainloop()


