import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
root = tk.Tk()
menubar = tk.Menu(root)
root.geometry('500x500')
root.title("shantanu")
root.iconbitmap("C:/Users/Students/Downloads/notepad_37173.ico")
root.config(menu=menubar)
def about():
    messagebox.showinfo("Noteapd", "version 1.2.33")
def close():
    root.destroy()

file = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New")
file.add_command(label="open")
file.add_command(label="save as..")
file.add_command(label="close", command=close)


edit =tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
form = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format",menu=form)
form.add_command(label="word Wrap")
form.add_command(label="font")
h = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=h)
h.add_command(label="view Help", command=about)




textarea = tk.Text(root, height=150, width=185).pack()
root.mainloop()

