import datetime
from tkinter import Tk, Canvas, Button, PhotoImage, Label, messagebox, font, Frame, Entry, Toplevel
import sys
import os
import subprocess
import tkinter as tk
import random

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
                        messagebox.showinfo("Success", "Successfully signed in!")
                        root.destroy()  # Close the main window after successful sign-in
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
root.geometry('1474x801')  # Adjusted geometry to match second code
root.configure(bg="#ffc0db")
root.resizable(False, False)

comic_sans_font = font.Font(family='Comic Sans MS', size=40)
stylish_font = font.Font(family='Stylish', size=20)
zen_dots_font = font.Font(family='Zen Dots', size=20)

main_frame = tk.Frame(root, bg="#ffc0db")
main_frame.place(relwidth=1, relheight=1)

img = PhotoImage(file='build/assets/Design/logo.png')
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

    images['image_deco'] = load_image("./build/assets/frame0/image_deco.png")
    canvas.create_image(1018.0, 161.0, image=images['image_deco'])

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
        command=quiz_selection_screen,
        relief="flat"
    )
    button_rq.place(x=65.0, y=284.0, width=440.0, height=473.0)

# Lecture Notes Frame (Frame 1)
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

# Physics Notes (Frame 2)
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
        ("button_1.png", lambda: open_pdf("assets\\physics\\phyn_1.pdf"), 72, 291, 446, 112),
        ("button_2.png", lambda: open_pdf("assets\\physics\\phyn_2.pdf"), 518, 278, 439, 125),
        ("button_3.png", lambda: open_pdf("assets\\physics\\phyn_3.pdf"), 957, 280, 439, 125),
        ("button_4.png", lambda: open_pdf("assets\\physics\\phyn_4.pdf"), 518, 546, 439, 125),
        ("button_5.png", lambda: open_pdf("assets\\physics\\phyn_5.pdf"), 80, 405, 427, 125),
        ("button_6.png", lambda: open_pdf("assets\\physics\\phyn_6.pdf"), 518, 407, 439, 125),
        ("button_7.png", lambda: open_pdf("assets\\physics\\phyn_7.pdf"), 957, 409, 439, 125),
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

    images['image_3'] = load_image("./build/assets/frame2/image_3.png")
    canvas.create_image(200.0, 650.0, image=images['image_3'])

    images['image_4'] = load_image("./build/assets/frame2/image_4.png")
    canvas.create_image(1200.0, 650.0, image=images['image_4'])

# Digital System Notes (Frame 3)
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
    canvas.create_image(738.0, 161.0, image=images['image_ds'])

    images['image_logo'] = load_image("./build/assets/frame3/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_12.png", lambda: open_pdf("assets\\ds\\ds_1.pdf"), 75, 276, 332, 121),
        ("button_11.png", lambda: open_pdf("assets\\ds\\ds_2.pdf"), 397, 276, 332, 130),
        ("button_10.png", lambda: open_pdf("assets\\ds\\ds_3.pdf"), 719, 276, 332, 121),
        ("button_9.png", lambda: open_pdf("assets\\ds\\ds_4.pdf"), 1051, 276, 322, 121),
        ("button_8.png", lambda: open_pdf("assets\\ds\\ds_5.pdf"), 75, 406, 332, 105),
        ("button_7.png", lambda: open_pdf("assets\\ds\\ds_6.pdf"), 407, 406, 322, 105),
        ("button_6.png", lambda: open_pdf("assets\\ds\\ds_7.pdf"), 729, 406, 312, 105),
        ("button_5.png", lambda: open_pdf("assets\\ds\\ds_8.pdf"), 1051, 406, 314, 105),
        ("button_4.png", lambda: open_pdf("assets\\ds\\ds_9.pdf"), 75, 521, 332, 97),
        ("button_3.png", lambda: open_pdf("assets\\ds\\ds_10.pdf"), 407, 511, 312, 111),
        ("button_2.png", lambda: open_pdf("assets\\ds\\ds_11.pdf"), 719, 511, 332, 111),
        ("button_1.png", lambda: open_pdf("assets\\ds\\ds_12.pdf"), 1051, 521, 312, 104),
        ("button_back.png", show_frame1, 651, 707, 153, 61)
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

    images['image_3'] = load_image("./build/assets/frame3/image_3.png")
    canvas.create_image(156.0, 714.0, image=images['image_3'])

    images['image_4'] = load_image("./build/assets/frame3/image_4.png")
    canvas.create_image(1362.0, 710.0, image=images['image_4'])

