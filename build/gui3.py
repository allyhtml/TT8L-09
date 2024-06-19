
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


gui3_window = Tk()

gui3_window.geometry("1474x801")
gui3_window.configure(bg = "#D0F0C0")

def return_to_main_gui():
    gui3_window.destroy()  # Close current window
    import gui  # Import the main GUI module to return to it


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
            "question": "Which logic gate outputs true only when both inputs are true? ",
            "answer": "AND gate"
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
            "question": "What is the primary characteristic of combinational logic circuits?  ",
            "answer": "They produce outputs solely based on current input values"
        },
        {
            "question": "What are the two standard forms of Boolean expressions used in combinational logic?  ",
            "answer": "SOP and POS"
        },
        {
            "question": "What is the primary purpose of a Karnaugh map (K-map) in digital logic design?  ",
            "answer": "To simplify boolean expressions"
        },
        {
            "question": "What determines the size of a K-map for a given boolean expression? ",
            "answer": "The number of input variables"
        },
        {
            "question": "What is the significance of gray code labeling in Karnaugh maps?",
            "answer": "It ensures adjacent cells differ by only one variable"
        },
        {
            "question": "What is the purpose of looping in K-map simplification?  ",
            "answer": "To identify adjacent 1s for grouping"
        },
        {
            "question": "What is the primary function of a half-adder?  ",
            "answer": "Adds two single-bit binary digits"
        },
        {
            "question": "Which type of adder eliminates ripple delays by anticipating output carry at each stage?",
            "answer": "Look-ahead carry adder"
        },
        {
            "question": "What is the main application of a decoder in digital circuits?",
            "answer": "Detecting specific bit patterns on inputs"
        },
        {
            "question": "How does a full adder differ from a half-adder?  ",
            "answer": "Full adder has three binary inputs and two binary outputs"
        },
        {
            "question": "What type of decoder is used for converting Binary Coded Decimal (BCD) to decimal?",
            "answer": "1-of-10 decoder"
        },
        {
            "question": "What is the primary purpose of a clock signal in digital systems?",
            "answer": "To generate a periodic rectangular pulse train"
        },
        {
            "question": "How do edge-triggered flip-flops differ from latches?",
            "answer": "Flip-flops change states only at the clock edge"
        },
        {
            "question": "What determines the exact timing of state changes in synchronous digital systems?",
            "answer": "The clock signal"
        },
        {
            "question": "How does the J-K flip-flop prevent invalid states?",
            "answer": "By toggling outputs when both inputs are high"
        },
        {
            "question": "What does the least significant bit (LSB) in a binary counter represent?",
            "answer": "The first stage in the counter"
        },
        {
            "question": "What is another name for an asynchronous counter? ",
            "answer": "Ripple counter"
        },
        {
            "question": "What is the main disadvantage of asynchronous counters? ",
            "answer": "They have accumulated propagation delays"
        },
        {
            "question": "What is the modulus of a 4-bit counter? ",
            "answer": "16"
        },
        {
            "question": "What is the primary function of a shift register in digital systems? ",
            "answer": "Store and transfer data"
        },
        {
            "question": "Which type of shift register allows data to be entered serially and read out in parallel? ",
            "answer": "Serial-in Parallel-out (SIPO)"
        },
        {
            "question": "How many states does a 4-bit Johnson counter have?",
            "answer": "8"
        },
        {
            "question": "In a ring counter, how is the output of the last flip-flop fed back?",
            "answer": "To the data input of the first flip-flop"
        },
        {
            "question": "Which shift register counter is sometimes referred to as a twisted-ring counter?",
            "answer": "Johnson counter"
        },
        
    ]

current_question_index = 0  # Initialize index to 0

def next_question():
    global current_question_index
    if current_question_index < len(questions_ds) - 1:
       current_question_index += 1
       update_question()  # Disable editing after update
    
    else:
        return_to_main_gui()  # Return to the main GUI when all questions are finished   


           

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
    580.0,
    16.0,
    anchor="nw",
    text="Digital System",
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
    command=next_question,
    relief="flat"
)
button_3.place(
    x=805.0,
    y=688.0,
    width=153.0,
    height=61.0
)


gui3_window.resizable(True, True)
gui3_window.mainloop()

