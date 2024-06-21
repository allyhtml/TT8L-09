import datetime
from tkinter import Tk, Canvas, Button, PhotoImage, Label, messagebox, font
import sys
import os
import subprocess
import tkinter as tk
import random

# Function to open PDF files
def open_pdf(file_path):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.join(script_dir, file_path)
        print(f"Attempting to open PDF at: {abs_path}")
        if os.path.isfile(abs_path):
            print(f"File exists: {abs_path}")
            if sys.platform == 'win32':
                os.startfile(abs_path)
            elif sys.platform == 'darwin':
                subprocess.run(['open', abs_path])
            elif sys.platform == 'linux':
                subprocess.run(['xdg-open', abs_path])
        else:
            print(f"File does not exist: {abs_path}")
    except Exception as e:
        print(f"Failed to open {file_path}: {e}")

# Global Tkinter window
window = Tk()
window.geometry("1474x801")
window.configure(bg="#D1EAF0")
window.resizable(False, False)

# Function to clear the current canvas
def clear_canvas():
    for widget in window.winfo_children():
        widget.destroy()

# Dictionary to hold references to images to prevent garbage collection
images = {}

def load_image(image_path):
    try:
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None

# Main Menu Frame (Frame 0)
def show_frame0():
    clear_canvas()
    canvas = Canvas(
        window,
        bg="#D1EAF0",
        height=801,
        width=1474,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    images['image_deco'] = load_image("./build/assets/frame0/image_deco.png")
    canvas.create_image(1018.0, 161.0, image=images['image_deco'])

    images['image_logo'] = load_image("./build/assets/frame0/image_3.png")
    canvas.create_image(132.0, 50.0, image=images['image_logo'])

    kl_timezone = datetime.timezone(datetime.timedelta(hours=8)) 
    dt_mst = datetime.datetime.now(kl_timezone)
    formatted_date = dt_mst.strftime('%A, %B %d, %Y')
    date_label = Label(window, text=formatted_date, bg="#D1EAF0", font=("Arial", 16))
    date_label.place(x=626, y=31)

    images['button_signout'] = load_image("./build/assets/frame0/signout.png")
    button_signout = Button(
        image=images['button_signout'],
        borderwidth=0,
        highlightthickness=0,
        command=show_frame5,
        relief="flat"
    )
    button_signout.place(x=1250, y=35, width=150, height=50)

    images['image_hi'] = load_image("./build/assets/frame0/image_hi.png")
    canvas.create_image(737.0, 200.0, image=images['image_hi'])

    images['button_fc'] = load_image("./build/assets/frame0/button_fc.png")
    button_fc = Button(
        image=images['button_fc'],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_fc clicked"),
        relief="flat"
    )
    button_fc.place(x=974.0, y=298.0, width=425.0, height=432.0)

    images['button_ln'] = load_image("./build/assets/frame0/button_ln.png")
    button_ln = Button(
        image=images['button_ln'],
        borderwidth=0,
        highlightthickness=0,
        command=show_frame0,
        relief="flat"
    )
    button_ln.place(x=518.0, y=284.0, width=438.0, height=473.0)

    images['button_rq'] = load_image("./build/assets/frame0/button_rq.png")
    button_rq = Button(
        image=images['button_rq'],
        borderwidth=0,
        highlightthickness=0,
        command=quiz_selection_screen,
        relief="flat"
    )
    button_rq.place(x=65.0, y=284.0, width=440.0, height=473.0)

# Quiz Selection Screen
def quiz_selection_screen():
    clear_canvas()
    quiz_frame = tk.Frame(window, bg="#d1eaf0")
    quiz_frame.pack(fill="both", expand=True)
    
    quebiz_section = tk.Label(quiz_frame, text="QUEBIZ SECTION", font=("Comic Sans MS", 24), bg="#d1eaf0")
    quebiz_section.place(x=500, y=51)
    
    physic1 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic1.place(x=94, y=203)
    physic2 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic2.place(x=558, y=203)
    physic3 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic3.place(x=1022, y=203)
    
    digital_system_label = tk.Label(quiz_frame, text="DIGITAL SYSTEM", font=("Arial", 18, "bold"), bg="#ffc8c0", fg="#000")
    digital_system_label.place(x=144, y=222)
    mathematics_label = tk.Label(quiz_frame, text="MATHEMATICS", font=("Arial", 18, "bold"), bg="#ffc8c0", fg="#000")
    mathematics_label.place(x=624, y=222)
    physic_label = tk.Label(quiz_frame, text="PHYSIC", font=("Arial", 18, "bold"), bg="#ffc8c0", fg="#000")
    physic_label.place(x=1150, y=222)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    saly_16_img = tk.PhotoImage(file=os.path.join(current_dir, "Design/Saly-16.png"))
    saly_16_img = saly_16_img.subsample(1)
    saly_10_img = tk.PhotoImage(file=os.path.join(current_dir, "Design/Saly-10.png"))
    saly_19_img = tk.PhotoImage(file=os.path.join(current_dir, "Design/Saly-19.png"))
    
    saly_16_label = tk.Label(quiz_frame, image=saly_16_img, bg="#FFC8C0")
    saly_16_label.place(x=1064, y=260)
    saly_16_label.image = saly_16_img
    saly_10_label = tk.Label(quiz_frame, image=saly_10_img, bg="#FFC8C0")
    saly_10_label.place(x=578, y=272)
    saly_19_label = tk.Label(quiz_frame, image=saly_19_img, bg="#FFC8C0")
    saly_19_label.place(x=122, y=260)
    
    button_ds = tk.Button(quiz_frame, text="START", font=("Zen Dots", 12), bg="#d1eaf0", command=open_ds_quiz)
    button_ds.place(x=195, y=635, width=180, height=50)
    button_math = tk.Button(quiz_frame, text="START", font=("Zen Dots", 12), bg="#d1eaf0", command=open_math_quiz)
    button_math.place(x=659, y=635, width=180, height=50)
    button_physic = tk.Button(quiz_frame, text="START", font=("Zen Dots", 12), bg="#d1eaf0", command=open_physic_quiz)
    button_physic.place(x=1123, y=635, width=180, height=50)

# Sign Out Frame (Frame 5)
def show_frame5():
    clear_canvas()
    canvas = Canvas(
        window,
        bg="#D1EAF0",
        height=801,
        width=1474,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    images['image_signout'] = load_image("./build/assets/frame5/image_signout.png")
    canvas.create_image(737.0, 282.0, image=images['image_signout'])

    images['button_signout'] = load_image("./build/assets/frame5/button_signout.png")
    button_signout = Button(
        image=images['button_signout'],
        borderwidth=0,
        highlightthickness=0,
        command=window.quit,
        relief="flat"
    )
    button_signout.place(x=637.0, y=491.0, width=200.0, height=60.0)

# Quiz Game Code
class QuizGame:
    def __init__(self, root, questions):
        self.root = root
        custom_font = font.Font(family="Helvetica", size=14)
        self.questions = questions
        random.shuffle(self.questions)
        self.score = 0
        self.current_question_index = 0
        self.question_label = tk.Label(self.root, text="", font=custom_font, wraplength=600, bg="#F8C6EF")
        self.question_label.pack(pady=20)
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=custom_font, width=50, height=3, command=lambda i=i: self.check_answer(i), bg="#F1D1CC")
            button.pack(pady=10)
            self.option_buttons.append(button)
        self.score_label = tk.Label(self.root, text="Score: 0", font=custom_font, bg="#D1EAF0")
        self.score_label.pack(pady=20)
        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            random.shuffle(options)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
        else:
            self.end_game()

    def check_answer(self, selected_option):
        selected_answer = self.option_buttons[selected_option].cget("text")
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect! The correct answer is: {correct_answer}")
        self.score_label.config(text="Score: {}".format(self.score))
        self.current_question_index += 1
        self.display_question()

    def end_game(self):
        score_message = "Final Score: {}/{}".format(self.score, len(self.questions))
        self.question_label.config(text=score_message)
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 12), command=self.play_again)
        play_again_button.pack(pady=10)
        back_button = tk.Button(self.root, text="Back to Quiz Selection", font=("Arial", 12), command=quiz_selection_screen)
        back_button.pack(pady=10)

    def play_again(self):
        self.score = 0
        self.current_question_index = 0
        self.score_label.config(text="Score: 0")
        random.shuffle(self.questions)
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)
        self.display_question()

def open_ds_quiz():
    questions_ds = [
        {
            "question": "Which of the following is a fundamental building block of digital circuits?",
            "options": ["Resistor", "Transistor", "Diode", "Inductor"],
            "answer": "Transistor"
        },
    ]
    clear_canvas()
    app_ds = QuizGame(window, questions_ds)

def open_math_quiz():
    questions_math = [
        {
            "question": "If a1 = 3 and an = 2an-1 + 5 for n ≥ 2, what is a3?",
            "options": ["17", "21", "19", "23"],
            "answer": "21"
        },
    ]
    clear_canvas()
    app_math = QuizGame(window, questions_math)

def open_physic_quiz():
    questions_physic = [
        {
            "question": "Which of the following is not a type of motion?",
            "options": ["Translational", "Rotatinal", "Oscillatory", "Vibrational"],
            "answer": "Vibrational"
        },
    ]
    clear_canvas()
    app_physic = QuizGame(window, questions_physic)

# Start the application
show_frame0()
window.mainloop()

                                  

