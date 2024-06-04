import tkinter as tk
from tkinter import font
import os


def open_ds_link():
    import webbrowser
    webbrowser.open_new("https://www.example.com/digital_system")

def open_math_link():
    import webbrowser
    webbrowser.open_new("https://www.example.com/mathematics")

def open_physic_link():
    import webbrowser
    webbrowser.open_new("https://www.example.com/physics")


def apply_widget_style(widget, bg, width, height, x, y):
    widget.place(x=x, y=y, width=width, height=height)
    widget.config(bg=bg, bd=4, relief='solid')


root = tk.Tk()
root.title("Quebiz Section")
root.geometry("1400x900")  

comic_sans_font = font.Font(family='Comic Sans MS', size=40)
stylish_font = font.Font(family='Stylish', size=20)
zen_dots_font = font.Font(family='Zen Dots', size=20)

main_frame = tk.Frame(root, bg="#d1eaf0")
main_frame.place(relwidth=1, relheight=1)

quebiz_section = tk.Label(main_frame, text="QUEBIZ SECTION", font=comic_sans_font, bg="#d1eaf0")

x_position = 500  
y_position = 51   
quebiz_section.place(x=x_position, y=y_position)


physic1 = tk.Frame(main_frame)
apply_widget_style(physic1, "#ffc8c0", 378, 532, 94, 203)

physic2 = tk.Frame(main_frame)
apply_widget_style(physic2, "#ffc8c0", 378, 532, 558, 203)

physic3 = tk.Frame(main_frame)
apply_widget_style(physic3, "#ffc8c0", 378, 532, 1022, 203)

digital_system_label = tk.Label(main_frame, text="DIGITAL SYSTEM", font=stylish_font, bg="#ffc8c0", fg="#000")
digital_system_label.place(x=144, y=222)

mathematics_label = tk.Label(main_frame, text="MATHEMATICS", font=stylish_font, bg="#ffc8c0", fg="#000")
mathematics_label.place(x=624, y=222)

physic_label = tk.Label(main_frame, text="PHYSIC", font=stylish_font, bg="#ffc8c0", fg="#000")
physic_label.place(x=1150, y=222)

current_dir = os.path.dirname(os.path.abspath(__file__))

saly_16_img = tk.PhotoImage(file=os.path.join(current_dir, "Saly-16.png"))
saly_16_img = saly_16_img.subsample(2, 2)  

saly_10_img = tk.PhotoImage(file=os.path.join(current_dir, "Saly-10.png"))
saly_19_img = tk.PhotoImage(file=os.path.join(current_dir, "Saly-19.png"))

saly_16_label = tk.Label(main_frame, image=saly_16_img, bg="#FFC8C0")
saly_16_label.place(x=1064, y=270) 
saly_16_label.image = saly_16_img 

saly_10_label = tk.Label(main_frame, image=saly_10_img, bg="#FFC8C0")
saly_10_label.place(x=578, y=272)

saly_19_label = tk.Label(main_frame, image=saly_19_img, bg="#FFC8C0")
saly_19_label.place(x=122, y=260)

button_ds = tk.Button(main_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_ds_link)
button_ds.place(x=195, y=635, width=180, height=50)

button_math = tk.Button(main_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_math_link)
button_math.place(x=659, y=635, width=180, height=50)

button_physic = tk.Button(main_frame, text="START", font=zen_dots_font, bg="#d1eaf0", command=open_physic_link)
button_physic.place(x=1123, y=635, width=180, height=50)

root.mainloop()