# Mathematics Notes (Frame 4)
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

    images['image_mn'] = load_image("./build/assets/frame4/image_mn.png")
    canvas.create_image(737.0, 157.0, image=images['image_mn'])

    images['image_logo'] = load_image("./build/assets/frame4/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_1.png", lambda: open_pdf("assets\\maths\\mt_1.pdf"), 957, 409, 439, 125),
        ("button_2.png", lambda: open_pdf("assets\\maths\\mt_1.pdf"), 518, 407, 439, 125),
        ("button_3.png", lambda: open_pdf("assets\\maths\\mt_1.pdf"), 47, 405, 471, 125),
        ("button_4.png", lambda: open_pdf("assets\\maths\\mt_1.pdf"), 957, 280, 439, 125),
        ("button_5.png", lambda: open_pdf("assets\\maths\\mt_1.pdf"), 518, 278, 439, 125),
        ("button_6.png", lambda: open_pdf("assets\\maths\\mt_1.pdf"), 47, 276, 471, 125),
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

    images['image_3'] = load_image("./build/assets/frame4/image_3.png")
    canvas.create_image(200.0, 650.0, image=images['image_3'])

    images['image_4'] = load_image("./build/assets/frame4/image_4.png")
    canvas.create_image(1200.0, 650.0, image=images['image_4'])

# Frame 5 (Quit)
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

    images['image_a'] = load_image("./build/assets/frame5/image_a.png")
    canvas.create_image(737.0, 215.0, image=images['image_a'])

    images['image_2'] = load_image("./build/assets/frame5/image_2.png")
    canvas.create_image(1260.0, 566.0, image=images['image_2'])

    images['image_logo'] = load_image("./build/assets/frame5/image_logo.png")
    canvas.create_image(737.0, 431.0, image=images['image_logo'])

    images['button_quit'] = load_image("./build/assets/frame5/button_quit.png")
    button_quit = Button(
        image=images['button_quit'],
        borderwidth=0,
        highlightthickness=0,
        command=quit_app,
        relief="flat"
    )
    button_quit.place(x=441.0, y=608.0, width=592.0, height=94.0)

    images['image_4'] = load_image("./build/assets/frame5/image_4.png")
    canvas.create_image(245.0, 583.0, image=images['image_4'])

def quit_app():
    window.destroy()
    
