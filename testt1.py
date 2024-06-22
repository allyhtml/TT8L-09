#LOGIN AND REGISTRATION CODE

import tkinter as tk
from tkinter import font, messagebox, PhotoImage, Label, Frame, Entry, Button, Toplevel
import os

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

# Main application setup
root = tk.Tk()
root.title('Login and Quiz Application')
root.geometry('1474x801')
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



#QUIZ SELECTION CODE
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


#QUIZ GAME CODE
import random

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
        self.score_label = tk.Label(self.root, text="Score:0", font=custom_font, bg="#D1EAF0")
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
        back_button = tk.Button(self.root, text="Back to Quiz Selection", font=("Arial", 12), command=go_back_to_selection)
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
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_ds = QuizGame(quiz_frame, questions_ds)

def open_math_quiz():
    questions_math = [
        {
            "question": "If a1 = 3 and an = 2an-1 + 5 for n ≥ 2, what is a3?",
            "options": ["17", "21", "19", "23"],
            "answer": "21"
        },
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_math = QuizGame(quiz_frame, questions_math)

def open_physic_quiz():
    questions_physic = [
        {
            "question": "Which of the following is not a type of motion?",
            "options": ["Translational", "Rotatinal", "Oscillatory", "Vibrational"],
            "answer": "Vibrational"
        },
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_physic = QuizGame(quiz_frame, questions_physic)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()



#BUTTON BACK TO QUIZ SELECTION CODE
def go_back_to_selection():
    quiz_frame.pack_forget()
    quiz_selection_screen()



#MAIN MENU PAGE CODE
import datetime
from tkinter import Tk, Canvas, Button, PhotoImage, Label
import sys
import os
import subprocess

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
        command=show_frame1,
        relief="flat"
    )
    button_ln.place(x=518.0, y=284.0, width=438.0, height=473.0)

    images['button_rq'] = load_image("./build/assets/frame0/button_rq.png")
    button_rq = Button(
        image=images['button_rq'],
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_rq clicked"),
        relief="flat"
    )
    button_rq.place(x=65.0, y=284.0, width=440.0, height=473.0)



#LECTURE NOTES PHYSIC CODE
def show_frame1():
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

    images['image_lectn'] = load_image("./build/assets/frame1/image_lectn.png")
    canvas.create_image(732.0, 131.0, image=images['image_lectn'])

    images['button_maths'] = load_image("./build/assets/frame1/button_maths.png")
    button_maths = Button(
        image=images['button_maths'],
        borderwidth=0,
        highlightthickness=0,
        command=show_frame4,  # Correct frame function
        relief="flat"
    )
    button_maths.place(x=970.0, y=249.0, width=435.0, height=472.0)

    images['button_ds'] = load_image("./build/assets/frame1/button_ds.png")
    button_ds = Button(
        image=images['button_ds'],
        borderwidth=0,
        highlightthickness=0,
        command=show_frame3,  # Correct frame function
        relief="flat"
    )
    button_ds.place(x=522.0, y=258.0, width=438.0, height=473.0)

    images['button_phy'] = load_image("./build/assets/frame1/button_phy.png")
    button_phy = Button(
        image=images['button_phy'],
        borderwidth=0,
        highlightthickness=0,
        command=show_frame2,  # Correct frame function
        relief="flat"
    )
    button_phy.place(x=69.0, y=258.0, width=440.0, height=473.0)

    images['image_logo'] = load_image("./build/assets/frame1/image_logo.png")
    canvas.create_image(44.0, 41.0, image=images['image_logo'])

    images['button_back'] = load_image("./build/assets/frame1/button_back.png")
    button_back = Button(
        image=images['button_back'],
        borderwidth=0,
        highlightthickness=0,
        command=show_frame0,
        relief="flat"
    )
    button_back.place(x=667.0, y=721.0, width=153.0, height=61.0)



#PHYSIC NOTES PDF CODE
# Physics Lecture Notes Frame (Frame 2)
def show_frame2():
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

    images['image_phy'] = load_image("./build/assets/frame2/image_phy.png")
    canvas.create_image(740.0, 157.0, image=images['image_phy'])

    images['image_logo'] = load_image("./build/assets/frame2/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_1.png", lambda: open_pdf("assets/physics/phyn_1.pdf"), 72, 291, 446, 112),
        ("button_2.png", lambda: open_pdf("assets/physics/phyn_2.pdf"), 518, 278, 439, 125),
        ("button_3.png", lambda: open_pdf("assets/physics/phyn_3.pdf"), 957, 280, 439, 125),
        ("button_4.png", lambda: open_pdf("assets/physics/phyn_4.pdf"), 518, 546, 439, 125),
        ("button_5.png", lambda: open_pdf("assets/physics/phyn_5.pdf"), 80, 405, 427, 125),
        ("button_6.png", lambda: open_pdf("assets/physics/phyn_6.pdf"), 518, 407, 439, 125),
        ("button_7.png", lambda: open_pdf("assets/physics/phyn_7.pdf"), 957, 409, 439, 125),
        ("button_back.png", show_frame1, 651, 707, 153, 61)
    ]

    for btn_img, btn_cmd, x, y, w, h in buttons:
        images[btn_img] = load_image(f"./build/assets/frame2/{btn_img}")
        button = Button(
            image=images[btn_img],
            borderwidth=0,
            highlightthickness=0,
            command=btn_cmd,
            relief="flat"
        )
        button.place(x=x, y=y, width=w, height=h)




