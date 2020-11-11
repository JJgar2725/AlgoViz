# Jaime Garcia, Rodrigo Palacios, Isaac Valdez
# 10/12/2020
# AlgoViz
# Description:
# This program is meant to visually show the speed at which sorting algorithms operate at.
# In the program the user will be able to select from a variety of sorting algorithms and test their speeds!
# Users will also get detailed information about each algorithm and how it operates

import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
from bubblesort import bubble_sort
import random

# CONSTANTS
WIN_RES = 600
GRAY = '#C0C0C0'
arr = random.sample(range(0, 100), 10)
count = 0


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
        bubble_button = tk.Button(main, text="Bubble Sort", borderwidth=1, width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3, command=bubble_page)
        insertion_button = tk.Button(main, text="Insertion Sort", borderwidth=1, width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3, command=insertion_page)
        merge_button = tk.Button(main, text="Merge Sort", borderwidth=1, width=12, height=1, relief="solid", bg=GRAY, font=fontStyle3, command=merge_page)

        # PLACEMENTS
        title.grid(row=0, column=1)
        selection.grid(row=1, column=1)
        bubble_button.grid(row=2, column=0, padx=5, pady=5)
        insertion_button.grid(row=2, column=1, padx=5, pady=5)
        merge_button.grid(row=2, column=2, padx=5, pady=5)
        main.pack(expand=True)

def display_bubble_info(event):
    info_win = tk.Toplevel(root)
    info_win.configure(bg=GRAY)
    width = info_win.winfo_screenwidth()
    height = info_win.winfo_screenheight()
    windowWidth = int(width / 2) - int((200 + 150) / 2)
    windowHeight = int(height / 2) - int(200 / 2)
    info_win.geometry(f"{200 + 150}x{150}+{windowWidth}+{windowHeight}")
    inputStyle = tkFont.Font(family="Lucida Grande", size=15)
    backButtonStyle = tkFont.Font(family="Lucida Grande", size=12)
    info_win.title("Algorithm Info")
    label = tk.Label(info_win, text="Time Complexity", bg=GRAY, font=inputStyle)
    label.pack(side="top", fill="x")
    best = tk.Label(info_win, text="Best: O(n)", bg=GRAY, font=backButtonStyle)
    best.pack(side="top", fill="x")
    worst = tk.Label(info_win, text="Worst: O(n^2)", bg=GRAY, font=backButtonStyle)
    worst.pack(side="top", fill="x")
    space = tk.Label(info_win, text="Space Complexity", bg=GRAY, font=inputStyle)
    space.pack(side="top", fill="x")
    space_value = tk.Label(info_win, text="O(1)", bg=GRAY, font=backButtonStyle)
    space_value.pack(side="top", fill="x")
    info_win.mainloop()
    
def draw_data(data, canvas, sort, colors):
    canvas.delete("all")
    c_height = 350
    c_width = 650
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5
    normalized = [i / max(data) for i in data]
    for i, height in enumerate(normalized):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 300
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i])) 
    sort.update_idletasks()

def shuffle_data(event, canvas, min_value, max_value, data_value, sort):
    global arr
    min_num = int(min_value.get())
    max_num = int(max_value.get())
    data_num = int(data_value.get())

    arr = random.sample(range(min_num, max_num), data_num)
    draw_data(arr, canvas, sort, ['blue' for x in range(len(arr))])

def start_bubble(event, canvas, sort, i_count):
    global arr, count
    count = 0
    i_count["text"] = f"{count}"
    bubble_sort(arr, draw_data, canvas, sort, count, i_count)

# BUTTON EVENTS
def bubble_page():

    # POPUP WINDOW SETTINGS
    bubble_w = tk.Toplevel(root)
    bubble_w.configure(bg=GRAY)
    width = bubble_w.winfo_screenwidth()
    height = bubble_w.winfo_screenheight()
    windowWidth = int(width / 2) - int((WIN_RES + 150) / 2)
    windowHeight = int(height / 2) - int(WIN_RES / 2)
    bubble_w.geometry(f"{WIN_RES + 150}x{WIN_RES}+{windowWidth}+{windowHeight}")
    bubble_w.title("Bubble Sort")

    # FONTS
    bubbleTitleStyle = tkFont.Font(family="Lucida Grande", size=18)
    backButtonStyle = tkFont.Font(family="Lucida Grande", size=10)
    inputStyle = tkFont.Font(family="Lucida Grande", size=15)

    # USER INTERFACE
    bubble_title = tk.Label(bubble_w, text="Bubble Sort", background=GRAY, font=bubbleTitleStyle)
    bubble_title.place(x=310, y=10)
    back_button = tk.Button(bubble_w, text="X", borderwidth=1, width=2, height=1, relief="solid", bg=GRAY, font=backButtonStyle, command=bubble_w.destroy)
    back_button.place(x=10, y=10)

    canvas = Canvas(bubble_w, width=650, height=350, bg="white")
    canvas.place(x=45, y=50)

    info_button = tk.Button(bubble_w, text="Information!", borderwidth=1, width=10, height=1, relief="solid", bg=GRAY, font=backButtonStyle)
    info_button.bind("<Button-1>", display_bubble_info)
    info_button.place(x=650, y=10)

    min_title = tk.Label(bubble_w, text="Min Value", background=GRAY, width=10, font=inputStyle)
    min_title.place(x=50, y=415)
    min_value = tk.Entry(bubble_w, bg=GRAY, width=8, font=inputStyle, relief="solid")
    min_value.place(x=155, y=415)
    min_value.insert(0, "0")

    max_title = tk.Label(bubble_w, text="Max Value", background=GRAY, width=10, font=inputStyle)
    max_title.place(x=260, y=415)
    max_value = tk.Entry(bubble_w, bg=GRAY, width=8, font=inputStyle, relief="solid")
    max_value.place(x=365, y=415)
    max_value.insert(0, "100")

    data_title = tk.Label(bubble_w, text="Data Size", background=GRAY, width=10, font=inputStyle)
    data_title.place(x=470, y=415)
    data_value = tk.Entry(bubble_w, bg=GRAY, width=8, font=inputStyle, relief="solid")
    data_value.place(x=575, y=415)
    data_value.insert(0, "10")

    # INITIAL DATA
    global arr, count
    draw_data(arr, canvas, bubble_w, ['blue' for x in range(len(arr))])

    iteration = tk.Label(bubble_w, text="Iterations:", background=GRAY, font=bubbleTitleStyle)
    iteration.place(x=90, y=10)

    iteration_count = tk.Label(bubble_w, text=f"{count}", width=3, background=GRAY, font=bubbleTitleStyle)
    iteration_count.place(x=200, y=10)

    # SHUFFLE BUTTON
    shuffle_button = tk.Button(bubble_w, text="Shuffle!", borderwidth=1, width=7, height=1, relief="solid", bg=GRAY, font=backButtonStyle)
    shuffle_button.place(x=575, y=10)
    shuffle_button.bind("<Button-1>", lambda event, a=canvas, b=min_value, c=max_value, d=data_value, e=bubble_w: shuffle_data(event, a, b, c, d, e))

    start_button = tk.Button(bubble_w, text="Start!", borderwidth=1, width=7, height=1, relief="solid", bg=GRAY, font=backButtonStyle)
    start_button.place(x=500, y=10)
    start_button.bind("<Button-1>", lambda event, a=canvas, b=bubble_w, c=iteration_count: start_bubble(event, a, b, c))
    
    # PLACEMENT
    bubble_w.mainloop()


def insertion_page():
    print("Insertion Sort Page")


def merge_page():
    print("Merge Sort Page")


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
