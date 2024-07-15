
# created on 15th Jul 2024

# @author: pengchao

import tkinter as tk

from tkinter import ttk

#create instance
win = tk.Tk()

win.title("Pengchao GUI")

#Adding a label
ttk.Label(win, text="pengchao's Label").grid(column=0, row=0)

#start the GUI App
win.mainloop()

