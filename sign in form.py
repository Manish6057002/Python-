








import tkinter as tk
import PIL
from PIL import Image, ImageTk
app=tk.Tk()
app.geometry("600x500")
app.title("Form")
app.config(bg="silver")
f1 = tk.Frame(app, bg="white").place(x=20, y=20, w=280, h=400)
f2 = tk.Frame(app, bg="green").place(x=300, y=20, w=280, h=400)
fb= Image.open("C:/Users/Students/Desktop/manjeet/fb.png")
ri1=fb.resize((30,30))
imgf= ImageTk.PhotoImage(ri1)
l1=tk.Label(f1, image=imgf, borderwidth=0).place(x=70, y=300)
g= Image.open("C:/Users/Students/Desktop/manjeet/g+.png")
ri2=g.resize((30,30))
imgg= ImageTk.PhotoImage(ri2)
l2=tk.Label(f1, image=imgg, borderwidth=0).place(x=130, y=300)
lk= Image.open("C:/Users/Students/Desktop/manjeet/li.png")
ri3=lk.resize((30,30))
imgl= ImageTk.PhotoImage(ri3)
l3=tk.Label(f1, image=imgl, borderwidth=0).place(x=190, y=300)
l4=tk.Label(f1, text="Signin", bg="white",font=("calibri",30, "bold")).place(x=120, y=30)
e1=tk.Entry(f1, bg="silver", borderwidth=0).place(x=35, y=90, w=250,h=40)
e1=tk.Entry(f1, bg="silver", borderwidth=0).place(x=35, y=150, w=250,h=40)
b=tk.Button(f1, bg="green", borderwidth=0, text="Signin",fg="white").place(x=35, y=210, w=250,h=50)
l5=tk.Label(f1, text="or Signin with", bg="white",borderwidth=0).place(x=120, y=270)
l5=tk.Label(f2, text="Welcome back!", bg="green", fg="white", borderwidth=0).place(x=400, y=90)
l5=tk.Label(f2, text="Welcome back! We are so happy to have you\n here. It's great to see you again. We hope you\n had a safe and enjoyable time away.", bg="green",  fg="white",borderwidth=0).place(x=320, y=130)
l5=tk.Label(f2, text="No account yet? Signup", bg="green", fg="white",borderwidth=1).place(x=380, y=210)
