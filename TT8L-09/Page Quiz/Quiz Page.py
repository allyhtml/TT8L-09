import tkinter as tk
from tkinter import font
import os


def open_ds_link():
    print("Opening Digital System page")
    
def open_math_link():
    print("Opening Mathematics page")
    
def open_physic_link():
    print("Opening Physics page")
    
def start_button_action():
    print("Button pressed!")
   


root = tk.Tk()
root.title("Quebiz Section")
root.geometry("1400x900")

comic_sans_font = font.Font(family='Comic Sans MS', size=40)
stylish_font = font.Font(family='Stylish', size=20)
zen_dots_font = font.Font(family='Zen Dots', size=20)

main_frame = tk.Frame(root, bg="#d1eaf0")
main_frame.place(relwidth=1, relheight=1)

quebiz_section = tk.Label(main_frame, text="QUEBIZ SECTION", font=comic_sans_font, bg="#d1eaf0")
quebiz_section.place(x=500, y=51)

physic1 = tk.Frame(main_frame, bg="#ffc8c0", width=378, height=532)
physic1.place(x=94, y=203)

physic2 = tk.Frame(main_frame, bg="#ffc8c0", width=378, height=532)
physic2.place(x=558, y=203)

physic3 = tk.Frame(main_frame, bg="#ffc8c0", width=378, height=532)
physic3.place(x=1022, y=203)

digital_system_label = tk.Label(main_frame, text="DIGITAL SYSTEM", font=stylish_font, bg="#ffc8c0", fg="#000")
digital_system_label.place(x=144, y=222)

mathematics_label = tk.Label(main_frame, text="MATHEMATICS", font=stylish_font, bg="#ffc8c0", fg="#000")
mathematics_label.place(x=624, y=222)

physic_label = tk.Label(main_frame, text="PHYSIC", font=stylish_font, bg="#ffc8c0", fg="#000")
physic_label.place(x=1150, y=222)

current_dir = os.path.dirname(os.path.abspath(__file__))

saly_16_img = tk.PhotoImage(file=os.path.join(current_dir, "Saly-16.png"))
saly_16_img = saly_16_img.subsample(1)

saly_10_img = tk.PhotoImage(file=os.path.join(current_dir, "Saly-10.png"))
saly_19_img = tk.PhotoImage(file=os.path.join(current_dir, "Saly-19.png"))

saly_16_label = tk.Label(main_frame, image=saly_16_img, bg="#FFC8C0")
saly_16_label.place(x=1064, y=260)
saly_16_label.image = saly_16_img

saly_10_label = tk.Label(main_frame, image=saly_10_img, bg="#FFC8C0")
saly_10_label.place(x=578, y=272)

saly_19_label = tk.Label(main_frame, image=saly_19_img, bg="#FFC8C0")
saly_19_label.place(x=122, y=260)

button_ds = tk.Button(main_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=start_button_action)
button_ds.place(x=195, y=635, width=180, height=50)

button_math = tk.Button(main_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=start_button_action)
button_math.place(x=659, y=635, width=180, height=50)

button_physic = tk.Button(main_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=start_button_action)
button_physic.place(x=1123, y=635, width=180, height=50)

root.mainloop()












