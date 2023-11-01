from tkinter import *
from PIL import Image, ImageTk

# Create the Tkinter window
window = Tk()

# Set the window title and size
window.title("Tkinter Five")
window.geometry("400x400")

#place a label in the window for the username and password
#place a username input box and a password input box in the middle of the window
#place a login button underneath the input boxes

user_label = Label(window, text="Username")
user_label.pack()

user_input = Entry(window)
user_input.pack()


user_password = Label(window, text="Password")
user_password.pack()

password_input = Entry(window)
password_input.pack()

login_button = Button(window, text="Login")
cancel_button = Button(window, text="Cancel")

login_button.pack()
cancel_button.pack()

# Run the Tkinter event loop
window.mainloop()
