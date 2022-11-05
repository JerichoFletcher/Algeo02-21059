from tkinter import *
from tkinter import filedialog

def btn_clicked():
    print("Button Clicked")

def files():
    Tk.filename = filedialog.askopenfile()

def folders():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory()

window = Tk()

window.geometry("1100x600")
window.configure(bg = "#fffffa")
canvas = Canvas(
    window,
    bg = "#fffffa",
    height = 600,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = folders,
    relief = "flat")

b0.place(
    x = 97, y = 260,
    width = 85,
    height = 31)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = files,
    relief = "flat")

b1.place(
    x = 97, y = 385,
    width = 85,
    height = 31)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    550.0, 299.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()
