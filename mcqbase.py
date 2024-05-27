import tkinter as tk
from tkinter import font, messagebox
import random
from PIL import Image, ImageTk  # Import necessary modules from PIL

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")
        self.root.geometry('925x500+300+200')
        self.root.config(bg="#D1EAF0")  # Set background color
        self.root.resizable(False, False)

        custom_font = font.Font(family="Helvetica", size=14)

        self.questions = [
            {
                "question": "1) What is the primary function of an adder circuit?",
                "options": ["Logical manipulation", "Electrical transmission", "Multiplication of digits", "Addition of digits"],
                "answer": "Addition of digits"
            },
            {
                "question": "2) Which component of the CPU extensively uses adders?",
                "options": ["GPU", "ALU", "RAM", "Cache"],
                "answer": "ALU"
            },
            # Add more questions here
        ]

        # Shuffle questions to randomize their order
        random.shuffle(self.questions)

        self.score = 0
        self.current_question_index = 0  # Track the index of the current question

        # Example image
        self.image = Image.open("example_image.jpg")  # Replace "example_image.jpg" with your image file
        self.image = self.image.resize((100, 100), Image.ANTIALIAS)  # Resize image as needed
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image at specified position
        self.image_label = tk.Label(self.root, image=self.photo, bg="#D1EAF0")
        self.image_label.place(x=20, y=20)  # Adjust position as needed

        self.question_label = tk.Label(self.root, text="", font=custom_font, wraplength=600, bg="pink")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=custom_font, width=40, command=lambda i=i: self.check_answer(i), bg="pink")
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0", font=custom_font, bg="#D1EAF0")
        self.score_label.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)

        else:
            self.question_label.config(text="Quiz finished!")
            for button in self.option_buttons:
                button.config(text="")

    def check_answer(self, selected_option):
        selected_answer = self.option_buttons[selected_option].cget("text")
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Your answer is incorrect!")

        self.score_label.config(text="Score: {}".format(self.score))

        # Move to the next question
        self.current_question_index += 1
        self.display_question()  # Display the next question

# Create a Tkinter window and start the quiz game
root = tk.Tk()
app = QuizGame(root)
root.mainloop()











