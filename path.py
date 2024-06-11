from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\TT8L-09\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def switch_to_second_gui():
    window.withdraw()  # Hide the current GUI

    # Create a new Toplevel window for the second GUI
    second_window = Toplevel(window)
    second_window.geometry("1474x801")  # Set the geometry of the new window
    second_window.configure(bg="#ECD5E3")  # Set the background color

    canvas = Canvas(
        second_window,
        bg="#ECD5E3",
        height=801,
        width=1474,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Define the components of the second GUI
    # For brevity, I'm omitting the full definition of the components
    canvas.create_text(
        1208.0,
        49.0,
        anchor="nw",
        text="Username",
        fill="#000000",
        font=("MADEAwelierPERSONALUSE ExtraBold", 15)
    )
    # Add other components as needed...

# Your existing code
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

# Define the button to switch to the second GUI
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    window,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_second_gui,  # Call the function to switch GUIs
    relief="flat"
)
button_4.place(x=1004.912353515625, y=179.0, width=416.087646484375, height=505.0)

# Other buttons and widgets...
# (Omitted for brevity)

window.mainloop()