import os
from tkinter import Tk, Canvas, Button, Text, PhotoImage

# Initialize Tkinter window
window = Tk()
window.geometry("1474x801")
window.configure(bg="#D1EAF0")
window.title("Quebizz")

# Function to load images
def load_image(image_path):
    try:
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None

# Define global variables for images
button_image_1 = None
button_image_2 = None
button_image_3 = None
button_image_4 = None
image_image_1 = None

# Function to switch to GUI2
def open_gui2():
    global button_image_2, button_image_3, button_image_4, image_image_1
    
    # Destroy current widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Initialize Canvas
    canvas = Canvas(
        window,
        bg="#F7F1AF",
        height=801,
        width=1474,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Load images if not already loaded
    if button_image_2 is None:
        button_image_2 = load_image("./build/assets/nqa2/button_1.png")
    if button_image_3 is None:
        button_image_3 = load_image("./build/assets/nqa3/button_2.png")
    if button_image_4 is None:
        button_image_4 = load_image("./build/assets/nqa3/button_3.png")
    if image_image_1 is None:
        image_image_1 = load_image("./build/assets/nqa1/image_1.png")

    # Initialize Text widget to display questions
    text_widget = Text(
        canvas,
        wrap="word",  # Wrap text at word boundaries
        relief="flat",  # Remove any border or relief
        bd=0,  # No border
        highlightthickness=0,  # No highlight
        font=("Inter Regular", 16),  # Adjust font as needed
        spacing1=5,  # Additional spacing between lines
        spacing2=2  # Additional spacing between paragraphs
    )
    text_widget.place(x=260, y=111, width=931.93, height=532.3)

   def load_image(image_path):
    try:
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None

def return_gui():
    gui1_window.destroy()
    import gui
    gui.window.mainloop()

def next_question():
    global current_question_index
    if current_question_index < len(questions_physic) - 1:
        current_question_index += 1
        update_question()

def previous_question():
    global current_question_index
    current_question_index = max(0, current_question_index - 1)
    update_question()

def update_question():
    text_widget.config(state="normal")
    text_widget.delete(1.0, "end")
    question = questions_physic[current_question_index]["question"]
    answer = questions_physic[current_question_index]["answer"]
    text_widget.insert("end", f"{question}\n\n{answer}\n\n")
    text_widget.config(state="disabled")

gui1_window = Tk()
gui1_window.geometry("1474x801")
gui1_window.configure(bg="#F7F1AF")

canvas = Canvas(
    gui1_window,
    bg="#F7F1AF",
    height=801,
    width=1474,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

button_image_2 = load_image("./build/assets/nqa2/button_1.png")
button_1 = Button(
    canvas,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=260.0,
    y=111.0,
    width=931.93,
    height=532.3
)

questions_physic = [
    {"question": "Physics Question 1", "answer": "Option 1"},
    {"question": "Physics Question 2", "answer": "Option 2"},
    {"question": "Physics Question 3", "answer": "Option 1"},
    {"question": "Physics Question 4", "answer": "Option 1"},
    {"question": "Physics Question 5", "answer": "Option 1"},
    {"question": "Physics Question 6", "answer": "Option 1"},
    {"question": "Physics Question 7", "answer": "Option 1"},
    {"question": "Physics Question 8", "answer": "Option 1"},
    {"question": "Physics Question 9", "answer": "Option 1"},
    {"question": "Physics Question 10", "answer": "Option 1"},
    {"question": "Physics Question 11", "answer": "Option 1"},
    {"question": "Physics Question 12", "answer": "Option 1"},
    {"question": "Physics Question 13", "answer": "Option 1"},
    {"question": "Physics Question 14", "answer": "Option 1"},
    {"question": "Physics Question 15", "answer": "Option 1"},
    {"question": "Physics Question 16", "answer": "Option 1"},
    {"question": "Physics Question 17", "answer": "Option 1"},
    {"question": "Physics Question 18", "answer": "Option 1"},
    {"question": "Physics Question 19", "answer": "Option 1"},
    {"question": "Physics Question 20", "answer": "Option 1"}
]

current_question_index = 0

text_widget = Text(
    button_1,
    wrap="word",
    relief="flat",
    bd=0,
    highlightthickness=0,
    font=("Inter Regular", 16),
    spacing1=5,
    spacing2=2
)
text_widget.pack(expand=True, fill="both")
update_question()

canvas.create_text(
    660.0,
    358.0,
    anchor="nw",
    text="Questions",
    fill="#000000",
    font=("Inter SemiBold", 30)
)

canvas.create_text(
    630.0,
    16.0,
    anchor="nw",
    text="Physics",
    fill="#000000",
    font=("Inter Bold", 64)
)

image_image_2 = load_image("./build/assets/nqa2/image_2.png")
image_2 = canvas.create_image(
    81.0,
    81.0,
    image=image_image_2
)

button_image_3 = load_image("./build/assets/nqa3/button_2.png")
button_2 = Button(
    canvas,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=previous_question,
    relief="flat"
)
button_2.place(
    x=416.0,
    y=688.0,
    width=153.0,
    height=61.0
)

button_image_4 = load_image("./build/assets/nqa3/button_3.png")
button_3 = Button(
    canvas,
    image=button_image_4,
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
    canvas,
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
window.resizable(True, True)
window.mainloop()
