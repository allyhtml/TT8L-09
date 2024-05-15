import tkinter as tk
from tkinter import font 
from random import shuffle

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")

        custom_font = font.Font(family="Helvetica", size=14)

        self.question = [
            {
                "question": "1) What is the primary function of an adder circuit?",
                "options": ["Logical manipulation", "Electric transmission", "Addition of digits", "Multiplication of digits"],
                "answer": "Addition of digits"
            },
            {
                "question": "2) Which component of the CPU extensively uses adders?",
                "options": ["GPU", "ALU", "RAM", "Cache"],
                "answer": "ALU"
            },
            {
                "question": "3) What type of addition do the majority of adders handle?",
                "options": ["Octal addition", "Decimal addition", "Hexa addition", "Binary addition"],
                "answer": "Binary addition"
            }
        ]

        self.score = 0
        self.current_question = 0

       
        self.question_label = tk.Label(self.root, text="", font=custom_font, wraplength=600)
        self.question_label.pack(pady=20)

        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=custom_font, width=40, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        
        self.score_label = tk.Label(self.root, text="Score: 0", font=custom_font)
        self.score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            options = question["options"]
            shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])

    def check_answer(self, selected_option):
        question = self.questions[self.current_question]
        selected_answer = question["options"][selected_option]
        correct_answer = question["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            result_message = "You are correct!"
        else:
            result_message = f"Wrong! The correct answer is: {correct_answer}"

        result_label = tk.Label(self.root, text=result_message)
        result_label.pack()

        self.current_question += 1
        self.score_label.config(text="Score: {}".format(self.score))

        self.root.after(3000, result_label.destroy)
        self.next_question()
 


root = tk.Tk()
app = QuizGame(root)
root.mainloop()