#DS AND MATH LECTURE PDF CODE
# Data Structures Lecture Notes Frame (Frame 3)
def show_frame3():
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

    images['image_ds'] = load_image("./build/assets/frame3/image_ds.png")
    canvas.create_image(733.0, 160.0, image=images['image_ds'])

    images['image_logo'] = load_image("./build/assets/frame3/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_1.png", lambda: open_pdf("assets/ds/dsn_1.pdf"), 84, 319, 432, 114),
        ("button_2.png", lambda: open_pdf("assets/ds/dsn_2.pdf"), 519, 318, 440, 114),
        ("button_3.png", lambda: open_pdf("assets/ds/dsn_3.pdf"), 957, 318, 436, 114),
        ("button_4.png", lambda: open_pdf("assets/ds/dsn_4.pdf"), 83, 478, 433, 114),
        ("button_5.png", lambda: open_pdf("assets/ds/dsn_5.pdf"), 518, 478, 440, 114),
        ("button_6.png", lambda: open_pdf("assets/ds/dsn_6.pdf"), 957, 478, 436, 114),
        ("button_7.png", lambda: open_pdf("assets/ds/dsn_7.pdf"), 957, 636, 436, 114),
        ("button_back.png", show_frame1, 655, 721, 153, 61)
    ]

    for btn_img, btn_cmd, x, y, w, h in buttons:
        images[btn_img] = load_image(f"./build/assets/frame3/{btn_img}")
        button = Button(
            image=images[btn_img],
            borderwidth=0,
            highlightthickness=0,
            command=btn_cmd,
            relief="flat"
        )
        button.place(x=x, y=y, width=w, height=h)

# Mathematics Lecture Notes Frame (Frame 4)
def show_frame4():
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

    images['image_maths'] = load_image("./build/assets/frame4/image_maths.png")
    canvas.create_image(739.0, 155.0, image=images['image_maths'])

    images['image_logo'] = load_image("./build/assets/frame4/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_1.png", lambda: open_pdf("assets/maths/mn_1.pdf"), 68, 292, 459, 109),
        ("button_2.png", lambda: open_pdf("assets/maths/mn_2.pdf"), 526, 292, 440, 109),
        ("button_3.png", lambda: open_pdf("assets/maths/mn_3.pdf"), 973, 292, 448, 109),
        ("button_4.png", lambda: open_pdf("assets/maths/mn_4.pdf"), 69, 438, 458, 109),
        ("button_5.png", lambda: open_pdf("assets/maths/mn_5.pdf"), 527, 438, 440, 109),
        ("button_6.png", lambda: open_pdf("assets/maths/mn_6.pdf"), 973, 438, 448, 109),
        ("button_7.png", lambda: open_pdf("assets/maths/mn_7.pdf"), 524, 595, 440, 109),
        ("button_back.png", show_frame1, 651, 707, 153, 61)
    ]

    for btn_img, btn_cmd, x, y, w, h in buttons:
        images[btn_img] = load_image(f"./build/assets/frame4/{btn_img}")
        button = Button(
            image=images[btn_img],
            borderwidth=0,
            highlightthickness=0,
            command=btn_cmd,
            relief="flat"
        )
        button.place(x=x, y=y, width=w, height=h)




#SIGN OUT PAGE CODE
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




#RUNNING THE MENU PAGE CODE
# Display main menu
show_frame0()
window.mainloop()
