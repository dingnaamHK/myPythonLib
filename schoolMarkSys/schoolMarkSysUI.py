from schoolMarkSys import studentInfo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import time

classObj = studentInfo()
def addClass():
    cls = iptClass.get()
    classObj.setClass(cls)
    showRecentTeaching(cls)

def showRecentTeaching(cls):
    messagebox.showinfo(title="Message", message=f"{cls} is added to teaching list!")

def reset():
    classObj.reset("data/classes.txt")
    classObj.reset("data/students.txt")

def clearEntryClass():
    iptClass.delete(0, END)


root = Tk()
root.title = "School Mark System"
root.geometry("600x1000")

title = ttk.Label(text="School Mark System", font="Arial, 30")
title.grid(column=0, row=0)

iptClassLbl = tk.Label(text="Class Name")
iptClassLbl.grid(column=0, row=1)

iptClass  = tk.Entry()
iptClass.grid(column=1, row=1)


iptClassBtn = tk.Button(text="Create Class", command=lambda:[addClass(), clearEntryClass()])
iptClassBtn.grid(column=2, row=1)

showClass = tk.Label(text=f"Currently Teaching: ")
showClass.grid(column=1, row=2)



showClassVal = tk.Label()
showClassVal.grid(column=3, row=2)

showClassVal.config(text=classObj.recentlyTeaching())
print(classObj.recentlyTeaching())


resetBtn = tk.Button(text="Reset (REMOvE when Pulish)", command=reset)
resetBtn.grid(column=4, row=4)





root.mainloop()
