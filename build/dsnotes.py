
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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
    file="./build/assets/frame3/image_ds.png")
image_1 = canvas.create_image(
    738.0,
    161.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="./build/assets/frame3/image_logo.png")
image_2 = canvas.create_image(
    47.0,
    42.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file="./build/assets/frame3/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_12 clicked"),
    relief="flat"
)
button_1.place(
    x=1051.0,
    y=521.0,
    width=312.0,
    height=104.0
)

button_image_2 = PhotoImage(
    file="./build/assets/frame3/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_11 clicked"),
    relief="flat"
)
button_2.place(
    x=719.0,
    y=511.0,
    width=332.0,
    height=111.0
)

button_image_3 = PhotoImage(
    file="./build/assets/frame3/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_10 clicked"),
    relief="flat"
)
button_3.place(
    x=407.0,
    y=511.0,
    width=312.0,
    height=111.0
)

button_image_4 = PhotoImage(
    file="./build/assets/frame3/button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_9 clicked"),
    relief="flat"
)
button_4.place(
    x=75.0,
    y=521.0,
    width=332.0,
    height=97.0
)

button_image_5 = PhotoImage(
    file="./build/assets/frame3/button_5.png")
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_8 clicked"),
    relief="flat"
)
button_5.place(
    x=1051.0,
    y=406.0,
    width=314.0,
    height=105.0
)

button_image_6 = PhotoImage(
    file="./build/assets/frame3/button_6.png")
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_7 clicked"),
    relief="flat"
)
button_6.place(
    x=729.0,
    y=406.0,
    width=312.0,
    height=105.0
)

button_image_7 = PhotoImage(
    file="./build/assets/frame3/button_7.png")
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_6 clicked"),
    relief="flat"
)
button_7.place(
    x=407.0,
    y=406.0,
    width=322.0,
    height=105.0
)

button_image_8 = PhotoImage(
    file="./build/assets/frame3/button_8.png")
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_5 clicked"),
    relief="flat"
)
button_8.place(
    x=75.0,
    y=406.0,
    width=332.0,
    height=105.0
)

button_image_9 = PhotoImage(
    file="./build/assets/frame3/button_9.png")
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_4 clicked"),
    relief="flat"
)
button_9.place(
    x=1051.0,
    y=276.0,
    width=322.0,
    height=121.0
)

button_image_10 = PhotoImage(
    file="./build/assets/frame3/button_10.png")
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_3 clicked"),
    relief="flat"
)
button_10.place(
    x=719.0,
    y=276.0,
    width=332.0,
    height=121.0
)

button_image_11 = PhotoImage(
    file="./build/assets/frame3/button_11.png")
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_2 clicked"),
    relief="flat"
)
button_11.place(
    x=397.0,
    y=276.0,
    width=332.0,
    height=130.0
)

button_image_12 = PhotoImage(
    file="./build/assets/frame3/button_12.png")
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("c_1 clicked"),
    relief="flat"
)
button_12.place(
    x=75.0,
    y=276.0,
    width=332.0,
    height=121.0
)

button_image_13 = PhotoImage(
    file="./build/assets/frame3/button_back.png")
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_back clicked"),
    relief="flat"
)
button_13.place(
    x=651.0,
    y=707.0,
    width=153.0,
    height=61.0
)

image_image_3 = PhotoImage(
    file="./build/assets/frame3/image_3.png")
image_3 = canvas.create_image(
    156.0,
    714.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file="./build/assets/frame3/image_4.png")
image_4 = canvas.create_image(
    1362.0,
    710.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
