# Import necessary libraries
import datetime
from tkinter import Tk, Canvas, Button, PhotoImage, Label, messagebox, font, Frame, Entry, Toplevel
import sys
import os
import subprocess
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
    canvas.create_image(72.0, 291.0, image=images['image_3'])

# Data Structures (Frame 3)
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
    canvas.create_image(742.0, 153.0, image=images['image_ds'])

    images['image_logo'] = load_image("./build/assets/frame3/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_1.png", lambda: open_pdf("assets\\datastruct\\dsn_1.pdf"), 72, 291, 446, 112),
        ("button_2.png", lambda: open_pdf("assets\\datastruct\\dsn_2.pdf"), 518, 278, 439, 125),
        ("button_3.png", lambda: open_pdf("assets\\datastruct\\dsn_3.pdf"), 957, 280, 439, 125),
        ("button_4.png", lambda: open_pdf("assets\\datastruct\\dsn_4.pdf"), 518, 546, 439, 125),
        ("button_5.png", lambda: open_pdf("assets\\datastruct\\dsn_5.pdf"), 80, 405, 427, 125),
        ("button_6.png", lambda: open_pdf("assets\\datastruct\\dsn_6.pdf"), 518, 407, 439, 125),
        ("button_7.png", lambda: open_pdf("assets\\datastruct\\dsn_7.pdf"), 957, 409, 439, 125),
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
    canvas.create_image(72.0, 291.0, image=images['image_3'])

# Maths Notes (Frame 4)
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
    canvas.create_image(742.0, 153.0, image=images['image_maths'])

    images['image_logo'] = load_image("./build/assets/frame4/image_logo.png")
    canvas.create_image(47.0, 42.0, image=images['image_logo'])

    buttons = [
        ("button_1.png", lambda: open_pdf("assets\\maths\\mthn_1.pdf"), 72, 291, 446, 112),
        ("button_2.png", lambda: open_pdf("assets\\maths\\mthn_2.pdf"), 518, 278, 439, 125),
        ("button_3.png", lambda: open_pdf("assets\\maths\\mthn_3.pdf"), 957, 280, 439, 125),
        ("button_4.png", lambda: open_pdf("assets\\maths\\mthn_4.pdf"), 518, 546, 439, 125),
        ("button_5.png", lambda: open_pdf("assets\\maths\\mthn_5.pdf"), 80, 405, 427, 125),
        ("button_6.png", lambda: open_pdf("assets\\maths\\mthn_6.pdf"), 518, 407, 439, 125),
        ("button_7.png", lambda: open_pdf("assets\\maths\\mthn_7.pdf"), 957, 409, 439, 125),
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
    canvas.create_image(72.0, 291.0, image=images['image_3'])

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
    canvas.create_image(737.0, 401.0, image=images['image_signout'])

    def confirm_signout():
        print("Signout confirmed")
        show_frame0()  # Return to main menu after sign out confirmation

    def cancel_signout():
        print("Signout cancelled")
        show_frame0()  # Return to main menu

    images['button_confirm'] = load_image("./build/assets/frame5/button_confirm.png")
    button_confirm = Button(
        image=images['button_confirm'],
        borderwidth=0,
        highlightthickness=0,
        command=confirm_signout,
        relief="flat"
    )
    button_confirm.place(x=518, y=548, width=151, height=51)

    images['button_cancel'] = load_image("./build/assets/frame5/button_cancel.png")
    button_cancel = Button(
        image=images['button_cancel'],
        borderwidth=0,
        highlightthickness=0,
        command=cancel_signout,
        relief="flat"
    )
    button_cancel.place(x=806, y=548, width=151, height=51)

# Quiz Selection Screen
def quiz_selection_screen():
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

    images['image_quiz'] = load_image("./build/assets/quiz_selection/image_quiz.png")
    canvas.create_image(737.0, 401.0, image=images['image_quiz'])

    quiz_buttons = [
        ("button_phy.png", lambda: start_quiz("Physics"), 72, 291, 446, 112),
        ("button_ds.png", lambda: start_quiz("Data Structures"), 518, 278, 439, 125),
        ("button_maths.png", lambda: start_quiz("Maths"), 957, 280, 439, 125),
        ("button_back.png", show_frame0, 651, 707, 153, 61)
    ]

    for btn_img, btn_cmd, x, y, w, h in quiz_buttons:
        images[btn_img] = load_image(f"./build/assets/quiz_selection/{btn_img}")
        button = Button(
            image=images[btn_img],
            borderwidth=0,
            highlightthickness=0,
            command=btn_cmd,
            relief="flat"
        )
        button.place(x=x, y=y, width=w, height=h)

def start_quiz(subject):
    print(f"Starting quiz for {subject}")
    # Quiz logic here

show_frame0()
window.mainloop()
