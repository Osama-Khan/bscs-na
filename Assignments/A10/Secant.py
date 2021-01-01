import tkinter as tk
from tkinter import ttk

global s, e, c, co, cond


def f(x):
    return x**3 + x - 1


def clickMe():
    cond = 0
    p = txt.get(1.0, 'end')
    txt.delete(0.0, 'end')
    s = a.get()
    e = b.get()
    fs = f(s)
    fe = f(e)

    c = (s*fe - e*fs)/(fe - fs)
    fc = f(c)

    a.set(e)
    b.set(c)
    # if fs*fc > 0 and fe*fc < 0:
    #    a.set(c)
    # elif fe*fc > 0 and fs*fc < 0:
    #    b.set(c)
    # else:
    #    n1 = 'ERROR due to wrong interval of values'
    #    cond = 1
    if cond == 0:
        n1 = str(p+str(globals()['co'])+'\t'+str(s)+'\t\t\t'+str(e) +
                 '\t\t\t'+str(c)+'\t\t\t'+str(fs)+'\t\t\t'+str(fe)+'\t\t\t'+str(fc))

    txt.insert(0.0, n1)
    globals()['co'] = int(globals()['co'])+1


win = tk.Tk()
win.title("Bisection Application in Python")
ttk.Label(win, text="Enter starting value ",).grid(column=0, row=0)


co = 0

a = tk.DoubleVar()
a1 = ttk.Entry(win, width=20, textvariable=a)
a1.grid(column=1, row=0)


ttk.Label(win, text="Enter ending value ",).grid(column=0, row=1)

b = tk.DoubleVar()
b1 = ttk.Entry(win, width=20, textvariable=b)
b1.grid(column=1, row=1)

txt = tk.Text(win, width=200, height=20, wrap=tk.WORD)
txt.grid(columnspan=10, row=2, column=0)
txt.insert(0.0, 'n\tan\t\t\tbn\t\t\tcn\t\t\tf(an)\t\t\tf(bn)\t\t\tf(cn)')


action = ttk.Button(win, text="Click Me...", command=clickMe)
action.grid(column=0, row=3, columnspan=2)
win.mainloop()
