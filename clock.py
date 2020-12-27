from tkinter import *
from tkinter. ttk import*

from time import strftime

r = Tk()
r.title("Time")
def time_display():
    s = strftime('%I : %M : %S %p ')
    l.config(text=s)
    l.after(1000,time_display)


if __name__=="__main__":
    l = Label(r,font=("DS-Digital Bold",50,'bold'), background = "Black" , foreground= 'Red')
    l.pack(anchor="n")
    time_display()




