import tkinter as tk
from tkinter import font, messagebox, PhotoImage, Label, Frame, Entry, Button, Toplevel
import random
import os

# First code: Sign-in and Registration System
def signin():
    email = user.get()
    password = code.get()

    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    saved_email, saved_password = parts
                    if email == saved_email and password == saved_password:
                        messagebox.showinfo("Success", "Login successful!")
                        main_frame.pack_forget()
                        quiz_selection_screen()
                        return
        messagebox.showerror("Error", "Invalid email or password")
    except FileNotFoundError:
        messagebox.showerror("Error", "No registered users found. Please register first.")

def on_enter_email(e):
    if user.get() == 'Email':
        user.delete(0, 'end')

def on_leave_email(e):
    if user.get() == '':
        user.insert(0, 'Email')

def on_enter_password(e):
    if code.get() == 'Password':
        code.delete(0, 'end')
        code.config(show='*')

def on_leave_password(e):
    if code.get() == '':
        code.config(show='')
        code.insert(0, 'Password')

def save_registration():
    email_val = user_entry.get()
    password_val = password_entry.get()

    if not email_val.endswith('@gmail.com'):
        messagebox.showerror("Error", "Invalid email. Please use a valid Gmail address.")
        return

    if len(password_val) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    try:
        with open("user_data.txt", "a") as file:
            file.write(f"{email_val},{password_val}\n")
        messagebox.showinfo("Success", "Registration successful!")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Failed to register. Please try again later.")

def register():
    global user_entry, password_entry
    reg_window = Toplevel(root)
    reg_window.title("Registration")
    reg_window.geometry('400x250+500+300')
    reg_window.config(bg="white")

    reg_label = Label(reg_window, text="Register your account", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
    reg_label.pack()

    email_label = Label(reg_window, text="Email:", bg="white", font=('Microsoft YaHei UI Light', 11))
    email_label.pack()
    user_entry = Entry(reg_window, width=25, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11))
    user_entry.pack()

    password_label = Label(reg_window, text="Password:", bg="white", font=('Microsoft YaHei UI Light', 11))
    password_label.pack()
    password_entry = Entry(reg_window, width=25, fg='black', bg="white", font=('Microsoft YaHei UI Light', 11), show='*')
    password_entry.pack()

    register_button = Button(reg_window, text="Register", bg='#57a1f8', fg='white', command=save_registration)
    register_button.pack()

# Second code: Quiz Game
class QuizGame:
    def __init__(self, root, questions):
        self.root = root
        custom_font = font.Font(family="Helvetica", size=14)
        self.questions = questions
        random.shuffle(self.questions)
        self.score = 0
        self.current_question_index = 0
        self.question_label = tk.Label(self.root, text="", font=custom_font, wraplength=600, bg="#F8C6EF")
        self.question_label.pack(pady=20)
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=custom_font, width=50, height=3, command=lambda i=i: self.check_answer(i), bg="#F1D1CC")
            button.pack(pady=10)
            self.option_buttons.append(button)
        self.score_label = tk.Label(self.root, text="Score:0", font=custom_font, bg="#D1EAF0")
        self.score_label.pack(pady=20)
        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            random.shuffle(options)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
        else:
            self.end_game()

    def check_answer(self, selected_option):
        selected_answer = self.option_buttons[selected_option].cget("text")
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect! The correct answer is: {correct_answer}")
        self.score_label.config(text="Score: {}".format(self.score))
        self.current_question_index += 1
        self.display_question()

    def end_game(self):
        score_message = "Final Score: {}/{}".format(self.score, len(self.questions))
        self.question_label.config(text=score_message)
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 12), command=self.play_again)
        play_again_button.pack(pady=10)
        back_button = tk.Button(self.root, text="Back to Quiz Selection", font=("Arial", 12), command=go_back_to_selection)
        back_button.pack(pady=10)

    def play_again(self):
        self.score = 0
        self.current_question_index = 0
        self.score_label.config(text="Score: 0")
        random.shuffle(self.questions)
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)
        self.display_question()

