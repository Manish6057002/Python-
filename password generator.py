import random
import tkinter as tk
import PIL
from PIL import Image,ImageTk
app=tk.Tk()
app.geometry('400x150')
app.config(bg="lightblue")
app.title("Random Password Generator")
image=Image.open("C:/Users/Students/Desktop/manjeet/password.png")
ri=image.resize((20,20))
img=ImageTk.PhotoImage(ri)
i1=tk.Label(app,image=img).place(x=20,y=10)
output=tk.StringVar()

def generate_password():
          password = int(p.get())
          pw = ""
          characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_+"
          for i in range(1, password+1):
                    pw= pw+ random.choice(characters)
          output.set(pw)
        
l1=tk.Label(app,text="Random Password Generator",font=("Calibri",15,"bold"),bg="lightblue",fg="black").place(x=90,y=5)
frame=tk.Frame(app,bg="white").place(x=10,y=40,h=100,w=380)
l2=tk.Label(app,text="Password",font=("calibri",10,"bold"),bg="white",fg="black").place(x=20,y=50)
p=tk.StringVar()
e1=tk.Entry(app,font=("calibri",10,"bold"),bg="lightblue", textvariable = output).place(x=80,y=50,h=20,w=100)
b1=tk.Button(app,text="Copy",font=("Calibri",10,"bold"),bg="white",fg="black").place(x=200,y=50,h=20,w=80)
b2=tk.Button(app,text="Generate",font=("calibri",10,"bold"),bg="white",fg="black", command=generate_password).place(x=300,y=50,h=20,w=80)
l3=tk.Label(app,text="Length",font=("calibri",10,"bold"),bg="white",fg="Black").place(x=20,y=100)
e2=tk.Entry(app,font=("calibri",10,"bold"),bg="lightblue",textvariable=p).place(x=80,y=100,h=20,w=100)

