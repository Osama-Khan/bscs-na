#Design a GUI using Tkinter in python for sorting of five user defined integers, the specifications of GUI is as follows
#•	Set Window size of 300x250
#•	All Labels are in column 0.
#•	All Entry text boxes are in column 1.
#•	Sort button is in column 1.
#•	Set Display text field of width 35 and height 6 with column span of 10.
#•	Display text field is in column 0.

import tkinter as tk

def sort():
  inp = [float(t.get()) for t in txts]
  output = f"Entered: {inp}\n"
  inp.sort()
  output += f"Sorted: {inp}"
  txtout.delete(1.0, tk.END)
  txtout.insert(0.0, output)

win = tk.Tk()
win.config(width=300, height=250)
txts = []
for i in range(5):
  tk.Label(text=f"Enter integer {i+1}: ").grid(column=0, row=i)
  txts.append(tk.Entry())
  txts[i].grid(column=1,row=i)

tk.Button(text="Sort", command=sort).grid(column=1, row=5)
txtout = tk.Text(width=35, height=6)
txtout.grid(column=0, row=6, columnspan=10)


win.mainloop()

