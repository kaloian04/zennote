from tkinter import *

root = Tk()
root.geometry("1024x768")
root.title("Zennote")

frame = Frame(root)
frame.pack()

def save():
    file = open("notes.plain", "w")
    file.write(editor.get("1.0",'end-1c'))
    file.close()

def exit():
    root.destroy()

menubar = Menu(frame)
menubar.add_command(label = "Save", command=save)
menubar.add_command(label = "Exit", command=exit)

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

root.bind('<Control-s>', lambda x: save())

with open('notes.plain') as f:
    lines = f.read()

editor.insert("1.0", lines)

editor.pack()

root.config(menu = menubar)

root.mainloop()
