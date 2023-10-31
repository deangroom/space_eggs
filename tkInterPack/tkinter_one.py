'''
This is the first script to show you
how to create a simple window with
common elements such as a label,
text input box and a button.

The keywords in this script are:
- tkinter
- Tk()
- title()
- geometry()
- Label()
- Entry()
- Button()
- pack()
- mainloop()

The variables in this script are:
- window
- heading
- input_box
- button

'''

import tkinter as Tk

# Create a window 400 x 400
window = Tk.Tk()
window.title("My First window")
window.geometry("400x400")

#add a label to the window
heading = Tk.Label(window, text="This is some text")
heading.pack()

#add a text input box to the window
input_box = Tk.Entry(window)
input_box.pack()

#add a button to the window
button = Tk.Button(window, text="Click Me")
button.pack()

window.mainloop()