# Quiz Selection Screen
def quiz_selection_screen():
    clear_canvas()
    quiz_frame = tk.Frame(window, bg="#d1eaf0")
    quiz_frame.pack(fill="both", expand=True)
    
    quebiz_section = tk.Label(quiz_frame, text="QUEBIZ SECTION", font=("Comic Sans MS", 40), bg="#d1eaf0")
    quebiz_section.place(x=500, y=51)
    
    physic1 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic1.place(x=94, y=203)
    physic2 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic2.place(x=558, y=203)
    physic3 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic3.place(x=1022, y=203)
    
    digital_system_label = tk.Label(quiz_frame, text="DIGITAL SYSTEM", font=("Arial", 18, "bold"), bg="#ffc8c0", fg="#000")
    digital_system_label.place(x=180, y=222)
    mathematics_label = tk.Label(quiz_frame, text="MATHEMATICS", font=("Arial", 18, "bold"), bg="#ffc8c0", fg="#000")
    mathematics_label.place(x=655, y=222)
    physic_label = tk.Label(quiz_frame, text="PHYSIC", font=("Arial", 18, "bold"), bg="#ffc8c0", fg="#000")
    physic_label.place(x=1150, y=222)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load and debug image paths
    image_paths = {
        'saly_16': os.path.join(current_dir, "Design/Saly-16.png"),
        'saly_10': os.path.join(current_dir, "Design/Saly-10.png"),
        'saly_19': os.path.join(current_dir, "Design/Saly-19.png")
    }
    
    for key, path in image_paths.items():
        if os.path.exists(path):
            print(f"Loading {key} from {path}")
            images[key] = tk.PhotoImage(file=path)
        else:
            print(f"File not found: {path}")
            images[key] = None
    
    # Create labels for each image if the image is loaded
    if images['saly_16']:
        saly_16_label = tk.Label(quiz_frame, image=images['saly_16'], bg="#FFC8C0")
        saly_16_label.place(x=1064, y=260)
    else:
        print("Failed to load saly_16")
    
    if images['saly_10']:
        saly_10_label = tk.Label(quiz_frame, image=images['saly_10'], bg="#FFC8C0")
        saly_10_label.place(x=578, y=272)
    else:
        print("Failed to load saly_10")
    
    if images['saly_19']:
        saly_19_label = tk.Label(quiz_frame, image=images['saly_19'], bg="#FFC8C0")
        saly_19_label.place(x=122, y=260)
    else:
        print("Failed to load saly_19")
    
    button_ds = tk.Button(quiz_frame, text="START", font=("Zen Dots", 12), bg="#d1eaf0", command=open_ds_quiz)
    button_ds.place(x=195, y=635, width=180, height=50)
    
    button_math = tk.Button(quiz_frame, text="START", font=("Zen Dots", 12), bg="#d1eaf0", command=open_math_quiz)
    button_math.place(x=659, y=635, width=180, height=50)
    
    button_physic = tk.Button(quiz_frame, text="START", font=("Zen Dots", 12), bg="#d1eaf0", command=open_physic_quiz)
    button_physic.place(x=1123, y=635, width=180, height=50)
    
    # Back Button to go back to the main menu
    button_back = tk.Button(quiz_frame, text="Back", font=("Arial", 30), bg="#FFC8C0", command=show_frame0)
    button_back.place(x=50, y=50)

