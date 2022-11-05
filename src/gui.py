from tkinter import *

root = Tk()
#title
root.title("Face Recognition")
#dimension
root.geometry("900x700")


# create label
title = Label(root,
              text = "Face Recognition",
              font = ("Nunito", 36)).pack()
subtitle = Label(root,
                 text = "by teskenal",
                 font = ("Nunito", 20)).pack()
'''
names1 = Label(root,
                text = "13521059 Arleen Chrysantha Gunardi",
                font = ("Nunito", 11)).grid(row=2,column=0,sticky = 'e')
names2 = Label(root,
                text = "13521097 Shidqi Indy Izhari",
                font = ("Nunito", 11)).grid(row=2,column=1)
names3 = Label(root,
                text = "13521107 Jericho Russel Sebastian",
                font = ("Nunito", 11)).grid(row=2,column=2,sticky = 'w')
'''
#title.pack()
#subtitle.pack()
#names1.pack()
#names2.pack()
#names3.pack()
#myLabel = Label(root,text="Face Recognition")
#myLabel.pack() #print to screen

#canvas = Canvas()
#canvas.create_line()

#CALL APP
#app = App(root)
root.mainloop()
