import tkinter as tk
from tkinter import font 
from random import shuffle

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")