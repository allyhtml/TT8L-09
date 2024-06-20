# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button,Scrollbar, PhotoImage

def load_image(image_path):
    try:
        # Convert to absolute path
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None


gui1_window = Tk()

gui1_window.geometry("1474x801")
gui1_window.configure(bg = "#F7F1AF")

def return_gui():
    # Code to hide or destroy current window and open gui2
    gui1_window.destroy()
    import gui
    gui.window.mainloop()


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
button_image_2 =load_image("./build/assets/nqa2/button_1.png")
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
        "question": "Which of the following statements best describes the importance of understanding physics in the field of information technology?",
        "answer": "Understanding physics is crucial for improving and operating electronic devices in IT."
    },
    {
        "question": "What is an example of an application where physics knowledge is crucial in IT?",
        "answer": "Applying relativistic corrections in GPS receivers."
    },
    {
        "question": "Which SI base unit is correctly matched with its quantity?",
        "answer": "Time - second (s)"
    },
    {
        "question": "Which of the following is a derived unit?",
        "answer": "Newton (N)"
    },
    {
        "question": "How would you express 2.9 x 10^-6 Hz using a standard prefix?",
        "answer": "2.9 µHz"
    },
    {
        "question": "Which of the following types of motion involves an object moving in a straight line?",
        "answer": "Translational motion"
    },
    {
        "question": "What is the primary difference between distance and displacement?",
        "answer": "Distance is a scalar quantity, while displacement is a vector quantity."
    },
    {
        "question": "What is the SI unit for speed?",
        "answer": "m/s"
    },
    {
        "question": "How is acceleration defined in physics?",
        "answer": "The rate at which an object changes its velocity."
    },
    {
        "question": "What does the slope of a position versus time graph represent?",
        "answer": "Velocity"
    },
    {
        "question": "Which of the following statements about force is correct?",
        "answer": "Force is the cause of acceleration and is a vector quantity because it has both magnitude and direction."
    },
    {
        "question": "What condition must be met for an object to accelerate?",
        "answer": "The net force acting on the object must be greater than zero."
    },
    {
        "question": "According to Newton's first law, if the net force on an object is zero, which of the following statements is true?",
        "answer": "The object's velocity will remain constant, and its acceleration will be zero."
    },
    {
        "question": "Which equation represents Newton's second law of motion?",
        "answer": "F=ma"
    },
    {
        "question": "What does Newton's third law of motion state?",
        "answer": "For every action, there is an equal and opposite reaction."
    },
    {
        "question": "Which of the following statements about periodic motion is true?",
        "answer": "The amount of time it takes for one complete cycle to occur is called the period T of the motion."
    },
    {
        "question": "In simple harmonic motion, what is the restoring force proportional to?",
        "answer": "Displacement"
    },
    {
        "question": "What is the relationship between the period and frequency of an oscillating system? a. They are directly proportional.",
        "answer": "They are inversely proportional."
    },
    {
        "question": "What factor does the period of a simple pendulum depend on?",
        "answer": "Length of the string and value of gravity"
    },
    {
        "question": "What type of oscillations occur when the damping is so large that the motion no longer resembles simple harmonic motion?",
        "answer": "Over-damped"
    },
    {
        "question": "What type of wave requires a material medium for propagation?",
        "answer": "Mechanical wave"
    },
    {
        "question": "Which principle states that the total displacement at any point due to two or more travelling waves is equal to the vector sum of their individual displacements at that point?",
        "answer": "Superposition principle"
    },
    {
        "question": "What principle accurately describes the particle motion in a transverse wave?",
        "answer": "Motion perpendicular to the direction of wave velocity"
    },
    {
        "question": "What is the wave function for a sinusoidal wave given by equation (8)?",
        "answer": "Y = A Sin (kx - ωt)"
    },
    {
        "question": "What are the positions of zero amplitude and maximum amplitude called, respectively, in standing waves?",
        "answer": "Nodes and antinodes"
    }
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
    630.0,
    16.0,
    anchor="nw",
    text="Physics",
    fill="#000000",
    font=("Inter Bold", 64 * -1)
)

image_image_2 =load_image("./build/assets/nqa2/image_2.png")
image_2 = canvas.create_image(
    81.0,
    81.0,
    image=image_image_2
)

def previous_question():
        global current_question_index
        current_question_index = (current_question_index - 1) % len(questions_physic)
        update_question()

         # Enable/disable next and back buttons based on current index
        if current_question_index == 0:
            button_2.config(state="disabled")  # Disable back button on first question
        else:
            button_2.config(state="normal")

        if current_question_index == len(questions_physic) - 1:
           button_3.place_forget()  # Hide the next button on the last question
        else:
            button_3.place(x=928.0, y=688.0)  # Ensure button is placed back if not on last question

def update_question():
        text_widget.config(state="normal")  # Enable editing to update content
        text_widget.delete(1.0, "end")  # Clear current content
        question = questions_physic[current_question_index]["question"]
        answer = questions_physic[current_question_index]["answer"]
        text_widget.insert("end", f" {question}\n\n {answer}\n\n")  # Insert question and answer
        text_widget.config(state="disabled")  # Disable editing after update
        

        # Enable/disable next and back buttons based on current index
        if current_question_index == 0:
            button_2.config(state="disabled")  # Disable back button on first question
        else:
            button_2.config(state="normal")

        if current_question_index == len(questions_physic) - 1:
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

button_image_3 =load_image("./build/assets/nqa3/button_3.png")
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

button_image_5 =load_image("./build/assets/nqa3/button_5.png")
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


gui1_window.resizable(True, True)
gui1_window.mainloop()

