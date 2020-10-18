# Jaime Garcia, Rodrigo Palacios, Isaac Valdez
# 10/12/2020
# AlgoViz
# Description:
# This program is meant to visually show the speed at which sorting algorithms operate at.
# In the program the user will be able to select from a variety of sorting algorithms and test their speeds!
# Users will also get detailed information about each algorithm and how it operates

import tkinter as tk

WIN_RES = 600
WIN_RES_DIFF = WIN_RES / 2

w = tk.Tk()
w.title("AlgoViz")
width = w.winfo_screenwidth()
height = w.winfo_screenheight()

windowWidth = int(width / 2) - int((WIN_RES * 2) / 2)
windowHeight = int(height / 2) - int(WIN_RES / 2)
w.geometry(f"{WIN_RES * 2}x{WIN_RES}+{windowWidth}+{windowHeight}")

w.mainloop()
