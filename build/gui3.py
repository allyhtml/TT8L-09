import pygame
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

# Initialize pygame for background music
pygame.mixer.init()
pygame.mixer.music.load('background audio.mp3')
pygame.mixer.music.play(-1)  # Repeat indefinitely
pygame.mixer.music.set_volume(0.2)  # Adjust volume (range: 0.0 to 1.0)

# Delay BG
pygame.time.delay(5000)

def load_image(image_path):
    try:
        # Convert to absolute path
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None


gui3_window = Tk()

gui3_window.geometry("1474x801")
gui3_window.configure(bg = "#D0F0C0")



def return_gui():
    # Code to hide or destroy current window and open gui2
    gui3_window.destroy()
    import gui
    gui.window.mainloop()

    canvas = Canvas(
        gui3_window,
        bg = "#D0F0C0",
        height = 801,
        width = 1474,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = load_image("./build/assets/nqa3/button_1.png")             #WHITE SCREEN

button_1 = Button(
    image=button_image_1,
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
    questions_ds =[
            {
                "question": "Which of the following is a fundamental building block of digital circuits?",
                "answer": "Transistor"
            }, 
            {
                "question": "What is the binary representation of the decimal number 10? ",
                "answer": "1010"
            }, 
            {
                "question": "Which logic gate outputs true only when both inputs are true?",
                "answer": "AND Gate"
            }, 
            {
                "question": "What type of signal is continuous and changes smoothly?",
                "answer": "Analog"
            }, 
            {
                "question": "Which is an advantage of digital systems?",
                "answer": "More compact storage"
            }, 
            {
                "question": "What is the result of the binary addition 110101102 +011110112 ?",
                "answer": "101000012"
            }, 
            {
                "question": "What is the primary characteristic of combinational logic circuits?",
                "answer": "They produce outputs solely based on current input values"
            }, 
            {
                "question": "What are the two standard forms of Boolean expressions used in combinational logic?",
                "answer": "SOP and POS"
            }, 
            {
                "question": "What is the primary purpose of a Karnaugh map (K-map) in digital logic design?",
                "answer": "To simplify boolean expressions"
            }, 
            {
                "question": "What determines the size of a K-map for a given boolean expression?",
                "answer": "The number of input variables"
            }, 
        ]

    current_question_index = 0  # Initialize index to 0

def next_question():
    global current_question_index
    if current_question_index < len(questions_ds) - 1:
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
text_widget.insert("end", questions_ds[current_question_index])
text_widget.config(state="disabled")  # Disable editing
# Place the Text widget inside button_1


# Insert questions into the Text widget
for question in questions_ds :
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
    580.0,
    16.0,
    anchor="nw",
    text="Digital System",
    fill="#000000",
    font=("Inter Bold", 64 * -1)
)

image_image_2 = load_image("./build/assets/nqa3/image_2.png")
image_2 = canvas.create_image(
    81.0,
    81.0,
    image=image_image_2
)

def previous_question():
        global current_question_index
        current_question_index = (current_question_index - 1) % len(questions_ds)
        update_question()

def update_question():
        text_widget.config(state="normal")  # Enable editing to update content
        text_widget.delete(1.0, "end")  # Clear current content
        question = questions_ds[current_question_index]["question"]
        answer = questions_ds[current_question_index]["answer"]
        text_widget.insert("end", f" {question}\n\n {answer}\n\n")  # Insert question and answer
        text_widget.config(state="disabled")  # Disable editing after update
        

        # Enable/disable next and back buttons based on current index
        if current_question_index == 0:
            button_2.config(state="disabled")  # Disable back button on first question
        else:
            button_2.config(state="normal")

        if current_question_index == len(questions_ds) - 1:
           button_3.place_forget()  # Hide the next button on the last question
        else:
            button_3.place(x=928.0, y=688.0)  # Ensure button is placed back if not on last question
            


button_image_2 = load_image("./build/assets/nqa3/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=previous_question,
    relief="flat"
)
button_2.place(
    x=416.0,
    y=688.0,
    width=153.0,
    height=61.0
)

button_image_3 = load_image("./build/assets/nqa3/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=next_question,
    relief="flat"
)
button_3.place(
    x=928.0,
    y=688.0,
    width=153.0,
    height=61.0
)


button_image_5 = load_image("./build/assets/nqa3/button_5.png")
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=return_gui,
    relief="flat"
)
button_5.place(
    x=622.0,
    y=688.0,
    width=243.0,
    height=61.0
)

    gui3_window.resizable(True, True)

flashcards_screen()
