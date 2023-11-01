'''
This is a simple program that loads an image, resizes it and places it in a Tkinter window.
It also asks the user if the image is cool or not and displays the answer in a label.

It demonstrates:
    - loading an image
    - resizing an image
    - placing an image in a Tkinter window
    - creating a label
    - creating a button
    - binding a button to an action
    - changing the text of a label

Your challenge is to:
    - place the label and buttons in the window using the grid system
'''

from tkinter import *
from PIL import Image, ImageTk

# Create the Tkinter window
window = Tk()

# Set the window title and size
window.title("My Image Background")
window.geometry("400x400")

#---load an image, resize it and place it in the window---

# Load and resize the image, resizing is optional
image = Image.open("images/image.png")
image = image.resize((200, 200)) #optional

# Create the PhotoImage object after resizing
photo = ImageTk.PhotoImage(image)

# Create a label with the image as the background
label = Label(window, image=photo)
label.pack()

#-------------end image set up----------------

#create a lable to ask "is this image cool?"
question_label = Label(window, text="Is this image cool?")
question_label.pack()

# Create a button to answer "yes"
yes_button = Button(window, text="Yes")
yes_button.pack()

# Create a button to answer "no"
no_button = Button(window, text="No")
no_button.pack()

#create an action for the yes button
def yes_clicked():
    question_label.configure(text="Yes, it's cool!")

#create an action for the no button
def no_clicked():
    question_label.configure(text="No, it's not cool!")

#bind the buttons to their actions
yes_button.configure(command=yes_clicked)
no_button.configure(command=no_clicked)

# Run the Tkinter event loop
window.mainloop()