def open_ds_quiz():
    questions_ds = [
        {
            "question": "Which of the following is a fundamental building block of digital circuits?",
            "options": ["Resistor", "Transistor", "Diode", "Inductor"],
            "answer": "Transistor"
        },
        {
            "question": "What is the binary representation of the decimal number 10? ",
            "options": ["1010", "1100", "1110", "1001"],
            "answer": "1010"
        },
        {
            "question": "Which logic gate outputs true only when both inputs are true? ",
            "options": ["OR gate", "AND gate", "XOR gate", "NOT gate"],
            "answer": "AND gate"
        },
        {
            "question": "What type of signal is continuous and changes smoothly?",
            "options": ["Digital", "Binary", "Analog", "Discrete"],
            "answer": "Analog"
        },
        {
            "question": "Which is an advantage of digital systems?",
            "options": ["More noise-sensitive", "Higher power consumption", "More compact storage", "Larger hardware size"],
            "answer": "More compact storage"
        },
        {
            "question": "What is the result of the binary addition 110101102 +011110112 ?",
            "options": ["101010012", "101011012", "101000012", "101101002"],
            "answer": "101000012"
        },
        {
            "question": "What is the primary characteristic of combinational logic circuits?  ",
            "options": ["They store data", "They produce outputs solely based on current input values", "They have feedback loops", "They only produce outputs when previous states are considered"],
            "answer": "They produce outputs solely based on current input values"
        },
        {
            "question": "What are the two standard forms of Boolean expressions used in combinational logic?  ",
            "options": ["SOP and NAND", "OR and POS", "SOP and POS", ") AND and NOR"],
            "answer": "SOP and POS"
        },
        {
            "question": "What is the primary purpose of a Karnaugh map (K-map) in digital logic design?  ",
            "options": ["To visualize the output waveform ", "To simulate circuit operation ", "To simplify boolean expressions", "To analyze timing diagrams"],
            "answer": "To simplify boolean expressions"
        },
        {
            "question": "What determines the size of a K-map for a given boolean expression? ",
            "options": ["The number of AND gates in the circuit", "The number of OR gates in the circuit", "The number of input variables", "The number of output variables"],
            "answer": "The number of input variables"
        },
        {
            "question": "What is the significance of gray code labeling in Karnaugh maps?",
            "options": ["It ensures adjacent cells differ by only one variable", "It represents the complement of the input variables", "It simplifies the process of mapping boolean expressions", "It reduces the number of required cells in the map"],
            "answer": "It ensures adjacent cells differ by only one variable"
        },
        {
            "question": "What is the purpose of looping in K-map simplification?  ",
            "options": ["To create complex boolean expressions", "To increase the number of required cells", "To identify adjacent 1s for grouping", "To visualize circuit waveforms"],
            "answer": "To identify adjacent 1s for grouping"
        },
        {
            "question": "What is the primary function of a half-adder?  ",
            "options": ["Adds three binary inputs", "Adds two single-bit binary digits", "Detects specific bit patterns", "Converts BCD to decimal"],
            "answer": "Adds two single-bit binary digits"
        },
        {
            "question": "Which type of adder eliminates ripple delays by anticipating output carry at each stage?",
            "options": ["Half-adder", "Full adder", "Ripple carry adder", "Look-ahead carry adder"],
            "answer": "Look-ahead carry adder"
        },
        {
            "question": "What is the main application of a decoder in digital circuits?",
            "options": ["Addition of multiple-bit binary numbers", "Selecting specific bits in a binary number", "Communicating with external devices", "Detecting specific bit patterns on inputs"],
            "answer": "Detecting specific bit patterns on inputs"
        },
        {
            "question": "How does a full adder differ from a half-adder?  ",
            "options": ["Full adder has three binary inputs and two binary outputs", "Full adder performs addition sequentially", "Full adder eliminates ripple delays", "Full adder has only one binary input and one binary output"],
            "answer": "Full adder has three binary inputs and two binary outputs"
        },
        {
            "question": "What type of decoder is used for converting Binary Coded Decimal (BCD) to decimal?",
            "options": ["4-line-to-16-line decoder", "1-of-10 decoder", "BCD-to-7-segment decoder", "4-bit decoder"],
            "answer": "1-of-10 decoder"
        },
        {
            "question": "What is the primary purpose of a clock signal in digital systems?",
            "options": ["To trigger state changes based on clock transitions", "To generate a periodic rectangular pulse train", "To control the data input to flip-flops", "To prevent invalid states in flip-flops"],
            "answer": "To generate a periodic rectangular pulse train"
        },
        {
            "question": "How do edge-triggered flip-flops differ from latches?",
            "options": ["Latches respond to clock edges, while flip-flops do not", "Latches are bistable devices, while flip-flops are not", "Flip-flops change states only at the clock edge", "Latches change states asynchronously"],
            "answer": "Flip-flops change states only at the clock edge"
        },
        {
            "question": "What determines the exact timing of state changes in synchronous digital systems?",
            "options": ["The inputs to logic gates", "The presence of asynchronous inputs", "The clock signal", "The transitions of the clock pulse"],
            "answer": "The clock signal"
        },
        {
            "question": "How does the J-K flip-flop prevent invalid states?",
            "options": ["By checking the clock input", "By using a D flip-flop instead", "By toggling outputs when both inputs are high", "By using an additional enable input"],
            "answer": "By toggling outputs when both inputs are high"
        },
        {
            "question": "What does the least significant bit (LSB) in a binary counter represent?",
            "options": ["The first stage in the counter", "The second stage in the counter", "The most significant bit", "The carry bit"],
            "answer": "The first stage in the counter"
        },
        {
            "question": "What is another name for an asynchronous counter? ",
            "options": ["Ripple counter", "Toggle counter", "Clock counter", "Sequential counter"],
            "answer": "Ripple counter"
        },
        {
            "question": "What is the main disadvantage of asynchronous counters? ",
            "options": ["They require more flip-flops", "They have accumulated propagation delays", "They cannot be used for high clock rates", "They are not reliable"],
            "answer": "They have accumulated propagation delays"
        },
        {
            "question": "What is the modulus of a 4-bit counter? ",
            "options": ["4", "8", "10", "16"],
            "answer": "16"
        },
        {
            "question": "What is the primary function of a shift register in digital systems? ",
            "options": ["Perform arithmetic operations", "Store and transfer data", "Generate clock pulses", "Filter noise from signals"],
            "answer": "Store and transfer data"
        },
        {
            "question": "Which type of shift register allows data to be entered serially and read out in parallel? ",
            "options": ["Serial-in Serial-out (SISO)", "Parallel-in Parallel-out (PIPO)", "Serial-in Parallel-out (SIPO)", "Parallel-in Serial-out (PISO)"],
            "answer": "Serial-in Parallel-out (SIPO)"
        },
        {
            "question": "How many states does a 4-bit Johnson counter have?",
            "options": ["4", "8", "10", "16"],
            "answer": "8"
        },
        {
            "question": "In a ring counter, how is the output of the last flip-flop fed back?",
            "options": ["To the clock input of the first flip-flop", "To the reset input of the first flip-flop", "To the data input of the first flip-flop", "To the Q' output of the first flip-flop"],
            "answer": "To the data input of the first flip-flop"
        },
        {
            "question": "Which shift register counter is sometimes referred to as a twisted-ring counter?",
            "options": ["Ring counter", "Johnson counter", "Binary counter", "Decade counter "],
            "answer": "Johnson counter"
        }, 
    ]
    clear_canvas()
    app_ds = QuizGame(window, questions_ds)

