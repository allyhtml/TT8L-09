
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import datetime
import pytz 
import subprocess
import os

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

dt_mst = datetime.datetime.now(tz=pytz.timezone('MST'))
formatted_date = dt_mst.strftime('%A, %B %d, %Y')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\allys\TT8L-09\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

LN_PATH = os.path.join(OUTPUT_PATH, "lecturenotes.py")

def lecture_notes():
    window.destroy()  # Close the current window
    subprocess.run(["python", LN_PATH])

window = Tk()

window.geometry("1474x801")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 801,
    width = 1474,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1474.0,
    801.0,
    fill="#D1EAF0",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_flashcards.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=966.0,
    y=275.0,
    width=435.0,
    height=472.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_lnotes.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lecture_notes,
    relief="flat"
)
button_2.place(
    x=518.0,
    y=284.0,
    width=438.0,
    height=473.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_revq.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=65.0,
    y=284.0,
    width=440.0,
    height=473.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_main.png"))
image_1 = canvas.create_image(
    732.0,
    185.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_deco.png"))
image_2 = canvas.create_image(
    1018.0,
    161.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    132.0,
    50.0,
    image=image_image_3
)

canvas.create_text(
    626.0,
    31.0,
    anchor="nw",
    text=formatted_date,
    fill="#000000",
    font=("MADEAwelierPERSONALUSE ExtraBold", 25 * -1)
)
window.resizable(False, False)
window.mainloop()
