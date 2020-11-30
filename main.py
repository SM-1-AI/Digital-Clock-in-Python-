import sys

import time

from tkinter import *


def main():
    Time_sting = time.strftime("%I : %M : %S ,%p")
    clock.config(text=Time_sting)
    clock.after(200, main)


root = Tk()
root.resizable(False, False)

clock = Label(font=("arial", 50), foreground="white", bg="black")
clock.grid(row=0, column=1)
main()
root.mainloop()
