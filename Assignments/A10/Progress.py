import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
win.title("Progress Bar")


def fill():
    val = int(prog['value'] + 20)
    if (val < 101):
        prog['value'] = val
        lblProg.configure(text=f"{val}%")


ttk.Label(text="Click button to fill progress bar").pack()
ttk.Button(text="Click", command=fill).pack()
prog = ttk.Progressbar(0)
prog.pack()
lblProg = ttk.Label(text="0%")
lblProg.pack()

win.mainloop()
