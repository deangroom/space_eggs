from tkinter import *
from PIL import Image, ImageTk

# Create the Tkinter window
window = Tk()

# Set the window title and size
window.title("Tkinter Six - The Grid System")
window.geometry("400x400")

# Place a label in the window for the username and password
# Place a username input box and a password input box in the middle of the window
user_label = Label(window, text="Username")
user_input = Entry(window)

password_label = Label(window, text="Password")
password_input = Entry(window)

# Place these components using grid
user_label.grid(row=0, column=0)
user_input.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_input.grid(row=1, column=1)

# Place login and cancel buttons side by side using grid
login_button = Button(window, text="Login")
login_button.grid(row=2, column=0)

cancel_button = Button(window, text="Cancel")

# the sticky option allows you to align the button to the left or right using W or E compass directions (I know, it's weird)
cancel_button.grid(row=2, column=1, sticky=W)

# Run the Tkinter event loop
window.mainloop()
