from tkinter import *
import os
import subprocess

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

root = Tk()
root.geometry("1024x768")

frame = Frame(root)
frame.pack()

#def new_file():


#def open_file(path):


def save():
    file = open("test.txt", "w")
    file.write(entry.get())
    file.close()

def exit():
    root.destroy()

menubar = Menu(frame)
#menubar.add_command(label = "New File", command=new_file)
#menubar.add_command(label = "Open File", command=open_file)
menubar.add_command(label = "Save", command=save)
#enubar.add_command(label = "Save As", command=save_as)
menubar.add_command(label = "Exit", command=exit)

entry = Entry(frame, width=100000)
entry.pack()

root.config(menu = menubar)

root.mainloop()
