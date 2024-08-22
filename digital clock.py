import tkinter as tk
import time
def clock():
    
    ct = time.strftime("%H:%M:%S")
    output.set(ct)
    root.after(1000,clock)
root = tk.Tk()
root.geometry('800x200')
root.config(bg = "black")
root.title("DIGITAL CLOCK")
root.resizable(0,0)
output = tk.StringVar()
l1 = tk.Label(root, textvariable = output, font = ('digital-7',180,'bold'), bg = "black", fg = "lime").pack()
clock()
root.mainloop()
