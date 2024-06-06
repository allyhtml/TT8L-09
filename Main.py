import tkinter as tk
from tkinter import font, messagebox, PhotoImage, Label, Frame, Entry, Button, Toplevel
import random
import os

# First code: Sign-in and Registration System
def signin():
    email = user.get()
    password = code.get()

    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    saved_email, saved_password = parts
                    if email == saved_email and password == saved_password:
                        messagebox.showinfo("Success", "Login successful!")
                        main_frame.pack_forget()
                        quiz_selection_screen()
                        return
        messagebox.showerror("Error", "Invalid email or password")
    except FileNotFoundError:
        messagebox.showerror("Error", "No registered users found. Please register first.")

def on_enter_email(e):
    if user.get() == 'Email':
        user.delete(0, 'end')

def on_leave_email(e):
    if user.get() == '':
        user.insert(0, 'Email')

def on_enter_password(e):
    if code.get() == 'Password':
        code.delete(0, 'end')
        code.config(show='*')

def on_leave_password(e):
    if code.get() == '':
        code.config(show='')
        code.insert(0, 'Password')

def save_registration():
    email_val = user_entry.get()
    password_val = password_entry.get()

    if not email_val.endswith('@gmail.com'):
        messagebox.showerror("Error", "Invalid email. Please use a valid Gmail address.")
        return

    if len(password_val) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    try:
        with open("user_data.txt", "a") as file:
            file.write(f"{email_val},{password_val}\n")
        messagebox.showinfo("Success", "Registration successful!")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Failed to register. Please try again later.")

def register():
    global user_entry, password_entry
    reg_window = Toplevel(root)
    reg_window.title("Registration")
    reg_window.geometry('400x250+500+300')
    reg_window.config(bg="white")

    reg_label = Label(reg_window, text="Register your account", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
    reg_label.pack()

    email_label = Label(reg_window, text="Email:", bg="white", font=('Microsoft YaHei UI Light', 11))
    email_label.pack()
    user_entry = Entry(reg_window, width=25, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
    user_entry.pack()

    password_label = Label(reg_window, text="Password:", bg="white", font=('Microsoft YaHei UI Light', 11))
    password_label.pack()
    password_entry = Entry(reg_window, width=25, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11), show='*')
    password_entry.pack()

    register_button = Button(reg_window, text="Register", bg='#57a1f8', fg='white', command=save_registration)
    register_button.pack()


# Second code: Quiz Game
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
            "question": "Digital System Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Digital System Question 2",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 2"
        },
        # Add more questions as needed
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_ds = QuizGame(quiz_frame, questions_ds)

def open_math_quiz():
    questions_math = [
        {
            "question": "Mathematics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Mathematics Question 2",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 2"
        },
        # Add more questions as needed 
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_math = QuizGame(quiz_frame, questions_math)

def open_physic_quiz():
    questions_physic = [
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 2",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 2"
        },
        # Add more questions as needed
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_physic = QuizGame(quiz_frame, questions_physic)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def quiz_selection_screen():
    global quiz_frame, saly_16_img, saly_10_img, saly_19_img
    main_frame.pack_forget()
    quiz_frame = tk.Frame(root, bg="#d1eaf0")
    quiz_frame.pack(fill="both", expand=True)
    
    quebiz_section = tk.Label(quiz_frame, text="QUEBIZ SECTION", font=comic_sans_font, bg="#d1eaf0")
    quebiz_section.place(x=500, y=51)
    
    physic1 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic1.place(x=94, y=203)
    physic2 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic2.place(x=558, y=203)
    physic3 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic3.place(x=1022, y=203)
    
    digital_system_label = tk.Label(quiz_frame, text="DIGITAL SYSTEM", font=stylish_font, bg="#ffc8c0", fg="#000")
    digital_system_label.place(x=144, y=222)
    mathematics_label = tk.Label(quiz_frame, text="MATHEMATICS", font=stylish_font, bg="#ffc8c0", fg="#000")
    mathematics_label.place(x=624, y=222)
    physic_label = tk.Label(quiz_frame, text="PHYSIC", font=stylish_font, bg="#ffc8c0", fg="#000")
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
    
    button_ds = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_ds_quiz)
    button_ds.place(x=195, y=635, width=180, height=50)
    button_math = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_math_quiz)
    button_math.place(x=659, y=635, width=180, height=50)
    button_physic = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_physic_quiz)
    button_physic.place(x=1123, y=635, width=180, height=50)

# Main application setup
root = tk.Tk()
root.title('Login and Quiz Application')
root.geometry('1474x801')  # Adjusted geometry to match second code
root.configure(bg="#ffc0db")
root.resizable(False, False)

comic_sans_font = font.Font(family='Comic Sans MS', size=40)
stylish_font = font.Font(family='Stylish', size=20)
zen_dots_font = font.Font(family='Zen Dots', size=20)

main_frame = tk.Frame(root, bg="#ffc0db")
main_frame.place(relwidth=1, relheight=1)

img = PhotoImage(file='Design/logo.png')
Label(main_frame, image=img, bg='white').place(x=-100, y=60)

frame = Frame(main_frame, width=350, height=350, bg="white")
frame.place(relx=0.5, rely=0.5, anchor='center')

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.pack(pady=10)

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.pack(pady=10)
user.insert(0, 'Email')
user.bind('<FocusIn>', on_enter_email)
user.bind('<FocusOut>', on_leave_email)

Frame(frame, width=295, height=2, bg='black').pack()

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.pack(pady=10)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').pack()

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).pack(pady=10)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.pack(pady=10)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=register)
sign_up.pack()

root.mainloop()
