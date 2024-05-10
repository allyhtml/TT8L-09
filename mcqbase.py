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
                "question": "1) What is the primary function of an adder circuit?"
                "option": 
            }
        ]