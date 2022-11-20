from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import util.processimage as process
from util.eigenface import eigenface, testImage
import numpy as np
import util.benchmark as bm
import time

MAX_PIC_COUNT = 5

# Deklarasi
# array_image = []
inplabel = None
outlabel = None
array_of_inp = []
array_of_out = []
cek_eigenface = False
matrix_image = None
index_result = None

def init_window():
    window = Tk()
    def folders():
        global cek_eigenface, matrix_image, index_result
        root = Tk()
        root.withdraw()
        folder = filedialog.askdirectory() 
        folder_only = os.path.basename(folder)
        canvas.itemconfig(no_folder_default ,text = folder_only)

        # Load image in folder
        array_of_inp.clear()
        array_of_out.clear()

        for f, m in baca_folder(folder):
            array_of_inp.append((f, m))

        
        """ array_image.clear()
        for matrix in baca_folder(folder):
            array_image.append(matrix)
        
        print(f"{len(array_of_tupl)} pictures loaded, first element:")
        mattest = np.array(array_of_tupl[0][1])
        print(f"Size: {mattest.shape}")
        print(array_of_tupl[0])
        """

        array_of_matrix = []
        #array_of_eigface = []
        for t in array_of_inp:
            array_of_matrix.append(t[1])

        def getEigface():
            eigenface(array_of_matrix)

        # Hitung eigenface
        t0, t1 = bm.run_measure_ns(getEigface)
        print(f"Finished eigenface extraction in {(t1-t0)/1E9} seconds")

        #for i in range(len(array_of_eigface)):
        #    array_of_eigface.append((array_of_inp[i][0], array_of_eigface[i]))

        cek_eigenface = True

        if matrix_image is not None:
            index_result = testImage(matrix_image)
            display_hasil()
            
    def files():
        global inplabel, matrix_image, index_result

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
        inplabel = Label(imginpframe)
        inplabel.pack()
        inplabel.configure(image = new)
        inplabel.image = new
        imginpframe.tkraise()

        matrix_image = process.loadImg(filename)

        if cek_eigenface:
            def getTestImage():
                global index_result, matrix_image
                index_result = testImage(matrix_image)

            t0, t1 = bm.run_measure_ns(getTestImage)
            print(f"Finished testface comparison in {(t1-t0)/1E9} seconds")

            display_hasil()

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
                yield filepath, matrix
            else:
                for t, m in baca_folder(filepath):
                    yield t, m
        #'''
                

    def display_hasil():
        global outlabel, index_result, array_of_inp

        filename, _ = array_of_inp[index_result]

        # Load image
        imeg = Image.open(filename)
        resized = imeg.resize((256,256), Image.ANTIALIAS)
        new = ImageTk.PhotoImage(resized)

        # Place in frame
        if outlabel is not None:
            outlabel.destroy()
        outlabel = Label(imgoutframe)
        outlabel.pack()
        outlabel.configure(image = new)
        outlabel.image = new
        imgoutframe.tkraise()


    window.geometry("1100x600")
    window.configure(bg = "#fffffa")

    # FRAME CONSTRUCTION
    # Background frame
    #bgiframe = Frame(window, width=1100, height=600)
    #bgiframe.pack()
    #bgiframe.place(anchor="center", relx=.5, rely=.5)
    #bgiframe.tkraise()

    # Image display frame
    imginpframe = Frame(window, width=1100, height=600)
    imginpframe.pack()
    imginpframe.place(anchor="center", relx=540./1100., rely=349./600.)

    # Image output frame
    imgoutframe = Frame(window, width=1100, height=600)
    imgoutframe.pack()
    imgoutframe.place(anchor="center", relx=887./1100., rely=349./600.)

    #inplabel = Label(imginpframe)
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
    execution_time = canvas.create_text(540,518, text="", fill="black",justify="left",anchor="w", font=('IBM Plex Serif','13'))

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
