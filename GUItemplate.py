# -*- coding: utf-8 -*-
"""
The GUI was created with GUI Generator 1.0 by Jeff Chamberlain
Use the variables named in line 15 to calculate the output variable in line 17
"""


import tkinter as tk


def calculate():
    """Calculate the output value using the values entered in the GUI"""
    values = []
    for i in range(n):
        values.append(float(variables[i].get()))
    varlist = values

    outvar = 137.036  # calculate your value using the variables on the line above

    out_str = ("{:0.4}").format(outvar)  # the output widget expects a string
    out_str = out_str.rstrip("0").rstrip(".")  # value is rounded to 4 sig figs
    out_var.set(out_str)


def setup_gui():
    """Create n variable entry boxes, an output entry, and a button."""
    global n, w, variables, out_var
    n = number
    w = tk.Tk()
    w.title("GUItitle")
    w.geometry("250x" + str(75+50*n) + "+100+20")
    w.configure(background="#b0c0f0")
    filename = "Fizzix137-32x32.gif"  # feel free to use your own icon
    icon = tk.PhotoImage(file=filename)
    w.tk.call('wm', 'iconphoto', w._w, icon)
    w.iconify()
    w.update()
    w.deiconify()
    labels = labellist
    for i in range(n):
        tk.Label(w, text=labels[i],
                 background="#b0c0f0").place(x=20, y=40+50*i)
    variables = [tk.DoubleVar() for i in range(n)]
    var_entry = [0 for i in range(n)]
    for i in range(n):
        var_entry[i] = tk.Entry(w, textvariable=variables[i])
        var_entry[i].place(x=20, y=60+50*i, height=20, width=80)
    tk.Button(w, text="Calculate", command=calculate).place(x=150, y=60)
    tk.Label(w, text=outlabel,
             background="#b0c0f0").place(x=150, y=90)
    out_var = tk.StringVar()
    out_entry = tk.Entry(w, textvariable=out_var)
    out_entry.place(x=150, y=110, height=20, width=80)
    menu_object = tk.Menu(w)
    w.configure(menu=menu_object)
    main_menu = tk.Menu(menu_object, tearoff=0)
    menu_object.add_cascade(menu=main_menu, label="File")
    main_menu.add_command(command=prog_exit, label="Exit")


def prog_exit():
    """Close window and stop execution"""
    w.destroy()
    w.quit()


setup_gui()
w.mainloop()
