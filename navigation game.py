import tkinter as tk
import tkinter.messagebox

def gotem():
    tkinter.messagebox.showinfo("You are an idiot.",  "HAHAHAHA! ")    
    tkinter.messagebox.showinfo("You are an idiot.",  "this is not the start of the game!  ")
def winner():
    tkinter.messagebox.showinfo("'insert happy music'", "you won! (this game isnt finished yet)")

#root = Tk(screenName=None, baseName=None, className='Tk', useTk=1)
w=tk.Tk()
w.geometry("640x480")
w.title("adventure game (stub)")
y="Start"
label = tk.Label(text=" a stupid adventure game. navigate to the end!(not yet complete)")
label.pack()
button = tk.Button(w, text=y, width=30,height=4,command=gotem)
winnerbutton = tk.Button(w, text="close game", width=10,command=winner)

winnerbutton.pack(side=tk.BOTTOM)
button.pack()
w.mainloop() 
