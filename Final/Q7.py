# Write Python code to design a GUI for subject registration form as shown below [Figure]
import tkinter as tk

def report():
  out = ""
  for i in range(3):
    out += f"{lbls[i]} : {txts[i].get()}\n"

  selected = [i.get() for i  in chkVars if i.get()]
  out += f"You selected {len(selected)} Subjects\n\n"
  for i in range(5):
    if (chkVars[i].get()):
      out += f"-{subjects[i]}\n"
  txtRep.delete(1.0, tk.END)
  txtRep.insert(0.0, out)

win = tk.Tk()
win.title("Registration")
win.config(width=375, height=450)
txts, lbls = [], ["Name", "Father Name", "Registration Number"]
for i in range(3):
  tk.Label(text=lbls[i]).grid(row=i, column=0)
  txts.append(tk.Entry(width=25))
  txts[i].grid(row=i,column=1)

tk.Label(text="Select the subjects you want to enroll: ").grid(row=3,column=0)
chkVars = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
subjects = ["Introduction to Computers", "Programming Fundamentals", "Calculus", "Operating System", "Data Structure and Algorithms"]
for i in range(5):
  tk.Checkbutton(text=subjects[i], var = chkVars[i]).grid(row=i+4, column=0)

tk.Button(text="Report", command=report).grid(row=9, column=1)
txtRep = tk.Text(width=45, height=12)
txtRep.grid(row=10, column=0, columnspan=2)

win.mainloop()