def open_math_quiz():
    questions_math = [
        {
            "question": "If a1=3a_1 = 3a1 =3 and an=2an−1+5a_n = 2a_{n-1} + 5an =2an−1 +5 for n≥2n \\geq 2n≥2, what is a3a_3a3 ?",
            "options": ["17", "21", "19", "23"],
            "answer": "21"
        },
        {
            "question": "What is 5! (5 factorial)?",
            "options": ["60", "100", "120", "150"],
            "answer": "120"
        },
        {
            "question": "Expand and evaluate the sum ∑i=13 (2i−1)",
            "options": ["6", "9", "12", "15"],
            "answer": "9"
        },
        {
            "question": "Find the ninth term of the arithmetic sequence whose first term is 6 and whose common difference is -5",
            "options": ["-34", "-39", "-41", "-46"],
            "answer": "-34"
        },
        {
            "question": "Find the sum of the first 3 terms of the geometric sequence: 2, -6, 18",
            "options": ["14", "-2", "10", "18"],
            "answer": "14"
        },
        {
            "question": "Which of the following is a system of linear equations?",
            "options": ["x^2+y^2=1", "3x+2y=6 and x-y=4", "y=3x^2+4", "x^3+y=2"],
            "answer": "3x+2y=6 and x-y=4"
        },
        {
            "question": "Which method is used to eliminate one variable by adding or subtracting equations?",
            "options": ["Substitution Method", "Elimination Method", "Graphical Method", "Matrix Method"],
            "answer": "Elimination Method"
        },
        {
            "question": "What is the solution to the system x+y=5 and 2x-y=1 using the substitution method?",
            "options": ["(2,3)", "(3,2)", "(1,4)", "(4,1)"],
            "answer": "(2,3)"
        },
        {
            "question": "How many solutions does a system of linear equations have if the lines are parallel?",
            "options": ["One solution", "Many solution", "Infinitely many solutions", "Cnnot be determined"],
            "answer": "No solution"
        },
        {
            "question": "What is the determinant of the matrix",
            "options": ["10", "11", "8", "14"],
            "answer": "10"
        },
        {
            "question": "Which of the following quantities is a vector?",
            "options": ["Speed", "Mass", "Temperature", "Velocity"],
            "answer": "Velocity"
        },
        {
            "question": "What is the magnitude of the vector v=(3,4)v = (3, 4)v=(3,4) in 2-dimensional space?",
            "options": ["5", "7", "6", "8"],
            "answer": "5"
        },
        {
            "question": "Two vectors are considered equal if they have:",
            "options": ["The same initial point", "The same magnitude and direction, regardless of their initial points ", "The same terminal point", "The same initial and terminal points"],
            "answer": "The same magnitude and direction, regardless of their initial points"
        },
        {
            "question": "If u=(1,2,3) and v=(4,5,6), what is their dot product u.v?",
            "options": ["32", "38", "26", "42"],
            "answer": "32"
        },
        {
            "question": "Which of the following best describes statistics?",
            "options": ["A branch of science that deals with the study of living organisms", " A branch of mathematics concerned with collecting, organizing, summarizing, and analyzing information", "A branch of literature that involves storytelling and poetry.", "A branch of history focusing on ancient civilizations."],
            "answer": " A branch of mathematics concerned with collecting, organizing, summarizing, and analyzing information"
        },
        {
            "question": "What is the main focus of inferential statistics?",
            "options": ["Organizing and summarizing data using tables and graphs", "Making decisions about a population based on sample data.", "Collecting data from all members of a population.", "Describing data using numerical techniques."],
            "answer": "Making decisions about a population based on sample data." 
        },
        {
            "question": "Which of the following is an example of a population?",
            "options": ["The heights of 100 secondary students in Malaysia", "The income taxes collected from 50 companies in Malaysia", "The prices of all houses sold by a developer", "The weights of 14 policemen in a country"],
            "answer": "The prices of all houses sold by a developer"
        },
        {
            "question": "Identify the type of variable: The weight of engineering students",
            "options": ["Qualitative Variable", "Discrete Variable", "Continuous Variable", "Categorical Variable"],
            "answer": "Continuous Variable"
        },
        {
            "question": "Which of the following is an example of a quantitative variable?",
            "options": ["Hair colors", "Types of product produced in a factory", "Height of policemen in a physical test", "Religious affiliation"],
            "answer": "Height of policemen in a physical test"
        },
        {
            "question": "What is the cross product of vectors u=(1,0,0) and v=(0,1,0) in 3-dimensional space?",
            "options": ["(0,0,1)", "(0,0,-1) ", "(1,1,0)", "(1,0,1)"],
            "answer": "(0,0,1)"
        },
        {
            "question": "What is a set?",
            "options": ["A collection of elements arranged in a specific order", "A collection whose members are specified by a list or a rule.", "A single element with no other elements.", "A collection of numbers arranged in ascending order"],
            "answer": "A collection whose members are specified by a list or a rule"
        },
        {
            "question": "Which symbol represents x is an element of a set X?",
            "options": [" x ⊆ X", "x ∈ X ", "x ∉ X", "x ⊂ X"],
            "answer": "x ∈ X "
        },
        {
            "question": "What does the union of two sets A and B represent?",
            "options": ["The intersection of set A and set B", "The combination of all elements in set A and set B. ", "The set of elements common to both set A and set B.", "The set of elements that are in either set A or set B or both."],
            "answer": "The set of elements that are in either set A or set B or both."
        },
        {
            "question": "If A = {2, 4, 6} and B = {3, 6, 9}, what is A ∩ B?",
            "options": ["{2, 3, 4, 6, 9}", "{ } (empty set)", "{6}", "{2, 4}"],
            "answer": "{6}"
        },
        {
            "question": "What is the complement of set A, denoted as A'?",
            "options": ["The set of all elements in A.", "The set of all elements not in set A.", "The set of elements common to set A and its complement.", "The set of elements in set A and its complement"],
            "answer": "The set of all elements not in set A."
        },
        {
            "question": "For a binomial distribution with parameters n=10 and p=0.5p = 0.5p=0.5, what is the mean (μ) of the distribution?",
            "options": ["2.5", "5", "7.5", "10"],
            "answer": "5"
        },
        {
            "question": "For a standard normal distribution, what is the Z-score corresponding to the 95th percentile?",
            "options": ["1.28", "1.65", "1.96", "2.33"],
            "answer": "1.96"
        },
        {
            "question": "In a binomial distribution with n=5 and p=0.2, what is the standard deviation (σ)?",
            "options": ["0.4", "0.8", "1", "1.2"],
            "answer": "0.8"
        },
        {
            "question": "Which of the following is true for a normal distribution curve?",
            "options": ["The total area under the curve is less than 1.", "The curve is skewed to the right. ", "The mean, median, and mode are all equal.", "The curve has a single peak at x=σ."],
            "answer": "The mean, median, and mode are all equal."
        },
        {
            "question": "In a normal distribution with mean μ=50 and standard deviation σ=5, what is the z-score corresponding to X=60?",
            "options": ["1", "2", "8", "10"],
            "answer": "2"
        },    
    ]
    clear_canvas()
    app_math = QuizGame(window, questions_math)

