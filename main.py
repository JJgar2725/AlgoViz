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


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        main = tk.Frame(self, background=GRAY)

        # FONTS
        fontStyle1 = tkFont.Font(family="Lucida Grande", size=30)
        fontStyle2 = tkFont.Font(family="Lucida Grande", size=18)
        fontStyle3 = tkFont.Font(family="Lucida Grande", size=15)

        # USER INTERFACE
        title = tk.Label(main, text="AlgoViz", background=GRAY, font=fontStyle1)

        selection = tk.Label(main, text="Algorithms", background=GRAY, font=fontStyle2)

        bubble_button = tk.Button(main, text="Bubble Sort", borderwidth=1, width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3)
        bubble_button.bind("<Button-1>", bubble_page)

        insertion_button = tk.Button(main, text="Insertion Sort", borderwidth=1, width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3)
        insertion_button.bind("<Button-1>", insertion_page)

        merge_button = tk.Button(main, text="Merge Sort", borderwidth=1, width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3)
        merge_button.bind("<Button-1>", merge_page)

        title.grid(row=0, column=1)
        selection.grid(row=1, column=1)
        bubble_button.grid(row=2, column=0, padx=5, pady=5)
        insertion_button.grid(row=2, column=1, padx=5, pady=5)
        merge_button.grid(row=2, column=2, padx=5, pady=5)

        main.pack(expand=True)


# BUTTON EVENTS
def bubble_page(event):
    bubble_w = tk.Tk()
    bubble_w.configure(bg=GRAY)
    width = bubble_w.winfo_screenwidth()
    height = bubble_w.winfo_screenheight()
    windowWidth = int(width / 2) - int((WIN_RES + 150) / 2)
    windowHeight = int(height / 2) - int(WIN_RES / 2)
    bubble_w.geometry(f"{WIN_RES + 150}x{WIN_RES}+{windowWidth}+{windowHeight}")
    bubble_w.wm_title("Great!")
    label = tk.Label(bubble_w, text="Awesome! You're good to go!")
    label.pack()
    okay_button = tk.Button(bubble_w, text="Okay", command=bubble_w.destroy)
    okay_button.pack()
    bubble_w.mainloop()
    print("Bubble Sort Page")


def insertion_page(event):
    print("Insertion Sort Page")


def merge_page(event):
    print("Merge Sort Page")


# CONSTANTS
WIN_RES = 600
GRAY = '#C0C0C0'

if __name__ == "__main__":

    # WINDOW SETTINGS
    w = tk.Tk()
    w.title("AlgoViz")
    w.configure(bg=GRAY)
    width = w.winfo_screenwidth()
    height = w.winfo_screenheight()

    windowWidth = int(width / 2) - int((WIN_RES + 150) / 2)
    windowHeight = int(height / 2) - int(WIN_RES / 2)
    w.geometry(f"{WIN_RES + 150}x{WIN_RES}+{windowWidth}+{windowHeight}")

    # MAIN PAGE INSTANTIATION
    root = MainView(w)
    root.pack(expand=True)
    w.mainloop()
