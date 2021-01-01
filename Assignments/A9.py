import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
win.title("Bill Calculator")


def calculate():
    try:
        units = int(txtUnits.get())
    except:
        return
    mul8 = 100 if units >= 100 else units
    mul12, mul15 = 0, 0
    units -= 100
    if units > 0:
        mul12 = 200 if units >= 200 else units
        units -= 200
        if units > 0:
            mul15 = units
    out = f"""Name: {txtName.get()}\n
    Bill ID: {txtId.get()}\n
    Units Consumed: {txtUnits.get()}\n
    Bill Detail:\n
    {mul8} x 8 = {mul8*8}\n
    {mul12} x 12 = {mul12*12}\n
    {mul15} x 15 = {mul15*15}\n
    Total \t = {mul8*8+mul12*12+mul15*15}"""

    lblBill.configure(text=out)


ttk.Label(text="Enter a name").grid(column=0, row=0)
txtName = ttk.Entry(win, width=20)
txtName.grid(column=2, row=0)
ttk.Label(text="Enter Bill ID").grid(column=0, row=1)
txtId = ttk.Entry(win, width=20)
txtId.grid(column=2, row=1)
ttk.Label(text="Enter Units Consumed").grid(column=0, row=2)
txtUnits = ttk.Entry(win, width=20)
txtUnits.grid(column=2, row=2)
ttk.Label(text="").grid(column=0, row=3)
ttk.Button(text="Calculate", command=calculate).grid(
    column=0, row=4, columnspan=3)

lblBill = ttk.Label(text="Please enter bill details", justify="left")
lblBill.grid(column=0, row=5, columnspan=3, rowspan=10)

win.mainloop()
