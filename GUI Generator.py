# -*- coding: utf-8 -*-
"""
                                GUI Generator 1.0
Quickly creates a GUI for inputting numeric values and displaying a result.
Requires GUItemplate.py and Fizzix137-32x32.gif in the same folder with it.
"""
# (c)2019 Jeff Chamberlain
# This program is free software: you can use it under the terms of the
# GNU Affero General Public License version 3. This program is distributed
# WITHOUT ANY WARRANTY of any kind. See the GNU Affero General Public License
# for more details. <https://www.gnu.org/licenses/>.


import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from os.path import basename


def generate():
    """Modifies the template file using the names entered in the GUI"""
    filename = asksaveasfilename(defaultextension=".py",
                                 filetypes=[("Python files", "*.py")],
                                 title="Program Name")
    if filename == "":
        return
    title = basename(filename)
    n = 0  #  n counts the number of labels/entries to create
    svars = []
    for i in range(8):
        v = variables[i].get()
        if v != "":
            n += 1
            svars.append(v)
    varlist = ", ".join(svars)
    slabels = []
    for i in range(n):
        slabels.append(labels[i].get())
    lbl = "["
    for i in range(n):
        lbl = lbl + "'" + slabels[i] + "', "
    lbl = lbl.rstrip(", ")
    lbl = lbl + "]"
    out_lbl = "'" + out_label.get() + "'"
    with open("GUItemplate.py", "r") as f:
        newfile = f.read()
    newfile = newfile.replace("labellist", lbl)
    newfile = newfile.replace("outlabel", out_lbl)
    newfile = newfile.replace("number", str(n))
    newfile = newfile.replace("varlist", varlist)
    newfile = newfile.replace("outvar", out_var.get())
    newfile = newfile.replace("GUItitle", title)
    ff = open(filename, "w")
    ff.write(newfile)
    ff.close()
    for i in range(8):
        labels[i].set("Done.")
        variables[i].set("Done.")
        w.after(100)
        w.update()
    w.destroy()
    w.quit()


def prog_exit():
    """Close window and stop execution"""
    w.destroy()
    w.quit()


w = tk.Tk()
w.title("GUI Generator 1.0")
w.geometry("560x470+100+20")
w.configure(background="#b0c0f0")

filename = "Fizzix137-32x32.gif"
icon = tk.PhotoImage(file=filename)
w.tk.call('wm', 'iconphoto', w._w, icon)
w.iconify()
w.update()
w.deiconify()

labels = [tk.StringVar() for i in range(8)]  #  holds labels entered
label_entry = [0 for i in range(8)]          #  entry widgets

variables = [tk.StringVar() for i in range(8)]  #  holds names of variables
var_entry = [0 for i in range(8)]               #  entry widgets

tk.Label(w, text="Labels", background="#b0c0f0").place(x=20, y=30)
tk.Label(w, text="Python Variables", background="#b0c0f0").place(x=220, y=30)

for i in range(8):
    label_entry[i] = tk.Entry(w, textvariable=labels[i])
    label_entry[i].place(x=20, y=50+30*i, height=20, width=180)

for i in range(8):
    var_entry[i] = tk.Entry(w, textvariable=variables[i])
    var_entry[i].place(x=220, y=50+30*i, height=20, width=80)

out_label = tk.StringVar()
out_var = tk.StringVar()
tk.Label(w, text="Output Label", background="#b0c0f0").place(x=20, y=300)
tk.Label(w, text="Output Variable", background="#b0c0f0").place(x=220, y=300)
out_label_entry = tk.Entry(w, textvariable=out_label)
out_label_entry.place(x=20, y=320, height=20, width=180)
out_var_entry = tk.Entry(w, textvariable=out_var)
out_var_entry.place(x=220, y=320, height=20, width=80)

tk.Button(w, text="Generate", command=generate).place(x=330, y=50)

menu_object = tk.Menu(w)
w.configure(menu=menu_object)
main_menu = tk.Menu(menu_object, tearoff=0)
menu_object.add_cascade(menu=main_menu, label="File")
main_menu.add_command(command=prog_exit, label="Exit")

w.mainloop()
