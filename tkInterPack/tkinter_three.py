from PIL import Image
from tkinter import Tk, Label
import PIL.ImageTk as ImageTk

window = Tk()

window.title("My first image window")
#set window as fixed size
window.resizable(width=False, height=False)
window.geometry("400x400")

img = Image.open("images/image.png")
img = ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

# options for panel.pack() are:
# anchor, side, fill, expand, ipadx, ipady, padx, pady


window.mainloop()
