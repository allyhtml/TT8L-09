import tkinter as tk
from tkinter import font, messagebox, PhotoImage
import os

def open_ds_quiz():
    messagebox.showinfo("Quiz", "Opening Digital System Quiz")

def open_math_quiz():
    messagebox.showinfo("Quiz", "Opening Mathematics Quiz")

def open_physic_quiz():
    messagebox.showinfo("Quiz", "Opening Physics Quiz")

def quiz_selection_menu():
    root = tk.Tk()
    root.title("Quiz Selection")
    root.geometry("1500x800")
    root.configure(bg="#d1eaf0")

    # Define fonts
    comic_sans_font = font.Font(family="Comic Sans MS", size=20)
    stylish_font = font.Font(family="Stylish", size=20)
    zen_dots_font = font.Font(family="Zen Dots", size=20)

    # Define global variables
    main_frame = tk.Frame(root, bg="#d1eaf0")
    main_frame.pack(fill="both", expand=True)
    quiz_frame = None

    def quiz_selection_screen():
        nonlocal quiz_frame
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
        print("Current directory:", current_dir)  # Debug line to check current directory
        
        saly_16_path = os.path.join(current_dir, "Design/Saly-16.png")
        saly_10_path = os.path.join(current_dir, "Design/Saly-10.png")
        saly_19_path = os.path.join(current_dir, "Design/Saly-19.png")
        
        print("Saly-16 path:", saly_16_path)  # Debug line to check image paths
        
        if os.path.exists(saly_16_path):
            saly_16_img = tk.PhotoImage(file=saly_16_path)
            saly_16_img = saly_16_img.subsample(1)
            saly_16_label = tk.Label(quiz_frame, image=saly_16_img, bg="#ffc8c0")
            saly_16_label.place(x=1064, y=260)
            saly_16_label.image = saly_16_img
        else:
            print("Error: Saly-16.png not found")
        
        if os.path.exists(saly_10_path):
            saly_10_img = tk.PhotoImage(file=saly_10_path)
            saly_10_label = tk.Label(quiz_frame, image=saly_10_img, bg="#ffc8c0")
            saly_10_label.place(x=578, y=272)
            saly_10_label.image = saly_10_img
        else:
            print("Error: Saly-10.png not found")
        
        if os.path.exists(saly_19_path):
            saly_19_img = tk.PhotoImage(file=saly_19_path)
            saly_19_label = tk.Label(quiz_frame, image=saly_19_img, bg="#ffc8c0")
            saly_19_label.place(x=122, y=260)
            saly_19_label.image = saly_19_img
        else:
            print("Error: Saly-19.png not found")
        
        button_ds = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_ds_quiz)
        button_ds.place(x=195, y=635, width=180, height=50)
        button_math = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_math_quiz)
        button_math.place(x=659, y=635, width=180, height=50)
        button_physic = tk.Button(quiz_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_physic_quiz)
        button_physic.place(x=1123, y=635, width=180, height=50)

    # Call to show the quiz selection screen
    quiz_selection_screen()

    # Start the tkinter main loop
    root.mainloop()
