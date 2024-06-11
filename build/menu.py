
import datetime
import pytz
from tkinter import Tk, Canvas, Button, PhotoImage, Label

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
        image = PhotoImage(file=image_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {image_path}: {e}")
        return None

# Frame 0 (Main menu)
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

    dt_mst = datetime.datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur'))
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
        command=lambda: print("button_rq clicked"),
        relief="flat"
    )
    button_rq.place(x=65.0, y=284.0, width=440.0, height=473.0)

# Frame 1 (Lecture Notes)
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

# Frame 2 (Physics)
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
        ("button_1.png", lambda: print("button_1 clicked"), 72, 291, 446, 112),
        ("button_2.png", lambda: print("button_2 clicked"), 518, 278, 439, 125),
        ("button_3.png", lambda: print("button_3 clicked"), 957, 280, 439, 125),
        ("button_4.png", lambda: print("button_4 clicked"), 518, 546, 439, 125),
        ("button_5.png", lambda: print("button_5 clicked"), 80, 405, 427, 125),
        ("button_6.png", lambda: print("button_6 clicked"), 518, 407, 439, 125),
        ("button_7.png", lambda: print("button_7 clicked"), 957, 409, 439, 125),
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

# Frame 3 (Digital System)
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
        ("button_12.png", lambda: print("c_1 clicked"), 75, 276, 332, 121),
        ("button_11.png", lambda: print("c_2 clicked"), 397, 276, 332, 130),
        ("button_10.png", lambda: print("c_3 clicked"), 719, 276, 332, 121),
        ("button_9.png", lambda: print("c_4 clicked"), 1051, 276, 322, 121),
        ("button_8.png", lambda: print("c_5 clicked"), 75, 406, 332, 105),
        ("button_7.png", lambda: print("c_6 clicked"), 407, 406, 322, 105),
        ("button_6.png", lambda: print("c_7 clicked"), 729, 406, 312, 105),
        ("button_5.png", lambda: print("c_8 clicked"), 1051, 406, 314, 105),
        ("button_4.png", lambda: print("c_9 clicked"), 75, 521, 332, 97),
        ("button_3.png", lambda: print("c_10 clicked"), 407, 511, 312, 111),
        ("button_2.png", lambda: print("c_11 clicked"), 719, 511, 332, 111),
        ("button_1.png", lambda: print("c_12 clicked"), 1051, 521, 312, 104),
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

# Frame 4 (Mathematics)
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
        ("button_1.png", lambda: print("c_6 clicked"), 957, 409, 439, 125),
        ("button_2.png", lambda: print("c_5 clicked"), 518, 407, 439, 125),
        ("button_3.png", lambda: print("c_4 clicked"), 47, 405, 471, 125),
        ("button_4.png", lambda: print("c_3 clicked"), 957, 280, 439, 125),
        ("button_5.png", lambda: print("c_2 clicked"), 518, 278, 439, 125),
        ("button_6.png", lambda: print("c_1 clicked"), 47, 276, 471, 125),
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

# Function to quit the application
def quit_app():
    window.destroy()

# Initial call to show the main frame
show_frame0()

# Run the Tkinter main loop
window.mainloop()