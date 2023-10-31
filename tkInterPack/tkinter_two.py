import tkinter as Tk

# Create a window 400 x 400
window = Tk.Tk()
window.title("My First window")
window.geometry("400x400")

#add a label to the window
name = Tk.Label(window, text="What is your name?")
name.pack()

#add a text input box to the window
input_box = Tk.Entry(window)
input_box.pack()

#add a button to the window
button = Tk.Button(window, text="Submit")
button.pack()

#display name when the button is clicked
#we are talking about a function here
#we are using f-strings here

def display_name():
    name_label = Tk.Label(window, text=f"Hello {input_box.get()}")
    name_label.pack()

button.config(command=display_name)  #this is the command that will be executed when the button is clicked

window.mainloop()
