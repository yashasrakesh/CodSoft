import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    """Play one round of Rock-paper-scissors."""
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    winner = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{winner}", fg='blue')

def rock_clicked():
    """Handle rock button click."""
    play_game('rock')

def paper_clicked():
    """Handle paper button click."""
    play_game('paper')

def scissors_clicked():
    """Handle scissors button click."""
    play_game('scissors')

# Create the main window
root = tk.Tk()
root.title("Rock-paper-scissors Game")

# Create and configure widgets
rock_button = tk.Button(root, text="Rock",fg='red',font=("Arial",15,"bold"), command=rock_clicked, width=50)
rock_button.pack(pady=20)

paper_button = tk.Button(root, text="Paper",fg='light green',font=("Arial",15,"bold"), command=paper_clicked, width=50)
paper_button.pack(pady=20)

scissors_button = tk.Button(root, text="Scissors",fg='cyan',font=("Arial",15,"bold"), command=scissors_clicked, width=50)
scissors_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg='blue')
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
