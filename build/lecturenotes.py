
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import subprocess
import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\allys\TT8L-09\build\assets\frame1")

BACK_PATH = os.path.join(OUTPUT_PATH, "mainmenu.py")
PHY_PATH = os.path.join(OUTPUT_PATH, "physicsn.py")
DS_PATH = os.path.join(OUTPUT_PATH, "dsn.py")
MATHS_PATH = os.path.join(OUTPUT_PATH, "mathsn.py")

def back_mainmenu():
    window.destroy()  # Close the current window
    subprocess.run(["python", BACK_PATH])

def phys_notes():
    window.destroy()  # Close the current window
    subprocess.run(["python", PHY_PATH])

def ds_notes():
    window.destroy()  # Close the current window
    subprocess.run(["python", DS_PATH])

def maths_notes():
    window.destroy()  # Close the current window
    subprocess.run(["python", MATHS_PATH])

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1474x801")
window.configure(bg = "#D1EAF0")


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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_lectn.png"))
image_1 = canvas.create_image(
    732.0,
    131.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_maths.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=maths_notes,
    relief="flat"
)
button_1.place(
    x=970.0,
    y=249.0,
    width=435.0,
    height=472.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_ds.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=ds_notes,
    relief="flat"
)
button_2.place(
    x=522.0,
    y=258.0,
    width=438.0,
    height=473.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_phy.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=phys_notes,
    relief="flat"
)
button_3.place(
    x=69.0,
    y=258.0,
    width=440.0,
    height=473.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_logo.png"))
image_2 = canvas.create_image(
    44.0,
    41.0,
    image=image_image_2
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_back.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=back_mainmenu,
    relief="flat"
)
button_4.place(
    x=667.0,
    y=721.0,
    width=153.0,
    height=61.0
)
window.resizable(False, False)
window.mainloop()
