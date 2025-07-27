import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import threading

# === Initialize pygame mixer for sound ===
pygame.mixer.init()

def play_sound(file):
    def _play():
        try:
            pygame.mixer.music.load(f"sounds/{file}")
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")
    threading.Thread(target=_play, daemon=True).start()

# === Game Data ===
questions = [
    "Which planet is known as the Red Planet?",
    "Who developed the Python programming language?",
    "What is the capital of France?",
    "What is H2O commonly known as?",
    "Who was the first person to walk on the Moon?",
    "Which Indian cricketer is known as the 'Master Blaster'?",
    "What is the largest organ in the human body?"
]

options = [
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Linus Torvalds"],
    ["Berlin", "Madrid", "Paris", "Lisbon"],
    ["Salt", "Oxygen", "Hydrogen", "Water"],
    ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Rakesh Sharma"],
    ["Virat Kohli", "MS Dhoni", "Rahul Dravid", "Sachin Tendulkar"],
    ["Heart", "Skin", "Lungs", "Liver"]
]

correct_answers = [
    "Mars",
    "Guido van Rossum",
    "Paris",
    "Water",
    "Neil Armstrong",
    "Sachin Tendulkar",
    "Skin"
]

phone_friend_suggestions = [
    "I'm pretty sure it's Mars.",
    "That's definitely Guido van Rossum.",
    "Paris is the capital of France!",
    "H2O? That’s water, of course.",
    "Neil Armstrong was the first.",
    "Has to be Sachin Tendulkar.",
    "The skin is the largest organ."
]

prize_pool = [
    "₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000", "₹20,000", "₹40,000"
]

current_question = 0
used_5050 = False
used_phone = False

def next_question():
    global current_question
    if current_question < len(questions):
        q_label.config(text=questions[current_question])
        for i in range(4):
            buttons[i].config(text=options[current_question][i], state="normal", bg="SystemButtonFace")
        reset_timer()
    else:
        play_sound("Win.mp3")
        messagebox.showinfo("Congratulations!", "🎉 You have completed the quiz!")
        root.destroy()

def check_answer(index):
    global current_question
    answer = buttons[index]['text']
    if answer == correct_answers[current_question]:
        play_sound("Correct.mp3")
        buttons[index].config(bg="green")
        current_prize = prize_pool[current_question]
        messagebox.showinfo("Correct Answer!", f"🎉 You won {current_prize}!")
        prize_label.config(text=f"Prize: {current_prize}")
        root.after(1000, lambda: [reset_buttons(), next_step()])
    else:
        play_sound("Wrong.mp3")
        buttons[index].config(bg="red")
        correct_index = options[current_question].index(correct_answers[current_question])
        buttons[correct_index].config(bg="green")
        messagebox.showerror("Game Over", "❌ Wrong answer. Better luck next time!")
        root.destroy()

def reset_buttons():
    for b in buttons:
        b.config(state="normal", bg="SystemButtonFace")

def next_step():
    global current_question
    current_question += 1
    next_question()

def use_5050():
    global used_5050
    if used_5050:
        messagebox.showinfo("Used", "You have already used 50-50.")
        return
    used_5050 = True
    correct = correct_answers[current_question]
    correct_index = options[current_question].index(correct)
    removed = 0
    for i in range(4):
        if i != correct_index and removed < 2:
            buttons[i].config(text="", state="disabled")
            removed += 1

def use_phone():
    global used_phone
    if used_phone:
        messagebox.showinfo("Used", "You have already used Phone a Friend.")
        return
    used_phone = True
    play_sound("phoneafriend.mp3")
    messagebox.showinfo("Phone a Friend", phone_friend_suggestions[current_question])

def countdown():
    time = int(timer_label['text'])
    if time > 0:
        timer_label.config(text=str(time - 1))
        root.after(3000, countdown)
    else:
        messagebox.showinfo("Time's up!", "⏰ Time's up!")
        root.destroy()

def reset_timer():
    timer_label.config(text="30")
    countdown()

# === GUI Setup ===
root = tk.Tk()
root.title("Kaun Banega Crorepati")
root.geometry("1500x1200")
root.config(bg="black")

# === Background Image ===
bg_image = Image.open("image/bg.jpg")
bg_image = bg_image.resize((1500, 1200))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Play theme on startup
play_sound("theme.mp3")

# === Question Label ===
q_label = tk.Label(root, text="", font=("Georgia", 32, "bold"), fg="red", bg="black", wraplength=750, justify="center")
q_label.pack(pady=150)

# === Option Buttons ===
buttons = []
for i in range(4):
    b = tk.Button(root, text="", font=("Arial", 20), width=50, command=lambda i=i: check_answer(i))
    b.pack(pady=5)
    buttons.append(b)

# === Lifelines Frame ===
lifeline_frame = tk.Frame(root, bg="black")
lifeline_frame.pack(pady=15)

tk.Button(lifeline_frame, text="🧮 50-50", font=("Georgia", 20), command=use_5050).grid(row=0, column=0, padx=20)
tk.Button(lifeline_frame, text="📞 Phone a Friend", font=("Georgia", 20), command=use_phone).grid(row=0, column=1, padx=20)

# === Timer Label ===
timer_label = tk.Label(root, text="30", font=("Georgia", 24), fg="red", bg="black")
timer_label.pack(pady=10)

# === Prize Pool Label ===
prize_label = tk.Label(root, text="Prize: ₹0", font=("Georgia", 32), fg="red", bg="black")
prize_label.pack(pady=10)

# === Start the Game ===
next_question()
root.mainloop()
