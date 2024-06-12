
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from gui2 import launch_gui2  # Import the function
from gui1 import launch_gui1 
from gui3 import launch_gui3  


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\TT8L-09\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1474x801")
window.configure(bg = "#D1EAF0")
window.title("Quebizz")
    
def switch_to_gui2():
    print("Switching to Maths..")
    window.withdraw()  # Hide the current GUI
    launch_gui2()  # Call the function to launch the second GUI
    print("Returned from maths")

def switch_to_gui1():
    print("Switching to physics...")
    window.withdraw()  # Hide the current GUI
    launch_gui1()  # Call the function to launch the second GUI
    print("Returned from phy")

def switch_to_gui3():
    print("Switching to digital system...")
    window.withdraw()  # Hide the current GUI
    launch_gui3()  # Call the function to launch the second GUI
    print("Returned from figital system")

def button_click(event):
    print("Button clicked!")

canvas = Canvas(
    window,
    bg = "#D1EAF0",
    height = 801,
    width = 1474,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=687.0,
    y=701.0,
    width=153.0,
    height=61.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_gui3,
    relief="flat"
)
button_2.place(
    x=541.797607421875,
    y=181.0,
    width=416.202392578125,
    height=514.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_gui1,
    relief="flat"
)
button_3.place(
    x=84.81683349609375,
    y=179.0,
    width=416.18316650390625,
    height=522.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_gui2, #button bound to gui2
    relief="flat"
)
button_4.bind("button_4", button_click)
button_4.place(
    x=1004.912353515625,
    y=179.0,
    width=416.087646484375,
    height=505.0
)

canvas.create_text(
    282.0,
    71.0,
    anchor="nw",
    text="Choose your selective subject !",
    fill="#000000",
    font=("Inter Bold", 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    91.0,
    81.0,
    image=image_image_1
)

def resize_label(event):# Retrieve the new size of the window
    width = window.winfo_width()
    height = window.winfo_height()

window.bind("<Configure>", resize_label)

window.resizable(True, True)
window.mainloop()
