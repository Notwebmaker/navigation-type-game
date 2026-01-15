from tkinter import*
from tkinter.ttk import*
from gamedata import*
import tkinter.messagebox
#created by notwebmaker, 
def gotem():
    tkinter.messagebox.showinfo("You are an idiot.",  "HAHAHAHA! ")    
    tkinter.messagebox.showinfo("You are an idiot.",  "this is not the start of the game!  ")

def youwin():
    tkinter.messagebox.showinfo("congratulations","You won!(this was easy right?)")
    w.destroy()

def tip1():
    w.destroy()
    tkinter.messagebox.showinfo("Tip","Just because it says the truth does not mean it is the correct answer")

#test()
w = Tk()
w.geometry("640x480")  
w.title("stupid quiz type game")

lives = 4
#below is to make the lvl(x) variables global, so that the next level automatically closes the previous
lvl1 = 0
lvl2 = 0
lvl3 = 0
lvl4 = 0
lvl5 = 0
def incorrect():
    global lives
    lifechecksum()
    lives-=1
    tkinter.messagebox.showinfo("WRONG","-1 life")
def addlife():#currently unused 
    global lives
    tkinter.messagebox.showinfo("NICE ONE","+1 life")
    lives+=1
def lifechecksum():
    global lives
    print("you have "+str(lives)+" lives left")
    if lives <= 0:
        w.destroy()
        tkinter.messagebox.showinfo("GAME OVER","Game over")
def nextchallenge1():
    global lvl1,lives
    tkinter.messagebox.showinfo("'insert happy music'", "next challange( is very simple)")
    lvl1 = Toplevel(w)
    lvl1.title("Challenge 1")
    lvl1.geometry("640x480")  
    Label(lvl1, text="At least 1 button is lying, at least 1 speaks the truth. Only ONE lets you pass").pack(pady=20)
    Button(lvl1, text="you win if you click me",command=incorrect).pack(pady=20)
    button2= Button(lvl1, text="the first button is lying, it is me who will let you win", command=nextchallenge2).pack(pady=30)
    wisebutton=Button(lvl1, text="I dont let you win but i can tell you that one of the other two is lying, ", command=tip1).pack(pady=40)
def nextchallenge2():
    global lvl1, lvl2, lives
    lvl1.destroy()    
    tkinter.messagebox.showinfo("'insert happy music'", "next challange( is also very VERY simple)")
    lvl2 = Toplevel(w)
    lvl2.title("Challenge 2")
    lvl2.geometry("640x480")  
    Label(lvl2, text="just click this, no catches, trust").pack(pady=20)
    Button(lvl2, text="you progress if you click this button",command=nextchallenge3).pack(pady=20)
def nextchallenge3():
    global lvl2, lvl3,lives
    lvl2.destroy()
    lvl3 = Toplevel(w)
    lvl3.geometry("640x480")
    lvl3.title("Challenge 3")

    print("sanity check")
    Label(lvl3, text= "hmm if only you can reveal more of the window ").pack(side=TOP,pady=10)

    for sane in range (0, 12):
        print(sane)
        Label(lvl3, text= "You will never find the hidden button HAHAHAHA " ).pack(pady=10)
    Button(lvl3, text="oh shoot",command=nextchallange4).pack(pady=0)
    
def nextchallange4():
    global lvl3, lvl4,lives
    lifechecksum()
    lvl3.destroy()
    lvl4=Toplevel(w)
    quiz1=IntVar()
    Label (lvl4,text = "witch is the better graphics card?(in perfromance)").pack(pady=1)
    Radiobutton(lvl4,text = "GTX 1080",variable=quiz1,value=1).pack(anchor=W)
    Radiobutton(lvl4,text = "8800 GTX",variable=quiz1,value=2).pack(anchor=W)
    #Button(lvl4,text="ok since i havent coded this yet here is win button",command=youwin).pack(pady=1)
    def selected():
        if quiz1.get() == 1:
            nextchallange5()
        elif quiz1.get() == 2:
            incorrect()

    Button(lvl4, text='Choose', command=selected).pack(pady=2)


def nextchallange5():
    global lvl4, lvl5,lives
    lifechecksum()
    lvl4.destroy()
    lvl5=Toplevel(w)
    lvl5.geometry('1920x1080')
    print("what tf")
    Button(lvl5, text='click here to continue', command=guigame1).pack(pady=2)
    Button(lvl5, text='alternativley click here for a chnace to gain a life!(does not work, do not click)', command=guigame1).pack(pady=2)



    
Label(w, text="A stupid adventure game, navigate to the end!").pack(pady=10)
Label(w, text="made by notwebmaker.").pack(pady=10)
Button(w, text="'Start'",width=32, command=gotem).pack(side=TOP,pady=30)
Button(w, text="real start", command=nextchallenge1).pack(side=BOTTOM)


w.mainloop()
