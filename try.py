import os
from tkinter import Tk, Canvas, Button, Text, Frame, PhotoImage

def load_image(image_path):
    try:
        abs_path = os.path.abspath(image_path)
        image = PhotoImage(file=abs_path)
        return image
    except Exception as e:
        print(f"Failed to load image at {abs_path}: {e}")
        return None

def switch_frame(to_frame):
    for frame in frames:
        frame.pack_forget()
    to_frame.pack(fill="both", expand=True)

def gui0():
    # Clear previous widgets if any
    for widget in main_menu_frame.winfo_children():
        widget.destroy()

    # Create GUI0 content
    canvas_main = Canvas(main_menu_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
    canvas_main.place(x=0, y=0)

    images = {}
    images['button_fc'] = load_image("./build/assets/frame0/button_fc.png")
    button_fc = Button(main_menu_frame, image=images['button_fc'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui0))
    button_fc.place(x=974.0, y=298.0, width=425.0, height=432.0)

    canvas_main.create_text(282.0, 71.0, anchor="nw", text="Your New GUI0", fill="#000000", font=("Inter Bold", 64 * -1))

# Initialize the main window
root = Tk()
root.geometry("1474x801")
root.configure(bg="#D0F0C0")

# Initialize frames
main_menu_frame = Frame(root, bg="#D0F0C0")
gui1_frame = Frame(root, bg="#D1EAF0")
gui2_frame = Frame(root, bg="#D0F0C0")
gui3_frame = Frame(root, bg="#D0F0C0")
frames = [main_menu_frame, gui1_frame, gui2_frame, gui3_frame]

# Main menu content (GUI0)
canvas_main = Canvas(main_menu_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_main.place(x=0, y=0)

images = {}
images['button_image_1'] = load_image("./build/assets/nqa1/button_1.png")
button_main_1 = Button(main_menu_frame, image=images['button_image_1'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: print("button_1 clicked"))
button_main_1.place(x=687.0, y=701.0, width=153.0, height=61.0)

images['button_image_2'] = load_image("./build/assets/nqa1/button_2.png")
button_main_2 = Button(main_menu_frame, image=images['button_image_2'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui3_frame))
button_main_2.place(x=541.797, y=181.0, width=416.202, height=514.0)

images['button_image_3'] = load_image("./build/assets/nqa1/button_3.png")
button_main_3 = Button(main_menu_frame, image=images['button_image_3'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui1_frame))
button_main_3.place(x=84.816, y=179.0, width=416.183, height=522.0)

images['button_image_4'] = load_image("./build/assets/nqa1/button_4.png")
button_main_4 = Button(main_menu_frame, image=images['button_image_4'], borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(gui2_frame))
button_main_4.place(x=1004.912, y=179.0, width=416.087, height=505.0)

canvas_main.create_text(282.0, 71.0, anchor="nw", text="Choose your selective subject !", fill="#000000", font=("Inter Bold", 64 * -1))

images['image_image_1'] = load_image("./build/assets/nqa1/image_1.png")
canvas_main.create_image(91.0, 81.0, image=images['image_image_1'])

# GUI3 content (For illustration, you can replicate similar structures for other GUIs)
canvas_gui3 = Canvas(gui3_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_gui3.place(x=0, y=0)

button_image_gui3_1 = load_image("./build/assets/nqa3/button_1.png")
button_gui3_1 = Button(gui3_frame, image=button_image_gui3_1, borderwidth=0, highlightthickness=0, relief="flat")
button_gui3_1.place(x=260.0, y=111.0, width=931.929, height=532.299)

questions_ds_gui3 = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who is the president of USA?", "answer": "Joe Biden"},
    {"question": "8 + 8?", "answer": "16"},
]

current_question_index_gui3 = 0

text_widget_gui3 = Text(button_gui3_1, wrap="word", relief="flat", bd=0, highlightthickness=0, font=("Inter Regular", 16), spacing1=5, spacing2=2)
text_widget_gui3.pack(expand=True, fill="both")
text_widget_gui3.insert("end", questions_ds_gui3[current_question_index_gui3]["question"] + "\n" + questions_ds_gui3[current_question_index_gui3]["answer"])
text_widget_gui3.config(state="disabled")

def next_question_gui3():
    global current_question_index_gui3
    current_question_index_gui3 = (current_question_index_gui3 + 1) % len(questions_ds_gui3)
    update_question_gui3()

def update_question_gui3():
    text_widget_gui3.config(state="normal")
    text_widget_gui3.delete(1.0, "end")
    question = questions_ds_gui3[current_question_index_gui3]["question"]
    answer = questions_ds_gui3[current_question_index_gui3]["answer"]
    text_widget_gui3.insert("end", f" {question}\n\n {answer}\n\n")
    text_widget_gui3.config(state="disabled")

button_image_gui3_2 = load_image("./build/assets/nqa3/button_3.png")
button_gui3_2 = Button(gui3_frame, image=button_image_gui3_2, borderwidth=0, highlightthickness=0, relief="flat", command=next_question_gui3)
button_gui3_2.place(x=928.0, y=688.0, width=153.0, height=61.0)

button_image_gui3_3 = load_image("./build/assets/nqa3/button_5.png")
button_gui3_3 = Button(gui3_frame, image=button_image_gui3_3, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(main_menu_frame))
button_gui3_3.place(x=622.0, y=688.0, width=243.0, height=61.0)

canvas_gui3.create_text(660.0, 358.0, anchor="nw", text="Questions", fill="#000000", font=("Inter SemiBold", 30 * -1))
canvas_gui3.create_text(580.0, 16.0, anchor="nw", text="Digital System", fill="#000000", font=("Inter Bold", 64 * -1))

image_gui3_2 = load_image("./build/assets/nqa3/image_2.png")
canvas_gui3.create_image(81.0, 81.0, image=image_gui3_2)

# GUI2 content
canvas_gui2 = Canvas(gui2_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_gui2.place(x=0, y=0)

button_image_gui2_1 = load_image("./build/assets/nqa3/button_1.png")
button_gui2_1 = Button(gui2_frame, image=button_image_gui2_1, borderwidth=0, highlightthickness=0, relief="flat")
button_gui2_1.place(x=260.0, y=111.0, width=931.929, height=532.299)

questions_ds_gui2 = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who is the president of USA?", "answer": "Joe Biden"},
    {"question": "8 + 8?", "answer": "16"},
]

current_question_index_gui2 = 0

text_widget_gui2 = Text(button_gui2_1, wrap="word", relief="flat", bd=0, highlightthickness=0, font=("Inter Regular", 16), spacing1=5, spacing2=2)
text_widget_gui2.pack(expand=True, fill="both")
text_widget_gui2.insert("end", questions_ds_gui2[current_question_index_gui2]["question"] + "\n" + questions_ds_gui2[current_question_index_gui2]["answer"])
text_widget_gui2.config(state="disabled")

def next_question_gui2():
    global current_question_index_gui2
    current_question_index_gui2 = (current_question_index_gui2 + 1) % len(questions_ds_gui2)
    update_question_gui2()

def update_question_gui2():
    text_widget_gui2.config(state="normal")
    text_widget_gui2.delete(1.0, "end")
    question = questions_ds_gui2[current_question_index_gui2]["question"]
    answer = questions_ds_gui2[current_question_index_gui2]["answer"]
    text_widget_gui2.insert("end", f" {question}\n\n {answer}\n\n")
    text_widget_gui2.config(state="disabled")

button_image_gui2_2 = load_image("./build/assets/nqa3/button_3.png")
button_gui2_2 = Button(gui2_frame, image=button_image_gui2_2, borderwidth=0, highlightthickness=0, relief="flat", command=next_question_gui2)
button_gui2_2.place(x=928.0, y=688.0, width=153.0, height=61.0)

button_image_gui2_3 = load_image("./build/assets/nqa3/button_5.png")
button_gui2_3 = Button(gui2_frame, image=button_image_gui2_3, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(main_menu_frame))
button_gui2_3.place(x=622.0, y=688.0, width=243.0, height=61.0)

canvas_gui2.create_text(660.0, 358.0, anchor="nw", text="Questions", fill="#000000", font=("Inter SemiBold", 30 * -1))
canvas_gui2.create_text(580.0, 16.0, anchor="nw", text="Digital System", fill="#000000", font=("Inter Bold", 64 * -1))

image_gui2_2 = load_image("./build/assets/nqa3/image_2.png")
canvas_gui2.create_image(81.0, 81.0, image=image_gui2_2)


# GUI1 content
canvas_gui1 = Canvas(gui1_frame, bg="#D0F0C0", height=801, width=1474, bd=0, highlightthickness=0, relief="ridge")
canvas_gui1.place(x=0, y=0)

button_image_gui1_1 = load_image("./build/assets/nqa3/button_1.png")
button_gui1_1 = Button(gui1_frame, image=button_image_gui1_1, borderwidth=0, highlightthickness=0, relief="flat")
button_gui1_1.place(x=260.0, y=111.0, width=931.929, height=532.299)

questions_ds_gui1 = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who is the president of USA?", "answer": "Joe Biden"},
    {"question": "8 + 8?", "answer": "16"},
]

current_question_index_gui1 = 0

text_widget_gui1 = Text(button_gui1_1, wrap="word", relief="flat", bd=0, highlightthickness=0, font=("Inter Regular", 16), spacing1=5, spacing2=2)
text_widget_gui1.pack(expand=True, fill="both")
text_widget_gui1.insert("end", questions_ds_gui1[current_question_index_gui1]["question"] + "\n" + questions_ds_gui1[current_question_index_gui1]["answer"])
text_widget_gui1.config(state="disabled")

def next_question_gui1():
    global current_question_index_gui1
    current_question_index_gui1 = (current_question_index_gui1 + 1) % len(questions_ds_gui1)
    update_question_gui1()

def update_question_gui1():
    text_widget_gui1.config(state="normal")
    text_widget_gui1.delete(1.0, "end")
    question = questions_ds_gui1[current_question_index_gui1]["question"]
    answer = questions_ds_gui1[current_question_index_gui1]["answer"]
    text_widget_gui1.insert("end", f" {question}\n\n {answer}\n\n")
    text_widget_gui1.config(state="disabled")

button_image_gui1_2 = load_image("./build/assets/nqa3/button_3.png")
button_gui1_2 = Button(gui1_frame, image=button_image_gui1_2, borderwidth=0, highlightthickness=0, relief="flat", command=next_question_gui1)
button_gui1_2.place(x=928.0, y=688.0, width=153.0, height=61.0)

button_image_gui1_3 = load_image("./build/assets/nqa3/button_5.png")
button_gui1_3 = Button(gui1_frame, image=button_image_gui1_3, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: switch_frame(main_menu_frame))
button_gui1_3.place(x=622.0, y=688.0, width=243.0, height=61.0)

canvas_gui1.create_text(660.0, 358.0, anchor="nw", text="Questions", fill="#000000", font=("Inter SemiBold", 30 * -1))
canvas_gui1.create_text(580.0, 16.0, anchor="nw", text="Digital System", fill="#000000", font=("Inter Bold", 64 * -1))

image_gui1_2 = load_image("./build/assets/nqa3/image_2.png")
canvas_gui1.create_image(81.0, 81.0, image=image_gui1_2)

# Switch to the main menu frame initially
switch_frame(main_menu_frame)

# Main loop
root.mainloop()

