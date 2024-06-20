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



gui2_window = Tk()

gui2_window.geometry("1474x801")
gui2_window.configure(bg = "#ECD5E3")

def return_gui():
    # Code to hide or destroy current window and open gui2
    gui2_window.destroy()
    import gui
    gui.window.mainloop()


canvas = Canvas(
    gui2_window,
    bg = "#ECD5E3",
    height = 801,
    width = 1474,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_2 = load_image("./build/assets/nqa3/button_1.png")
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
questions_math = [
        {
            "question": "If a1=3a_1 = 3a1 =3 and an=2an−1+5a_n = 2a_{n-1} + 5an =2an−1 +5 for n≥2n \geq 2n≥2, what is a3a_3a3 ?",
            "options": ["17", "21", "19", "23"],
            "answer": "21"
        },
        {
            "question": "What is 5! (5 factorial)?",
            "options": ["60", "100", "120", "150"],
            "answer": "120"
        },
        {
            "question": "Expand and evaluate the sum ∑i=13 (2i−1)",
            "options": ["6", "9", "12", "15"],
            "answer": "9"
        },
        {
            "question": "Find the ninth term of the arithmetic sequence whose first term is 6 and whose common difference is -5",
            "options": ["-34", "-39", "-41", "-46"],
            "answer": "-34"
        },
        {
            "question": "Find the sum of the first 3 terms of the geometric sequence: 2, -6, 18",
            "options": ["14", "-2", "10", "18"],
            "answer": "14"
        },
        {
            "question": "Which of the following is a system of linear equations?",
            "options": ["x^2+y^2=1", "3x+2y=6 and x-y=4", "y=3x^2+4", "x^3+y=2"],
            "answer": "3x+2y=6 and x-y=4"
        },
        {
            "question": "Which method is used to eliminate one variable by adding or subtracting equations?",
            "options": ["Substitution Method", "Elimination Method", "Graphical Method", "Matrix Method"],
            "answer": "Elimination Method"
        },
        {
            "question": "What is the solution to the system x+y=5 and 2x-y=1 using the substitution method?",
            "options": ["(2,3)", "(3,2)", "(1,4)", "(4,1)"],
            "answer": "(2,3)"
        },
        {
            "question": "How many solutions does a system of linear equations have if the lines are parallel?",
            "options": ["One solution", "Many solution", "Infinitely many solutions", "Cnnot be determined"],
            "answer": "No solution"
        },
        {
            "question": "What is the determinant of the matrix",
            "options": ["10", "11", "8", "14"],
            "answer": "10"
        },
        {
            "question": "Which of the following quantities is a vector?",
            "options": ["Speed", "Mass", "Temperature", "Velocity"],
            "answer": "Velocity"
        },
        {
            "question": "What is the magnitude of the vector v=(3,4)v = (3, 4)v=(3,4) in 2-dimensional space?",
            "options": ["5", "7", "6", "8"],
            "answer": "5"
        },
        {
            "question": "Two vectors are considered equal if they have:",
            "options": ["The same initial point", "The same magnitude and direction, regardless of their initial points ", "The same terminal point", "The same initial and terminal points"],
            "answer": "The same magnitude and direction, regardless of their initial points"
        },
        {
            "question": "If u=(1,2,3) and v=(4,5,6), what is their dot product u.v?",
            "options": ["32", "38", "26", "42"],
            "answer": "32"
        },
        {
            "question": "Which of the following best describes statistics?",
            "options": ["A branch of science that deals with the study of living organisms", " A branch of mathematics concerned with collecting, organizing, summarizing, and analyzing information", "A branch of literature that involves storytelling and poetry.", "A branch of history focusing on ancient civilizations."],
            "answer": " A branch of mathematics concerned with collecting, organizing, summarizing, and analyzing information"
        },
        {
            "question": "What is the main focus of inferential statistics?",
            "options": ["Organizing and summarizing data using tables and graphs", "Making decisions about a population based on sample data.", "Collecting data from all members of a population.", "Describing data using numerical techniques."],
            "answer": "Making decisions about a population based on sample data." 
        },
        {
            "question": "Which of the following is an example of a population?",
            "options": ["The heights of 100 secondary students in Malaysia", "The income taxes collected from 50 companies in Malaysia", "The prices of all houses sold by a developer", "The weights of 14 policemen in a country"],
            "answer": "The prices of all houses sold by a developer"
        },
        {
            "question": "Identify the type of variable: The weight of engineering students",
            "options": ["Qualitative Variable", "Discrete Variable", "Continuous Variable", "Categorical Variable"],
            "answer": "Continuous Variable"
        },
        {
            "question": "Which of the following is an example of a quantitative variable?",
            "options": ["Hair colors", "Types of product produced in a factory", "Height of policemen in a physical test", "Religious affiliation"],
            "answer": "Height of policemen in a physical test"
        },
        {
            "question": "What is the cross product of vectors u=(1,0,0) and v=(0,1,0) in 3-dimensional space?",
            "options": ["(0,0,1)", "(0,0,-1) ", "(1,1,0)", "(1,0,1)"],
            "answer": "(0,0,1)"
        },
        {
            "question": "What is a set?",
            "options": ["A collection of elements arranged in a specific order", "A collection whose members are specified by a list or a rule.", "A single element with no other elements.", "A collection of numbers arranged in ascending order"],
            "answer": "A collection whose members are specified by a list or a rule"
        },
        {
            "question": "Which symbol represents x is an element of a set X?",
            "options": [" x ⊆ X", "x ∈ X ", "x ∉ X", "x ⊂ X"],
            "answer": "x ∈ X "
        },
        {
            "question": "What does the union of two sets A and B represent?",
            "options": ["The intersection of set A and set B", "The combination of all elements in set A and set B. ", "The set of elements common to both set A and set B.", "The set of elements that are in either set A or set B or both."],
            "answer": "The set of elements that are in either set A or set B or both."
        },
        {
            "question": "If A = {2, 4, 6} and B = {3, 6, 9}, what is A ∩ B?",
            "options": ["{2, 3, 4, 6, 9}", "{ } (empty set)", "{6}", "{2, 4}"],
            "answer": "{6}"
        },
        {
            "question": "What is the complement of set A, denoted as A'?",
            "options": ["The set of all elements in A.", "The set of all elements not in set A.", "The set of elements common to set A and its complement.", "The set of elements in set A and its complement"],
            "answer": "The set of all elements not in set A."
        },
        {
            "question": "For a binomial distribution with parameters n=10 and p=0.5p = 0.5p=0.5, what is the mean (μ) of the distribution?",
            "options": ["2.5", "5", "7.5", "10"],
            "answer": "5"
        },
        {
            "question": "For a standard normal distribution, what is the Z-score corresponding to the 95th percentile?",
            "options": ["1.28", "1.65", "1.96", "2.33"],
            "answer": "1.96"
        },
        {
            "question": "In a binomial distribution with n=5 and p=0.2, what is the standard deviation (σ)?",
            "options": ["0.4", "0.8", "1", "1.2"],
            "answer": "0.8"
        },
        {
            "question": "Which of the following is true for a normal distribution curve?",
            "options": ["The total area under the curve is less than 1.", "The curve is skewed to the right. ", "The mean, median, and mode are all equal.", "The curve has a single peak at x=σ."],
            "answer": "The mean, median, and mode are all equal."
        },
        {
            "question": "In a normal distribution with mean μ=50 and standard deviation σ=5, what is the z-score corresponding to X=60?",
            "options": ["1", "2", "8", "10"],
            "answer": "2"
        },    
    ]

current_question_index = 0  # Initialize index to 0

def next_question():
    global current_question_index
    if current_question_index < len(questions_math) - 1:
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
text_widget.insert("end", questions_math[current_question_index])
text_widget.config(state="disabled")  # Disable editing

# Insert questions into the Text widget
for question in questions_math :
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
    text="Mathematics",
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
        current_question_index = (current_question_index - 1) % len(questions_math)
        update_question()

def update_question():
        text_widget.config(state="normal")  # Enable editing to update content
        text_widget.delete(1.0, "end")  # Clear current content
        question = questions_math[current_question_index]["question"]
        answer = questions_math[current_question_index]["answer"]
        text_widget.insert("end", f" {question}\n\n {answer}\n\n")  # Insert question and answer
        text_widget.config(state="disabled")  # Disable editing after update
        


        # Enable/disable next and back buttons based on current index
        if current_question_index == 0:
           button_2.grid_remove()  # Hide back button on first question
           button_2.config(state="disabled")  # Disable back button on first question
        else:
            button_2.place(x=416.0, y=688.0)
            button_2.config(state="normal")


        if current_question_index == len(questions_math) - 1:
           button_3.place_forget()  # Hide the next button on the last question
        else:
            button_3.place(x=928.0, y=688.0)  # Ensure button is placed back if not on last question
            
            


button_image_2 = load_image("./build/assets/nqa3/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=previous_question,
    relief="flat",
    state="normal"
)
button_2.place(
    x=416.0,
    y=688.0,
    width=153.0,
    height=61.0
)

button_image_3 =  load_image("./build/assets/nqa3/button_3.png")
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



gui2_window.resizable(True, True)
gui2_window.mainloop()
