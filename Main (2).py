import datetime
from tkinter import Tk, Canvas, Button, PhotoImage, Label, messagebox, font, Frame, Entry, Toplevel, Text
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
root.title('Quebiz')
root.geometry('1474x801')  # Adjusted geometry to match second code
root.configure(bg="#ffc0db")


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



#CODE

def open_pdf(file_path):
    try:
        abs_path = os.path.abspath(file_path)
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
            messagebox.showerror("Error", f"Failed to open {file_path}: File not found")
    except Exception as e:
        print(f"Failed to open {file_path}: {e}")
        messagebox.showerror("Error", f"Failed to open {file_path}: {e}")

# Global Tkinter window
window = Tk()
window.title('Quebiz')
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
    relief="flat",
    command=window.destroy  #destroy the window and go to new window (flashcard)
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
        ("button_1.png", lambda: open_pdf("build/assets/physics/phyn_1.pdf"), 72, 291, 446, 112),
        ("button_2.png", lambda: open_pdf("build/assets/physics/phyn_2.pdf"), 518, 278, 439, 125),
        ("button_3.png", lambda: open_pdf("build/assets/physics/phyn_3.pdf"), 957, 280, 439, 125),
        ("button_4.png", lambda: open_pdf("build/assets/physics/phyn_4.pdf"), 518, 546, 439, 125),
        ("button_5.png", lambda: open_pdf("build/assets/physics/phyn_5.pdf"), 80, 405, 427, 125),
        ("button_6.png", lambda: open_pdf("build/assets/physics/phyn_6.pdf"), 518, 407, 439, 125),
        ("button_7.png", lambda: open_pdf("build/assets/physics/phyn_7.pdf"), 957, 409, 439, 125),
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
        ("button_12.png", lambda: open_pdf("build/assets/ds/ds_1.pdf"), 75, 276, 332, 121),
        ("button_11.png", lambda: open_pdf("build/assets/ds/ds_2.pdf"), 397, 276, 332, 130),
        ("button_10.png", lambda: open_pdf("build/assets/ds/ds_3.pdf"), 719, 276, 332, 121),
        ("button_9.png", lambda: open_pdf("build/assets/ds/ds_4.pdf"), 1051, 276, 322, 121),
        ("button_8.png", lambda: open_pdf("build/assets/ds/ds_5.pdf"), 75, 406, 332, 105),
        ("button_7.png", lambda: open_pdf("build/assets/ds/ds_6.pdf"), 407, 406, 322, 105),
        ("button_6.png", lambda: open_pdf("build/assets/ds/ds_7.pdf"), 729, 406, 312, 105),
        ("button_5.png", lambda: open_pdf("build/assets/ds/ds_8.pdf"), 1051, 406, 314, 105),
        ("button_4.png", lambda: open_pdf("build/assets/ds/ds_9.pdf"), 75, 521, 332, 97),
        ("button_3.png", lambda: open_pdf("build/assets/ds/ds_10.pdf"), 407, 511, 312, 111),
        ("button_2.png", lambda: open_pdf("build/assets/ds/ds_11.pdf"), 719, 511, 332, 111),
        ("button_1.png", lambda: open_pdf("build/assets/ds/ds_12.pdf"), 1051, 521, 312, 104),
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
        ("button_1.png", lambda: open_pdf("build/assets/maths/mt_1.pdf"), 957, 409, 439, 125),
        ("button_2.png", lambda: open_pdf("build/assets/maths/mt_2.pdf"), 518, 407, 439, 125),
        ("button_3.png", lambda: open_pdf("build/assets/maths/mt_3.pdf"), 47, 405, 471, 125),
        ("button_4.png", lambda: open_pdf("build/assets/maths/mt_4.pdf"), 957, 280, 439, 125),
        ("button_5.png", lambda: open_pdf("build/assets/maths/mt_5.pdf"), 518, 278, 439, 125),
        ("button_6.png", lambda: open_pdf("build/assets/maths/mt_6.pdf"), 47, 276, 471, 125),
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
    ]
    clear_canvas()
    app_math = QuizGame(window, questions_math)


