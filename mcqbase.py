import tkinter as tk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")
        self.root.geometry('925x500+300+200')
        self.root.config(bg="#D1EAF0")
        self.root.resizable(False, False)

        custom_font =font.Font(family="Helvetica", size=14)

        self.questions = [
            {
                "question": "1) What is the primary function of an adder circuit?",
                "options": ["Logical manipulation", "Electrical transmission", "Multiplication of digits", "Addition of digits"],
                "answer": "Addition of digits"
            },
            {
                "question": "2) Which component of the CPU extensively uses adders?",
                "options": ["CPU", "ALU", "RAM", "Cache"],
                "answer": "ALU"
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

root = tk.Tk()
app = QuizGame(root)
root.mainloop()

