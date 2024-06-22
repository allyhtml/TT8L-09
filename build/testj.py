import os
from pathlib import Path
import pygame
import tkinter as tk 
from tkinter import Tk, Canvas, Button, Text, PhotoImage

# Initialize pygame mixer for audio
pygame.mixer.init()
pygame.mixer.music.load('background audio.mp3')
pygame.mixer.music.play(-1)  # Play background music indefinitely
pygame.mixer.music.set_volume(0.2)  # Set music volume

# Delay for 5 seconds
pygame.time.delay(5000)

def load_image(image_path):
    try:
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None

# Function to switch to GUI 1
def open_gui1():
    MainFC.destroy()  # Destroy current window
    import gui1  # Load GUI 1 module

# Function to switch to GUI 2
def open_gui2():
    MainFC.destroy()  # Destroy current window
    import gui2  # Load GUI 2 module

# Function to switch to GUI 3
def open_gui3():
    MainFC.destroy()  # Destroy current window
    import gui3  # Load GUI 3 module

class MainFC(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.title("MainFC Window")
        
# Initialize main Tkinter window
    window = Tk()
    window.geometry("1474x801")
    window.configure(bg="#D1EAF0")
    window.title("Quebizz")

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

# Load images for buttons and other elements
    button_image_1 = load_image("./build/assets/nqa1/button_1.png")
    button_image_2 = load_image("./build/assets/nqa1/button_2.png")
    button_image_3 = load_image("./build/assets/nqa1/button_3.png")
    button_image_4 = load_image("./build/assets/nqa1/button_4.png")
    image_image_1 = load_image("./build/assets/nqa1/image_1.png")

# Create buttons on the main window
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui1,
        relief="flat"
    )
    button_1.place(x=687.0, y=701.0, width=153.0, height=61.0)

    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui3,
        relief="flat"
    )
    button_2.place(x=541.797607421875, y=181.0, width=416.202392578125, height=514.0)

    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui1,
        relief="flat"
    )
    button_3.place(x=84.81683349609375, y=179.0, width=416.18316650390625, height=522.0)

    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui2,
        relief="flat"
    )
    button_4.place(x=1004.912353515625, y=179.0, width=416.087646484375, height=505.0)

    canvas.create_text(
        282.0,
        71.0,
        anchor="nw",
        text="Choose your selective subject !",
        fill="#000000",
        font=("Inter Bold", 64 * -1)
    )

    canvas.create_image(
        91.0,
        81.0,
        image=image_image_1
    )

    window.resizable(True, True)
    window.mainloop()