def open_physic_quiz():
    questions_physic = [
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


current_question_index = 0 


# Start the application
show_frame0()
window.resizable(True, True)
window.mainloop()

import os
from tkinter import Tk, Canvas, Button, Text, Frame, PhotoImage

def load_image(image_path):
    try:
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None

def switch_frame(to_frame):
    for frame in frames:
        frame.pack_forget()
    to_frame.pack(fill="both", expand=True)

def gui0():
    # Clear previous widgets if any
    for widget in main_menu_frame.winfo_children():
        widget.destroy()

    # Create GUI0 content
    canvas_main = Canvas(main_menu_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
    canvas_main.place(x=0, y=0)

    images = {}
    images['button_fc'] = load_image("./build/assets/frame0/button_fc.png")
    button_fc = Button(main_menu_frame, image=images['button_fc'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui0))
    button_fc.place(x=974.0, y=298.0, width=425.0, height=432.0)

    canvas_main.create_text(282.0, 71.0, anchor="nw", text="Your New GUI0", fill="#000000", font=("Inter Bold", 64 * -1))

# Initialize the main window
root = Tk()
root.geometry("1474x801")
root.configure(bg="#D0F0C0")

# Initialize frames
main_menu_frame = Frame(root, bg="#D0F0C0")
gui1_frame = Frame(root, bg="#D1EAF0")
gui2_frame = Frame(root, bg="#D0F0C0")
gui3_frame = Frame(root, bg="#D0F0C0")
frames = [main_menu_frame, gui1_frame, gui2_frame, gui3_frame]

# Main menu content (GUI0)
canvas_main = Canvas(main_menu_frame, bg="#D1EAF0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_main.place(x=0, y=0)

images = {}
images['button_image_1'] = load_image("./build/assets/nqa1/button_1.png")  #back button
button_main_1 = Button(main_menu_frame, image=images['button_image_1'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(show_frame0))
button_main_1.place(x=687.0, y=701.0, width=153.0, height=61.0)

images['button_image_2'] = load_image("./build/assets/nqa1/button_2.png")  #ds button
button_main_2 = Button(main_menu_frame, image=images['button_image_2'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui3_frame))
button_main_2.place(x=541.797, y=181.0, width=416.202, height=514.0)

images['button_image_3'] = load_image("./build/assets/nqa1/button_3.png")  #physic button
button_main_3 = Button(main_menu_frame, image=images['button_image_3'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui1_frame))
button_main_3.place(x=84.816, y=179.0, width=416.183, height=522.0)

images['button_image_4'] = load_image("./build/assets/nqa1/button_4.png")  #math button
button_main_4 = Button(main_menu_frame, image=images['button_image_4'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui2_frame))
button_main_4.place(x=1004.912, y=179.0, width=416.087, height=505.0)

canvas_main.create_text(282.0, 71.0, anchor="nw", text="Choose your selective subject !", fill="#000000", font=("Inter Bold", 64 * -1))

images['image_image_1'] = load_image("./build/assets/nqa1/image_1.png")  #quebiz logo
canvas_main.create_image(91.0, 81.0, image=images['image_image_1'])

# GUI3 content 
canvas_gui3 = Canvas(gui3_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_gui3.place(x=0, y=0)

button_image_gui3_1 = load_image("./build/assets/nqa3/button_1.png")  #white
button_gui3_1 = Button(gui3_frame, image=button_image_gui3_1, borderwidth=0, highlightthickness=0, relief="flat")
button_gui3_1.place(x=260.0, y=111.0, width=931.929, height=532.299)

questions_ds_gui3 = [
    {"question": "Which of the following statements best describes the importance of understanding physics in the field of information technology?", "answer": "Understanding physics is crucial for improving and operating electronic devices in IT"},
    {"question": "Which SI base unit is correctly matched with its quantity?", "answer": "Time - second (s)"},
    {"question": "Which of the following is a derived unit?", "answer": "Newton (N)"},
    {"question": "How would you express 2.9 × 10^-6 Hz using a standard prefix? ", "answer": "2.9 µHz"},
    {"question": "Which of the following types of motion involves an object moving in a straight line?", "answer": "Translational motion"},
    {"question": "What is the primary difference between distance and displacement?", "answer": "Distance is a scalar quantity, while displacement is a vector quantity"},
    {"question": "What is the SI unit for speed?", "answer": "m/s"},
    {"question": "How is acceleration defined in physics?", "answer": "The rate at which an object changes its velocity."},
    {"question": "What does the slope of a position versus time graph represent?", "answer": "Velocity"},
    {"question": "Which of the following statements about force is correct?", "answer": "Force is the cause of acceleration and is a vector quantity because it has both magnitude and direction."},
]

current_question_index_gui3 = 0

text_widget_gui3 = Text(button_gui3_1, wrap="word", relief="flat", bd=0, highlightthickness=0, font=("Inter Regular", 16), spacing1=5, spacing2=2)
text_widget_gui3.pack(expand=True, fill="both")
text_widget_gui3.insert("end", questions_ds_gui3[current_question_index_gui3]["question"] + "\n" + questions_ds_gui3[current_question_index_gui3]["answer"])
text_widget_gui3.config(state="disabled")

def next_question_gui3():
    global current_question_index_gui3
    current_question_index_gui3 = (current_question_index_gui3 + 1) % len(questions_ds_gui3)
    update_question_gui3()

def update_question_gui3():
    text_widget_gui3.config(state="normal")
    text_widget_gui3.delete(1.0, "end")
    question = questions_ds_gui3[current_question_index_gui3]["question"]
    answer = questions_ds_gui3[current_question_index_gui3]["answer"]
    text_widget_gui3.insert("end", f" {question}\n\n {answer}\n\n")
    text_widget_gui3.config(state="disabled")

button_image_gui3_2 = load_image("build/assets/nqa2/nqa3/button_3.png")
button_gui3_2 = Button(gui3_frame, image=button_image_gui3_2, borderwidth=0, highlightthickness=0, relief="flat", command=next_question_gui3)
button_gui3_2.place(x=928.0, y=688.0, width=153.0, height=61.0)

button_image_gui3_3 = load_image("build/assets/nqa2/nqa3/button_5.png")
button_gui3_3 = Button(gui3_frame, image=button_image_gui3_3, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(main_menu_frame))
button_gui3_3.place(x=322.0, y=688.0, width=243.0, height=61.0)

canvas_gui3.create_text(660.0, 358.0, anchor="nw", text="Questions", fill="#000000", font=("Inter SemiBold", 30 * -1))
canvas_gui3.create_text(580.0, 16.0, anchor="nw", text="Digital System", fill="#000000", font=("Inter Bold", 64 * -1))

image_gui3_2 = load_image("./build/assets/nqa3/image_2.png")
canvas_gui3.create_image(81.0, 81.0, image=image_gui3_2)

# GUI2 content
canvas_gui2 = Canvas(gui2_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_gui2.place(x=0, y=0)

button_image_gui2_1 = load_image("./build/assets/nqa3/button_1.png")
button_gui2_1 = Button(gui2_frame, image=button_image_gui2_1, borderwidth=0, highlightthickness=0, relief="flat")
button_gui2_1.place(x=260.0, y=111.0, width=931.929, height=532.299)

questions_ds_gui2 = [
    {"question": "What is 5! (5 factorial)?", "answer": "120"},
    {"question": "Expand and evaluate the sum ∑i=13 (2i−1)", "answer": "9"},
    {"question": "Find the ninth term of the arithmetic sequence whose first term is 6 and whose common difference is -5", "answer": "-34"},
    {"question": "Find the sum of the first 3 terms of the geometric sequence: 2, -6, 18", "answer": "14"},
    {"question": "Which of the following is a system of linear equations?", "answer": "3x+2y=6 and x-y=4"},
    {"question": "Which method is used to eliminate one variable by adding or subtracting equations?", "answer": "Elimination Method"},
    {"question": "What is the solution to the system x+y=5 and 2x-y=1 using the substitution method?", "answer": "(2,3)"},
    {"question": "How many solutions does a system of linear equations have if the lines are parallel?", "answer": "No solution"},
    {"question": "What is the determinant of the matrix", "answer": "10"},
    {"question": "Which of the following quantities is a vector?", "answer": "Velocity"},
]

current_question_index_gui2 = 0

text_widget_gui2 = Text(button_gui2_1, wrap="word", relief="flat", bd=0, highlightthickness=0, font=("Inter Regular", 16), spacing1=5, spacing2=2)
text_widget_gui2.pack(expand=True, fill="both")
text_widget_gui2.insert("end", questions_ds_gui2[current_question_index_gui2]["question"] + "\n" + questions_ds_gui2[current_question_index_gui2]["answer"])
text_widget_gui2.config(state="disabled")

def next_question_gui2():
    global current_question_index_gui2
    current_question_index_gui2 = (current_question_index_gui2 + 1) % len(questions_ds_gui2)
    update_question_gui2()

def update_question_gui2():
    text_widget_gui2.config(state="normal")
    text_widget_gui2.delete(1.0, "end")
    question = questions_ds_gui2[current_question_index_gui2]["question"]
    answer = questions_ds_gui2[current_question_index_gui2]["answer"]
    text_widget_gui2.insert("end", f" {question}\n\n {answer}\n\n")
    text_widget_gui2.config(state="disabled")

button_image_gui2_2 = load_image("build/assets/nqa2/nqa3/button_3.png")
button_gui2_2 = Button(gui2_frame, image=button_image_gui2_2, borderwidth=0, highlightthickness=0, relief="flat", command=next_question_gui2)
button_gui2_2.place(x=928.0, y=688.0, width=153.0, height=61.0)

button_image_gui2_3 = load_image("build/assets/nqa2/nqa3/button_5.png")
button_gui2_3 = Button(gui2_frame, image=button_image_gui2_3, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(main_menu_frame))
button_gui2_3.place(x=322.0, y=688.0, width=243.0, height=61.0)

canvas_gui2.create_text(660.0, 358.0, anchor="nw", text="Questions", fill="#000000", font=("Inter SemiBold", 30 * -1))
canvas_gui2.create_text(580.0, 16.0, anchor="nw", text="Digital System", fill="#000000", font=("Inter Bold", 64 * -1))

image_gui2_2 = load_image("./build/assets/nqa3/image_2.png")
canvas_gui2.create_image(81.0, 81.0, image=image_gui2_2)


# GUI1 content
canvas_gui1 = Canvas(gui1_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_gui1.place(x=0, y=0)

button_image_gui1_1 = load_image("./build/assets/nqa3/button_1.png")    #screen putih question
button_gui1_1 = Button(gui1_frame, image=button_image_gui1_1, borderwidth=0, highlightthickness=0, relief="flat")
button_gui1_1.place(x=260.0, y=111.0, width=931.929, height=532.299)

questions_ds_gui1 = [
    {"question": "Which of the following is a fundamental building block of digital circuits?", "answer": "Transistor"},
    {"question": "What is the binary representation of the decimal number 10?", "answer": "1010"},
    {"question": "Which logic gate outputs true only when both inputs are true?", "answer": "AND Gate"},
    {"question": "What type of signal is continuous and changes smoothly?", "answer": "Analog"},
    {"question": "Which is an advantage of digital systems?", "answer": "More compact storage"},
    {"question": "What is the result of the binary addition 110101102 +011110112 ?", "answer": "101000012"},
    {"question": "What is the primary characteristic of combinational logic circuits?", "answer": "They produce outputs solely based on current input values"},
    {"question": "What are the two standard forms of Boolean expressions used in combinational logic?", "answer": "SOP and POS"},
    {"question": "What is the primary purpose of a Karnaugh map (K-map) in digital logic design?", "answer": "To simplify boolean expressions"},
    {"question": "What determines the size of a K-map for a given boolean expression?", "answer": "The number of input variables"},
]

current_question_index_gui1 = 0

text_widget_gui1 = Text(button_gui1_1, wrap="word", relief="flat", bd=0, highlightthickness=0, font=("Inter Regular", 16), spacing1=5, spacing2=2)
text_widget_gui1.pack(expand=True, fill="both")
text_widget_gui1.insert("end", questions_ds_gui1[current_question_index_gui1]["question"] + "\n" + questions_ds_gui1[current_question_index_gui1]["answer"])
text_widget_gui1.config(state="disabled")

def next_question_gui1():
    global current_question_index_gui1
    current_question_index_gui1 = (current_question_index_gui1 + 1) % len(questions_ds_gui1)
    update_question_gui1()

def update_question_gui1():
    text_widget_gui1.config(state="normal")
    text_widget_gui1.delete(1.0, "end")
    question = questions_ds_gui1[current_question_index_gui1]["question"]
    answer = questions_ds_gui1[current_question_index_gui1]["answer"]
    text_widget_gui1.insert("end", f" {question}\n\n {answer}\n\n")
    text_widget_gui1.config(state="disabled")

button_image_gui1_2 = load_image("build/assets/nqa2/nqa3/button_3.png")   #button next
button_gui1_2 = Button(gui1_frame, image=button_image_gui1_2, borderwidth=0, highlightthickness=0, relief="flat", command=next_question_gui1)
button_gui1_2.place(x=928.0, y=688.0, width=153.0, height=61.0)

button_image_gui1_3 = load_image("build/assets/nqa2/nqa3/button_5.png")   #button main menu
button_gui1_3 = Button(gui1_frame, image=button_image_gui1_3, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(main_menu_frame))
button_gui1_3.place(x=322, y=688.0, width=243.0, height=61.0)

canvas_gui1.create_text(660.0, 358.0, anchor="nw", text="Questions", fill="#000000", font=("Inter SemiBold", 30 * -1))
canvas_gui1.create_text(580.0, 16.0, anchor="nw", text="Digital System", fill="#000000", font=("Inter Bold", 64 * -1))

image_gui1_2 = load_image("./build/assets/nqa3/image_2.png")
canvas_gui1.create_image(81.0, 81.0, image=image_gui1_2)

# Switch to the main menu frame initially
switch_frame(main_menu_frame)

# Main loop
root.mainloop()                                   

