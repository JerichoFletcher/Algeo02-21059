from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import util.processimage as process
import numpy as np


def init_window():
    window = Tk()
    def folders():
        root = Tk()
        root.withdraw()
        folder = filedialog.askdirectory() 
        folder_only = os.path.basename(folder)
        canvas.itemconfig(no_folder_default ,text = folder_only)
        array_image = np.array([])
        for matrix in baca_folder(folder):
            np.append(array_image,matrix)
        print(len(array_image))    

    def files():
        filename = filedialog.askopenfilename()
        head, tail = os.path.split(filename)
        canvas.itemconfig(no_file_default, text = tail) 
        imeg = Image.open(filename)
        resized = imeg.resize((256,256), Image.ANTIALIAS)
        new = ImageTk.PhotoImage(resized)

        # Place in frame
        inplabel.configure(image = new)
        inplabel.image = new

        #display_gambar = canvas.create_image(540,349,image=new)
        #display_gambar.tkraise()

    def baca_folder(folder):
        for _files in os.listdir(folder):
            files = os.path.join(folder, _files)
            if(os.path.isfile(files)):
                img = process.resizeImg(files)
                img = process.RGBtoGrayscale(img)
                matrix = process.imgToMatrix(img)
                yield matrix
            else:
                yield baca_folder(files)
                
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

    # Image display frame
    imgframe = Frame(window, width=1100, height=600)
    imgframe.pack()
    imgframe.place(anchor="center", relx=540./1100., rely=349./600.)

    inplabel = Label(imgframe, image=None)
    inplabel.pack()

    no_folder_default = canvas.create_text(190,275, text="No folder selected", fill="black", justify="left", anchor="w")
    no_file_default = canvas.create_text(190,400, text="No file selected", fill="black",justify="left",anchor="w")


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