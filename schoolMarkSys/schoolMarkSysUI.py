from schoolMarkSys import studentInfo
from tkinter import *
from tkinter import ttk
import tkinter as tk

classObj = studentInfo()
def addClass():
    cls = iptClass.get()
    classObj.setClass(cls)
    print(cls)

def reset():
    classObj.reset("data/classes.txt")
    classObj.reset("data/students.txt")

root = Tk()
root.title = "School Mark System"
root.geometry("600x1000")

title = ttk.Label(text="School Mark System", font="Arial, 30")
title.grid(column=0, row=0)

iptClassLbl = tk.Label(text="Class Name")
iptClassLbl.grid(column=0, row=1)

iptClass  = tk.Entry()
iptClass.grid(column=1, row=1)

iptClassBtn = tk.Button(text="Create Class", command=addClass)
iptClassBtn .grid(column=2, row=1)

resetBtn = tk.Button(text="Reset (REMOvE when Pulish)", command=reset)
resetBtn.grid(column=4, row=4)





root.mainloop()
