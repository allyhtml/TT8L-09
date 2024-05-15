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

root = tk.Tk()
app = QuizGame(root)
root.mainloop()
