# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button,Scrollbar, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\TT8L-09\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


gui1_window = Tk()

gui1_window.geometry("1474x801")
gui1_window.configure(bg = "#F7F1AF")


canvas = Canvas(
    gui1_window,
    bg = "#F7F1AF",
    height = 801,
    width = 1474,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=260.0,
    y=111.0,
    width=931.9299926757812,
    height=532.2999877929688
)

#Initialize Question
questions_physic = [
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 2",
            "answer": "Option 2"
        },
        {
            "question": "Physics Question 3",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 4",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 5",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 11",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 12",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 15",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 20",
            "answer": "Option 1"
        },  
    ]

current_question_index = 0  # Initialize index to 0

def next_question():
    global current_question_index
    if current_question_index < len(questions_physic) - 1:
       current_question_index += 1
       update_question()  # Disable editing after update
    
           

# Create a Text widget inside button_1 to display questions
text_widget = Text(
    button_1,
    wrap="word",  # Wrap text at word boundaries
    relief="flat",  # Remove any border or relief
    bd=0,  # No border
    highlightthickness=0,  # No highlight
    font=("Inter Regular", 16),  # Adjust font as needed
    spacing1=5,  # Additional spacing between lines
    spacing2=2  # Additional spacing between paragraphs
)
text_widget.pack(expand=True, fill="both")
text_widget.insert("end", questions_physic[current_question_index])
text_widget.config(state="disabled")  # Disable editing

# Insert questions into the Text widget
for question in questions_physic :
    text_widget.insert("end", f"{question}\n\n")  # Insert each question followed by new lines


canvas.create_text(
    660.0,
    358.0,
    anchor="nw",
    text="Questions ",
    fill="#000000",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    1208.0,
    49.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("MADEAwelierPERSONALUSE ExtraBold", 15 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1367.0,
    74.0,
    image=image_image_1
)

canvas.create_text(
    630.0,
    16.0,
    anchor="nw",
    text="Physics",
    fill="#000000",
    font=("Inter Bold", 64 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    81.0,
    81.0,
    image=image_image_2
)

def previous_question():
        global current_question_index
        current_question_index = (current_question_index - 1) % len(questions_physic)
        update_question()

def update_question():
        text_widget.config(state="normal")  # Enable editing to update content
        text_widget.delete(1.0, "end")  # Clear current content
        text_widget.insert("end", questions_physic[current_question_index]["question"])  # Insert current question
        text_widget.config(state="disabled")  # Disable editing after update


        # Enable/disable next and back buttons based on current index
        if current_question_index == 0:
            button_2.config(state="disabled")  # Disable back button on first question
        else:
            button_2.config(state="normal")

        if current_question_index == len(questions_physic) - 1:
            button_3.config(state="disabled")  # Disable next button on last question
            
        else:
            button_3.config(state="normal")
            


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=previous_question,
    relief="flat"
)
button_2.place(
    x=516.0,
    y=688.0,
    width=153.0,
    height=61.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command="next_question,back_to_gui1",
    relief="flat"
)

button_3.place(
    x=805.0,
    y=688.0,
    width=153.0,
    height=61.0
)


gui1_window.resizable(True, True)
gui1_window.mainloop()

