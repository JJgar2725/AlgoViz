# Jaime Garcia, Rodrigo Palacios, Isaac Valdez
# 10/12/2020
# AlgoViz
# Description:
# This program is meant to visually show the speed at which sorting algorithms operate at.
# In the program the user will be able to select from a variety of sorting algorithms and test their speeds!
# Users will also get detailed information about each algorithm and how it operates

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *


# BUTTON EVENTS
def bubble_page(event):
    pass


def insertion_page(event):
    pass


def merge_page(event):
    pass


# CONSTANTS
WIN_RES = 600
GRAY = '#C0C0C0'

# WINDOW SETTINGS
w = tk.Tk()
w.title("AlgoViz")
w.configure(bg=GRAY)
width = w.winfo_screenwidth()
height = w.winfo_screenheight()

windowWidth = int(width / 2) - int((WIN_RES + 150) / 2)
windowHeight = int(height / 2) - int(WIN_RES / 2)
w.geometry(f"{WIN_RES + 150}x{WIN_RES}+{windowWidth}+{windowHeight}")

# FONTS
fontStyle1 = tkFont.Font(family="Lucida Grande", size=30)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=18)
fontStyle3 = tkFont.Font(family="Lucida Grande", size=15)

# USER INTERFACE
f = Frame(w, background=GRAY)
title = tk.Label(f, text="AlgoViz", background=GRAY, font=fontStyle1)
# title.place(x=300, y=200)

selection = tk.Label(f, text="Algorithms", background=GRAY, font=fontStyle2)
# selection.place(x=310, y=275)

bubble_button = tk.Button(f, text="Bubble Sort", borderwidth=1,
                          width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3)
# bubble_button.place(x=150, y=325)
bubble_button.bind("<Button 1>", bubble_page)

insertion_button = tk.Button(f, text="Insertion Sort", borderwidth=1,
                             width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3)
# insertion_button.place(x=300, y=325)
insertion_button.bind("<Button 1>", insertion_page)

merge_button = tk.Button(f, text="Merge Sort", borderwidth=1,
                         width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3)
# merge_button.place(x=450, y=325)
merge_button.bind("<Button 1>", merge_page)

title.grid(row=0, column=1)
selection.grid(row=1, column=1)
bubble_button.grid(row=2, column=0, padx=5, pady=5)
insertion_button.grid(row=2, column=1, padx=5, pady=5)
merge_button.grid(row=2, column=2, padx=5, pady=5)

f.pack(expand=True)
w.mainloop()
