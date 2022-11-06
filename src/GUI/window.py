from tkinter import *
from tkinter import filedialog
import os

def btn_clicked():
    print("Button Clicked")

def init_window():
    window = Tk()
    def folders():
        root = Tk()
        root.withdraw()
        folder = filedialog.askdirectory() 
        folder_only = os.path.basename(folder)
        canvas.itemconfig(no_folder_default ,text = folder_only)

    def files():
        filename = filedialog.askopenfilename()
        head, tail = os.path.split(filename)
        file_only = head.split('/')
        canvas.itemconfig(no_file_default, text = tail) 

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

    no_folder_default = canvas.create_text(240,275, text="No folder selected", fill="black")
    no_file_default = canvas.create_text(235,400, text="No file selected", fill="black")

    img0 = PhotoImage(file = f"GUI/img0.png")
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

    img1 = PhotoImage(file = f"GUI/img1.png")
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

    background_img = PhotoImage(file = f"GUI/background.png")
    background = canvas.create_image(
        550.0, 299.5,
        image=background_img)

    window.resizable(False, False)
    window.title("Face Recognition")
    window.mainloop()