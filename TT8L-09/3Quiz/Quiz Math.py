import tkinter as tk
from tkinter import font, messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")
        self.root.geometry('925x500+300+200')
        self.root.config(bg="#D1EAF0")
        self.root.resizable(False, False)

        custom_font = font.Font(family="Helvetica", size=14)

        self.questions = [
            {
                "question": "1+1",
                "options": ["2", "3", "4", "5"],
                "answer": "2"
            },
            {
                "question": "Which component of the CPU extensively uses adders?",
                "options": ["CPU", "ALU", "RAM", "Cache"],
                "answer": "ALU"
            },
            {
                "question": "What does SOP stand for in the context of Boolean expressions?",
                "options": ["Sum-of-Products", "Product-of-Sums", "Sum-of-Possibilities", "Product-of-Products"],
                "answer": "Sum-of-Products"
            },
            {
                "question": "Which gate outputs high when inputs disagree?",
                "options": ["AND Gate", "OR Gate", "XOR Gate", "NOT Gate"],
                "answer": "XOR Gate"
            },
            {
                "question": "What is the function of a NAND gate?",
                "options": ["It outputs high when inputs are low or not identical.", "It outputs high only when both inputs are high.", "It outputs low when inputs are low or not identical.", "It outputs low only when both inputs are high."],
                "answer": "It outputs high when inputs are low or not identical."
            },
            {
                "question": "What does POS stand for?",
                "options": ["Product-of-Sums", "Product-of-Strings", "Product-of-Supplies", "Product-of-Solutions"],
                "answer": "Product-of-Sums"
            },
            {
                "question": "Which gate can function as either NOR or a negative-AND gate?",
                "options": ["NAND Gate", "OR Gate", "NOR Gate", "XOR Gate"],
                "answer": "NOR Gate"
            },
            {
                "question": "Which Boolean algebra theorem states that A + A = A?",
                "options": ["Idempotent Law", "Complement Law", "Identity Law", "Distributive Law"],
                "answer": "Idempotent Law"
            },
            {
                "question": "What is the output of an XOR gate when both inputs are the same?",
                "options": ["High", "Low", "Depends on the inputs", "Undefined"],
                "answer": "Low"
            },
            {
                "question": "Convert the Boolean AB + A'C into SOP standard form",
                "options": ["AB + AC", "AB + A'C + ABC", "AB + A'C + A'C'", "AB + A'C + AB'C"],
                "answer": "AB + A'C + AB'C"
            },
 
        ]

        random.shuffle(self.questions)

        self.score = 0
        self.current_question_index = 0  

        self.question_label = tk.Label(self.root, text="", font=custom_font, wraplength=600, bg="#F1D1CC")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=custom_font, width=40, command=lambda i=i: self.check_answer(i), bg="#F1D1CC")
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0", font=custom_font, bg="#D1EAF0")
        self.score_label.pack(pady=10)

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

    def play_again(self):
        self.score = 0
        self.current_question_index = 0
        self.score_label.config(text="Score: 0")
        self.display_question()

        for button in self.option_buttons:
            button.config(state=tk.NORMAL)

root = tk.Tk()
app = QuizGame(root)
root.mainloop()