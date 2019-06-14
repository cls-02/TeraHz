from serial import Serial
import tkinter as tk
import pandas as pd

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

uartpath = '/dev/ttyUSB0'
uartbaud = 115200
uarttout = 5

wl = [410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940]
responseorder = [i for i in 'RSTUVWGHIJKLABCDEF'] # works, do NOT touch!
realorder = [i for i in 'ABCDEFGHRISJTUVWKL']

root = tk.Tk()
root.wm_title('TeraHz Demo')

fig = Figure(figsize=(5, 4), dpi=100)
plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
