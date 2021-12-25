# imports
from tkinter import *
import os

# function to save the file
def save():
    file = open("./notes/notes.plain", "w")
    file.write(editor.get("1.0",'end-1c'))
    file.close()

# function to quit the programm
def exit():
    with open('./notes/notes.plain') as f:
        contents = f.read()
    if contents == editor.get("1.0",'end-1c'):
        root.destroy()
    elif contents != editor.get("1.0",'end-1c'):
        unsaved_warning()

# creating the save and exit function
def save_and_exit():
    save()
    root.destroy()

# quit anyway function
def quit_anyway():
    root.destroy()

# function that checks for changes in the file
def check_for_changes():
    with open('./notes/notes.plain') as f:
        contents = f.read()
    if contents == editor.get("1.0",'end-1c'):
        root.title("Zennote")
    elif contents != editor.get("1.0",'end-1c'):
        root.title("*Zennote")
    root.after(100, check_for_changes)

# creating the warning function
def unsaved_warning():
    warning = Toplevel(root)
    warning.geometry("300x100")
    warning.title("Unsaved changes!")
    text = Label(warning, text="Unsaved changes!")
    text.pack()
    button_save_and_exit = Button(warning,
                                  text="Save and exit?",
                                  command=save_and_exit)
    button_save_and_exit.pack()
    button_quit_anyway = Button(warning,
                                text = "Quit anyway!",
                                command=quit_anyway)
    button_quit_anyway.pack()
# creating the notes.plain file if it does not exist
if os.path.exists('./notes/notes.plain') == False:
    os.mkdir("./notes")
    with open('./notes/notes.plain', 'w') as f:
        pass

# creating the root window
root = Tk()
root.geometry("1024x768")
root.title("Zennote")
frame = Frame(root)
frame.pack()

# creating the menubar
menubar = Menu(frame)
menubar.add_command(label = "Save", command=save)
menubar.add_command(label = "Exit", command=exit)
root.config(menu = menubar)

# creating the main text editor widget
font = ("Consolas", 13)
editor = Text(frame,
              bg="#282a36",
              fg="#f8f8f2",
              insertbackground="#f8f8f2",
              padx=2,
              pady=2,
              insertofftime=0,
              width=1000,
              height=1000,
              font = font)
with open('./notes/notes.plain') as f:
    contents = f.read()
editor.insert("1.0", contents)
editor.pack()

# executing the check_for_changes() function
check_for_changes()

# creating the key bindings
root.bind('<Control-s>', lambda x: save())
root.bind('<Control-q>', lambda x: exit())

# the mainloop method
root.mainloop()
