from tkinter import *
from PIL import Image, ImageTk

# Create the Tkinter window
window = Tk()

# Set the window title and size
window.title("My Image Background")
window.geometry("400x400")

# Load and resize the image, resizing is optional
image = Image.open("images/image.png")
image = image.resize((200, 200)) #optional

# Create the PhotoImage object after resizing
photo = ImageTk.PhotoImage(image)

# Create a label with the image as the background
label = Label(window, image=photo)
label.pack()

# Run the Tkinter event loop
window.mainloop()
