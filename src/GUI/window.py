from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import util.processimage as process
from util.eigenface import eigenface
import numpy as np
import util.benchmark as bm

MAX_PIC_COUNT = 5

# Deklarasi
# array_image = []
inplabel = None
array_of_tupl = []

def init_window():
    window = Tk()
    def folders():
        root = Tk()
        root.withdraw()
        folder = filedialog.askdirectory() 
        folder_only = os.path.basename(folder)
        canvas.itemconfig(no_folder_default ,text = folder_only)

        # Load image in folder
        array_of_tupl.clear()
        for f, m in baca_folder(folder):
            array_of_tupl.append((f, m))
        """ array_image.clear()
        for matrix in baca_folder(folder):
            array_image.append(matrix)
        
        print(f"{len(array_of_tupl)} pictures loaded, first element:")
        mattest = np.array(array_of_tupl[0][1])
        print(f"Size: {mattest.shape}")
        print(array_of_tupl[0])
        """
        array_of_matrix = []
        for t in array_of_tupl:
            array_of_matrix.append(t[1])

        eigenface(array_of_matrix)

        # Hitung eigenface
        #t0, t1 = bm.run_measure_ns(lambda: eigenface(array_of_tupl))
        #print(f"Finished eigenface extraction in {(t1-t0)/1E9} seconds")

        #"""

    def files():
        global inplabel

        filename = filedialog.askopenfilename()
        head, tail = os.path.split(filename)
        canvas.itemconfig(no_file_default, text = tail)

        # Load image
        imeg = Image.open(filename)
        resized = imeg.resize((256,256), Image.ANTIALIAS)
        new = ImageTk.PhotoImage(resized)

        # Place in frame
        if inplabel is not None:
            inplabel.destroy()
        inplabel = Label(imgdatframe)
        inplabel.pack()
        inplabel.configure(image = new)
        inplabel.image = new
        imgdatframe.tkraise()

        #display_gambar = canvas.create_image(540,349,image=new)
        #display_gambar.tkraise()

    def baca_folder(folder):
        '''
        i = 0
        c = 0
        _dirs = os.listdir(folder)
        while c < MAX_PIC_COUNT and i < len(_dirs):
            _file = _dirs[i]
            filepath = os.path.join(folder, _file)
            if(os.path.isfile(filepath)):
                c += 1
                matrix = process.loadImg(filepath)
                #head, tail = os.path.split(files)
                yield _file, matrix
            else:
                for t, m in baca_folder(filepath):
                    yield t, m
            i += 1
        '''

        #'''
        i = 0
        for _files in os.listdir(folder):
            if i >= MAX_PIC_COUNT: break
            filepath = os.path.join(folder, _files)
            if(os.path.isfile(filepath)):
                i += 1
                matrix = process.loadImg(filepath)
                #head, tail = os.path.split(filepath)
                yield _files, matrix
            else:
                for t, m in baca_folder(filepath):
                    yield t, m
        #'''
                
    window.geometry("1100x600")
    window.configure(bg = "#fffffa")

    # FRAME CONSTRUCTION
    # Background frame
    #bgiframe = Frame(window, width=1100, height=600)
    #bgiframe.pack()
    #bgiframe.place(anchor="center", relx=.5, rely=.5)
    #bgiframe.tkraise()

    # Image display frame
    imgdatframe = Frame(window, width=1100, height=600)
    imgdatframe.pack()
    imgdatframe.place(anchor="center", relx=540./1100., rely=349./600.)

    #inplabel = Label(imgdatframe)
    #inplabel.pack()

    canvas = Canvas(
        window,
        bg = "#fffffa",
        height = 600,
        width = 1100,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

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
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    window.mainloop()
