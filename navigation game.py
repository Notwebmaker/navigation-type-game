from tkinter import*
from tkinter.ttk import*
import tkinter.messagebox

def gotem():
    tkinter.messagebox.showinfo("You are an idiot.",  "HAHAHAHA! ")    
    tkinter.messagebox.showinfo("You are an idiot.",  "this is not the start of the game!  ")

def youwin():
    tkinter.messagebox.showinfo("congratulations","You won!(this was easy right?)")
    w.destroy()

w = Tk()
w.geometry("640x480")  
w.title("stupid navigation game")

def nextchallange1():
    tkinter.messagebox.showinfo("'insert happy music'", "next challange( is very simple)")
    lvl1 = Toplevel(w)
    lvl1.title("Challange 1")
    lvl1.geometry("640x480")  
    Label(lvl1, text="At least 1 button is lying, at least 1 speaks the truth").pack(pady=20)
    Button(lvl1, text="you win if you click this button",command= w.destroy).pack(pady=20)
    button2= Button(lvl1, text="the first button is lying, it is me", command=youwin).pack(pady=30)
    wisebutton=Button(lvl1, text="i speak the truth, and i tell you one of the other two is lying, ", command=w.destroy).pack(pady=40)

Label(w, text="A stupid adventure game, navigate to the end!").pack(pady=10)
Button(w, text="Start",width=32, command=gotem).pack(side=TOP,pady=30)
Button(w, text="close game", command=nextchallange1).pack(side=BOTTOM)


# Run the Tkinter event loop
w.mainloop()
