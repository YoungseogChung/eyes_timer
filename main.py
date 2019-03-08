import sys, time, os
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Helvetia', 10)
SMALL_FONT = ( 'Helveetica', 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill = 'x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command = popup.destroy)
    B1.pack()
    popup.mainloop()

def main():
    while True:
        popupmsg('Starting another session')
        time.sleep(60*20)
        popupmsg('Save them eyes bruv')
        time.slee(20)

if __name__ == '__main__':
    main()
