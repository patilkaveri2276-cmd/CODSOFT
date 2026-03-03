import tkinter as tk
import random

# Game choices
CHOICES = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(CHOICES)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update labels
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer Choice: ")
    result_label.config(text="Result will appear here")
    score_label.config(text="Score - You: 0  Computer: 0")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, height=2,
                         command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, height=2,
                          command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, height=2,
                             command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Display Labels
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here",
                        font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0",
                       font=("Arial", 12))
score_label.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset Game", width=15, height=2,
                         command=reset_game)
reset_button.pack(pady=10)

# Run application
root.mainloop()