def open_physic_quiz():
    questions_physic = questions_physic = [
        {
            "question": "Which of the following statements best describes the importance of understanding physics in the field of information technology?",
            "options": ["Physics is not relevant to information technology.", "Physics helps in understanding the economic aspects of IT. ", "Understanding physics is crucial for improving and operating electronic devices in IT.", " Physics only deals with theoretical concepts and not practical applications in IT."],
            "answer": "Understanding physics is crucial for improving and operating electronic devices in IT."
        },
        {
            "question": "What is an example of an application where physics knowledge is crucial in IT? ",
            "options": ["Designing user-friendly software interfaces.", "Creating marketing strategies for IT products.", "Applying relativistic corrections in GPS receivers.", "Writing documentation for IT systems."],
            "answer": "Applying relativistic corrections in GPS receivers."
        },
        {
            "question": "Which SI base unit is correctly matched with its quantity? ",
            "options": ["Length - kilogram (kg)", "Mass - meter (m) ", "Time - second (s)", "Electric current - candela (cd)"],
            "answer": "Time - second (s)"
        },
        {
            "question": "Which of the following is a derived unit? ",
            "options": ["Kelvin (K)", "Candela (cd)", "Newton (N) ", "Mole (mol)"],
            "answer": "Newton (N) "
        },
        {
            "question": "How would you express 2.9 × 10^-6 Hz using a standard prefix? ",
            "options": ["2.9 GHz", "2.9 MHz", "2.9 µHz", "2.9 pHz"],
            "answer": "2.9 µHz"
        },
        {
            "question": "Which of the following types of motion involves an object moving in a straight line? ",
            "options": ["Translational motion ", "Rotational motion", "Vibrational motion", "Circular motion"],
            "answer": "Translational motion "
        },
        {
            "question": "What is the primary difference between distance and displacement? ",
            "options": ["Distance measures the direction of motion, while displacement measures the time taken.", "Distance is a scalar quantity, while displacement is a vector quantity.", "Distance measures the shortest path between two points, while displacement measures the total ground covered.", "Distance and displacement are two names for the same concept."],
            "answer": "Distance is a scalar quantity, while displacement is a vector quantity."
        },
        {
            "question": "What is the SI unit for speed? ",
            "options": ["km/h", "m/s", "mph", "cm/s"],
            "answer": "m/s"
        },
        {
            "question": "How is acceleration defined in physics? ",
            "options": ["The change in position over time.", "The rate at which an object changes its speed.", "The rate at which an object changes its velocity.", "The distance covered per unit time."],
            "answer": "The rate at which an object changes its velocity."
        },
        {
            "question": "What does the slope of a position versus time graph represent? ",
            "options": ["Acceleration", "Displacement", "Speed", "Velocity"],
            "answer": "Velocity"
        },
        {
            "question": "Which of the following statements about force is correct? ",
            "options": ["Force is a scalar quantity because it has only magnitude.", "Force is the cause of acceleration and is a vector quantity because it has both magnitude and direction.", "Force can be described as a state of rest or uniform motion in a straight line.", "Force is measured in kilograms (kg)."],
            "answer": "Force is the cause of acceleration and is a vector quantity because it has both magnitude and direction."
        },
        {
            "question": "What condition must be met for an object to accelerate? ",
            "options": ["The net force acting on the object must be zero.", "The net force acting on the object must be greater than zero", "The object must be at rest.", " The object must be moving with constant velocity."],
            "answer": "The net force acting on the object must be greater than zero"
        },
        {
            "question": "According to Newton’s first law, if the net force on an object is zero, which of the following statements is true?",
            "options": ["The object will move with a constant acceleration.", "The object will eventually come to rest.", "The object’s velocity will remain constant, and its acceleration will be zero.", "The object will experience a change in velocity."],
            "answer": "The object’s velocity will remain constant, and its acceleration will be zero."
        },
        {
            "question": "Which equation represents Newton's second law of motion? ",
            "options": ["F=ma", "F=am ", "F=mv", "F=mv"],
            "answer": "F=ma"
        },
        {
            "question": "What does Newton's third law of motion state? ",
            "options": ["An object in motion will remain in motion unless acted upon by a net force", "The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass.", "For every action, there is an equal and opposite reaction.", "The total momentum of an isolated system remains constant. "],
            "answer": "For every action, there is an equal and opposite reaction."
        },
        {
            "question": "Which of the following statements about periodic motion is true?  ",
            "options": ["An object's motion is referred to as periodic motion when it repeats itself repeatedly. ", "When the motion comes exactly back to its original state, we say that the object has gone through a complete cycle or complete oscillation.", "The amount of time it takes for one complete cycle to occur is called the period T of the motion. ", "While the period is one way to characterize the speed for the periodic motion, another way is through the frequency "],
            "answer": "The amount of time it takes for one complete cycle to occur is called the period T of the motion. "
        },
        {
            "question": "In simple harmonic motion, what is the restoring force proportional to?  ",
            "options": ["Mass ", "Displacement", "Velocity", "Acceleration"],
            "answer": "Displacement"
        },
        {
            "question": "What is the relationship between the period and frequency of an oscillating system?",
            "options": ["They are directly proportional.", "They are inversely proportional.", "They are equal", "They are not related."],
            "answer": "They are inversely proportional."
        },
        {
            "question": "What factor does the period of a simple pendulum depend on?  ",
            "options": ["Mass of the pendulum", "Length of the string and value of gravity ", "Amplitude of the oscillation ", "Damping coefficient "],
            "answer": "Length of the string and value of gravity "
        },
        {
            "question": "What type of oscillations occur when the damping is so large that the motion no longer resembles simple harmonic motion?",
            "options": ["Under-damped ", "Critically damped", "Over-damped ", "Driven oscillations"],
            "answer": "Over-damped"
        },
        {
            "question": "What type of wave requires a material medium for propagation?  ",
            "options": ["Mechanical wave  ", "Electromagnetic wave ", "Longitudinal wave", "Transverse wave"],
            "answer": "Mechanical wave  "
        },
        {
            "question": "Which principle states that the total displacement at any point due to two or more travelling waves is equal to the vector sum of their individual displacements at that point?  ",
            "options": ["Superposition principle ", " Interference principle", "Reflection principle", "Refraction principle"],
            "answer": "Superposition principle "
        },
        {
            "question": "What principle accurately describes the particle motion in a transverse wave?  ",
            "options": ["Motion parallel to the direction of wave velocity", "Motion perpendicular to the direction of wave velocity ", "Motion in the same direction as the wave velocity ", "Motion in the opposite direction to the wave velocity "],
            "answer": "Motion perpendicular to the direction of wave velocity "
        },
        {
            "question": "What is the wave function for a sinusoidal wave given by equation (8)?",
            "options": ["Y = A Sin (kx - ωt)", "Y = A Sin (kx + ωt) ", "Y = A Cos (kx - ωt) ", "Y = A Cos (kx + ωt)"],
            "answer": "Y = A Sin (kx - ωt)"
        },
        {
            "question": "What defines periodic motion in physics?",
            "options": ["Motion that eventually comes to a stop", "Motion that occurs randomly", "Motion that repeats itself over and over again", "Motion that follows a linear path"],
            "answer": "Motion that repeats itself over and over again"
        },
        {
            "question": "What is the SI unit of frequency?",
            "options": ["Seconds (s)", "Meters per second", "Inverse second", "Newton"],
            "answer": "Inverse second"
        },
        {
            "question": "According to Hooke's Law, what is the restoring force exerted by a spring when a mass is displaced by a distance x?",
            "options": ["F=kx", "F=−kx", "F=k/x", "F=-k/x"],
            "answer": "F=−kx"
        },
        {
            "question": "For small angle oscillations, the period of a simple pendulum depends on which factors?",
            "options": ["Mass of the pendulum bob and acceleration due to gravity", "Length of the string and mass of the pendulum bob", "Length of the string and acceleration due to gravity", "Angle of displacement and length of the string"],
            "answer": "Length of the string and acceleration due to gravity"
        },
        {
            "question": "What is the behavior of a critically damped oscillatory system?",
            "options": ["The system oscillates with decreasing amplitude", "The system oscillates with increasing amplitude", "The system returns to equilibrium without oscillating", "The system returns to equilibrium without oscillating"],
            "answer": "The system returns to equilibrium without oscillating"
        },  
        {
            "question": "What type of motion does a mass attached to a spring exhibit when displaced from its equilibrium position and then released?",
            "options": ["Uniform linear motion", "Circular motion", "Simple harmonic motion (SHM)", "Random motion"],
            "answer": "Simple harmonic motion (SHM)"
        },
    ]
    clear_canvas()
    app_physic = QuizGame(window, questions_physic)

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

# Start the application
show_frame0()
window.mainloop()

                                  

