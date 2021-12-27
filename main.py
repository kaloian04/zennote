import os
from tkinter import *
from tkinter import filedialog

FONT = ("Consolas", 13)
TITLE = "Zennote"
RESOLUTION = "1024x768"
BACKGROUND = "#282a36"
FOREGROUND = "#f8f8f2"


def open_file():
    if editor.get("1.0", END) == "":
        open_file.file_loc = filedialog.askopenfilename()
        with open(open_file.file_loc) as f:
            contents = f.read()
        editor.insert("1.0", contents)
        editor.pack()
        check_for_changes()
    else:
        open_file.file_loc = filedialog.askopenfilename()
        with open(open_file.file_loc) as f:
            contents = f.read()
        editor.delete("1.0", END)
        editor.insert("1.0", contents)
        editor.pack()
        check_for_changes()


def save():
    try:
        file = open(open_file.file_loc, "w")
        file.write(editor.get("1.0", END))
        file.close()
    except:
        pass


def save_as():
    file = filedialog.asksaveasfile()
    file.write(editor.get("1.0", END))
    file.close()
    open_file()


def create_new_file():
    editor.pack()
    editor.delete("1.0", END)


def exit():
    try:
        with open(open_file.file_loc) as f:
            contents = f.read()
        if contents == editor.get("1.0", END):
            root.destroy()
        elif contents != editor.get("1.0", END):
            unsaved_warning()
    except:
        root.destroy()


def save_and_exit():
    save()
    root.destroy()


def quit_anyway():
    root.destroy()


def check_for_changes():
    with open(open_file.file_loc) as f:
        contents = f.read()
    if contents == editor.get("1.0", END):
        root.title("Zennote - " + open_file.file_loc)
    elif contents != editor.get("1.0", END):
        root.title("*Zennote - " + open_file.file_loc)
    root.after(100, check_for_changes)


def unsaved_warning():
    warning = Toplevel(root)
    warning.geometry("300x100")
    warning.title("Unsaved changes!")
    text = Label(warning, text="Unsaved changes!")
    text.pack()
    button_save_and_exit = Button(warning, text="Save and exit?", command=save_and_exit)
    button_save_and_exit.pack()
    button_quit_anyway = Button(warning, text="Quit anyway!", command=quit_anyway)
    button_quit_anyway.pack()


root = Tk()
root.geometry(RESOLUTION)
root.title(TITLE)
frame = Frame(root)
frame.pack()

menubar = Menu(frame)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Create New", command=create_new_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=save_as)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Exit", command=exit)
root.config(menu=menubar)

editor = Text(
    frame,
    bg=BACKGROUND,
    fg=FOREGROUND,
    insertbackground=FOREGROUND,
    padx=2,
    pady=2,
    insertofftime=0,
    width=1000,
    height=1000,
    font=FONT,
)

root.bind("<Control-o>", lambda x: open_file())
root.bind("<Control-s>", lambda x: save())
root.bind("<Control-S>", lambda x: save_as())
root.bind("<Control-q>", lambda x: exit())
root.bind("<Control-n>", lambda x: create_new_file())

root.mainloop()