def open_ds_quiz():
    questions_ds = [
        {
            "question": "Which of the following is a fundamental building block of digital circuits?",
            "options": ["Resistor", "Transistor", "Diode", "Inductor"],
            "answer": "Transistor"
        },
        {
            "question": "What is the binary representation of the decimal number 10? ",
            "options": ["1010", "1100", "1110", "1001"],
            "answer": "1010"
        },
        {
            "question": "Which logic gate outputs true only when both inputs are true? ",
            "options": ["OR gate", "AND gate", "XOR gate", "NOT gate"],
            "answer": "AND gate"
        },
        {
            "question": "What type of signal is continuous and changes smoothly?",
            "options": ["Digital", "Binary", "Analog", "Discrete"],
            "answer": "Analog"
        },
        {
            "question": "Which is an advantage of digital systems?",
            "options": ["More noise-sensitive", "Higher power consumption", "More compact storage", "Larger hardware size"],
            "answer": "More compact storage"
        },
        {
            "question": "What is the result of the binary addition 110101102 +011110112 ?",
            "options": ["101010012", "101011012", "101000012", "101101002"],
            "answer": "101000012"
        },
        {
            "question": "What is the primary characteristic of combinational logic circuits?  ",
            "options": ["They store data", "They produce outputs solely based on current input values", "They have feedback loops", "They only produce outputs when previous states are considered"],
            "answer": "They produce outputs solely based on current input values"
        },
        {
            "question": "What are the two standard forms of Boolean expressions used in combinational logic?  ",
            "options": ["SOP and NAND", "OR and POS", "SOP and POS", ") AND and NOR"],
            "answer": "SOP and POS"
        },
        {
            "question": "What is the primary purpose of a Karnaugh map (K-map) in digital logic design?  ",
            "options": ["To visualize the output waveform ", "To simulate circuit operation ", "To simplify boolean expressions", "To analyze timing diagrams"],
            "answer": "To simplify boolean expressions"
        },
        {
            "question": "What determines the size of a K-map for a given boolean expression? ",
            "options": ["The number of AND gates in the circuit", "The number of OR gates in the circuit", "The number of input variables", "The number of output variables"],
            "answer": "The number of input variables"
        },
        {
            "question": "What is the significance of gray code labeling in Karnaugh maps?",
            "options": ["It ensures adjacent cells differ by only one variable", "It represents the complement of the input variables", "It simplifies the process of mapping boolean expressions", "It reduces the number of required cells in the map"],
            "answer": "It ensures adjacent cells differ by only one variable"
        },
        {
            "question": "What is the purpose of looping in K-map simplification?  ",
            "options": ["To create complex boolean expressions", "To increase the number of required cells", "To identify adjacent 1s for grouping", "To visualize circuit waveforms"],
            "answer": "To identify adjacent 1s for grouping"
        },
        {
            "question": "What is the primary function of a half-adder?  ",
            "options": ["Adds three binary inputs", "Adds two single-bit binary digits", "Detects specific bit patterns", "Converts BCD to decimal"],
            "answer": "Adds two single-bit binary digits"
        },
        {
            "question": "Which type of adder eliminates ripple delays by anticipating output carry at each stage?",
            "options": ["Half-adder", "Full adder", "Ripple carry adder", "Look-ahead carry adder"],
            "answer": "Look-ahead carry adder"
        },
        {
            "question": "What is the main application of a decoder in digital circuits?",
            "options": ["Addition of multiple-bit binary numbers", "Selecting specific bits in a binary number", "Communicating with external devices", "Detecting specific bit patterns on inputs"],
            "answer": "Detecting specific bit patterns on inputs"
        },
        {
            "question": "How does a full adder differ from a half-adder?  ",
            "options": ["Full adder has three binary inputs and two binary outputs", "Full adder performs addition sequentially", "Full adder eliminates ripple delays", "Full adder has only one binary input and one binary output"],
            "answer": "Full adder has three binary inputs and two binary outputs"
        },
        {
            "question": "What type of decoder is used for converting Binary Coded Decimal (BCD) to decimal?",
            "options": ["4-line-to-16-line decoder", "1-of-10 decoder", "BCD-to-7-segment decoder", "4-bit decoder"],
            "answer": "1-of-10 decoder"
        },
        {
            "question": "What is the primary purpose of a clock signal in digital systems?",
            "options": ["To trigger state changes based on clock transitions", "To generate a periodic rectangular pulse train", "To control the data input to flip-flops", "To prevent invalid states in flip-flops"],
            "answer": "To generate a periodic rectangular pulse train"
        },
        {
            "question": "How do edge-triggered flip-flops differ from latches?",
            "options": ["Latches respond to clock edges, while flip-flops do not", "Latches are bistable devices, while flip-flops are not", "Flip-flops change states only at the clock edge", "Latches change states asynchronously"],
            "answer": "Flip-flops change states only at the clock edge"
        },
        {
            "question": "What determines the exact timing of state changes in synchronous digital systems?",
            "options": ["The inputs to logic gates", "The presence of asynchronous inputs", "The clock signal", "The transitions of the clock pulse"],
            "answer": "The clock signal"
        },
        {
            "question": "How does the J-K flip-flop prevent invalid states?",
            "options": ["By checking the clock input", "By using a D flip-flop instead", "By toggling outputs when both inputs are high", "By using an additional enable input"],
            "answer": "By toggling outputs when both inputs are high"
        },
        {
            "question": "What does the least significant bit (LSB) in a binary counter represent?",
            "options": ["The first stage in the counter", "The second stage in the counter", "The most significant bit", "The carry bit"],
            "answer": "The first stage in the counter"
        },
        {
            "question": "What is another name for an asynchronous counter? ",
            "options": ["Ripple counter", "Toggle counter", "Clock counter", "Sequential counter"],
            "answer": "Ripple counter"
        },
        {
            "question": "What is the main disadvantage of asynchronous counters? ",
            "options": ["They require more flip-flops", "They have accumulated propagation delays", "They cannot be used for high clock rates", "They are not reliable"],
            "answer": "They have accumulated propagation delays"
        },
        {
            "question": "What is the modulus of a 4-bit counter? ",
            "options": ["4", "8", "10", "16"],
            "answer": "16"
        },
        {
            "question": "What is the primary function of a shift register in digital systems? ",
            "options": ["Perform arithmetic operations", "Store and transfer data", "Generate clock pulses", "Filter noise from signals"],
            "answer": "Store and transfer data"
        },
        {
            "question": "Which type of shift register allows data to be entered serially and read out in parallel? ",
            "options": ["Serial-in Serial-out (SISO)", "Parallel-in Parallel-out (PIPO)", "Serial-in Parallel-out (SIPO)", "Parallel-in Serial-out (PISO)"],
            "answer": "Serial-in Parallel-out (SIPO)"
        },
        {
            "question": "How many states does a 4-bit Johnson counter have?",
            "options": ["4", "8", "10", "16"],
            "answer": "8"
        },
        {
            "question": "In a ring counter, how is the output of the last flip-flop fed back?",
            "options": ["To the clock input of the first flip-flop", "To the reset input of the first flip-flop", "To the data input of the first flip-flop", "To the Q' output of the first flip-flop"],
            "answer": "To the data input of the first flip-flop"
        },
        {
            "question": "Which shift register counter is sometimes referred to as a twisted-ring counter?",
            "options": ["Ring counter", "Johnson counter", "Binary counter", "Decade counter "],
            "answer": "Johnson counter"
        },
        
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_ds = QuizGame(quiz_frame, questions_ds)

def open_math_quiz():
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
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_math = QuizGame(quiz_frame, questions_math)

def open_physic_quiz():
    questions_physic = [
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 2",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 2"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },
        {
            "question": "Physics Question 1",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": "Option 1"
        },  
    ]
    quiz_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    clear_frame(quiz_frame)
    app_physic = QuizGame(quiz_frame, questions_physic)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def quiz_selection_screen():
    global quiz_frame, saly_16_img, saly_10_img, saly_19_img
    main_frame.pack_forget()
    quiz_frame = tk.Frame(root, bg="#d1eaf0")
    quiz_frame.pack(fill="both", expand=True)
    
    quebiz_section = tk.Label(quiz_frame, text="QUEBIZ SECTION", font=comic_sans_font, bg="#d1eaf0")
    quebiz_section.place(x=500, y=51)
    
    physic1 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic1.place(x=94, y=203)
    physic2 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic2.place(x=558, y=203)
    physic3 = tk.Frame(quiz_frame, bg="#ffc8c0", width=378, height=532)
    physic3.place(x=1022, y=203)
    
    digital_system_label = tk.Label(quiz_frame, text="DIGITAL SYSTEM", font=stylish_font, bg="#ffc8c0", fg="#000")
    digital_system_label.place(x=144, y=222)
    mathematics_label = tk.Label(quiz_frame, text="MATHEMATICS", font=stylish_font, bg="#ffc8c0", fg="#000")
    mathematics_label.place(x=624, y=222)
    physic_label = tk.Label(quiz_frame, text="PHYSIC", font=stylish_font, bg="#ffc8c0", fg="#000")
    physic_label.place(x=1150, y=222)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    saly_16_img = tk.PhotoImage(file=os.path.join(current_dir, "Design/Saly-16.png"))
    saly_16_img = saly_16_img.subsample(1)
    saly_10_img = tk.PhotoImage(file=os.path.join(current_dir, "Design/Saly-10.png"))
    saly_19_img = tk.PhotoImage(file=os.path.join(current_dir, "Design/Saly-19.png"))
    
    saly_16_label = tk.Label(quiz_frame, image=saly_16_img, bg="#FFC8C0")
    saly_16_label.place(x=1064, y=260)
    saly_16_label.image = saly_16_img
    saly_10_label = tk.Label(quiz_frame, image=saly_10_img, bg="#FFC8C0")
    saly_10_label.place(x=578, y=272)
    saly_19_label = tk.Label(quiz_frame, image=saly_19_img, bg="#FFC8C0")
    saly_19_label.place(x=122, y=260)
    
    button_ds = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_ds_quiz)
    button_ds.place(x=195, y=635, width=180, height=50)
    button_math = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_math_quiz)
    button_math.place(x=659, y=635, width=180, height=50)
    button_physic = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_physic_quiz)
    button_physic.place(x=1123, y=635, width=180, height=50)

def go_back_to_selection():
    quiz_frame.pack_forget()
    quiz_selection_screen()

# Main application setup
root = tk.Tk()
root.title('Login and Quiz Application')
root.geometry('1474x801')  # Adjusted geometry to match second code
root.configure(bg="#ffc0db")
root.resizable(False, False)

comic_sans_font = font.Font(family='Comic Sans MS', size=40)
stylish_font = font.Font(family='Stylish', size=20)
zen_dots_font = font.Font(family='Zen Dots', size=20)

main_frame = tk.Frame(root, bg="#ffc0db")
main_frame.place(relwidth=1, relheight=1)

img = PhotoImage(file='Design/logo.png')
Label(main_frame, image=img, bg='white').place(x=-100, y=60)

frame = Frame(main_frame, width=350, height=350, bg="white")
frame.place(relx=0.5, rely=0.5, anchor='center')

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.pack(pady=10)

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.pack(pady=10)
user.insert(0, 'Email')
user.bind('<FocusIn>', on_enter_email)
user.bind('<FocusOut>', on_leave_email)

Frame(frame, width=295, height=2, bg='black').pack()

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.pack(pady=10)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').pack()

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).pack(pady=10)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.pack(pady=10)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=register)
sign_up.pack()

root.mainloop()
