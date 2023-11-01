from tkinter import *
from PIL import Image, ImageTk

with open("tkInterPack\password.txt") as file:
    password = file.readline()
    print(password)

window = Tk()
window.title("Tkinter Five")
window.geometry("400x400")

def check_password():
    if password_input.get() == password:
        result_label.configure(text="Correct!")
    else:
        result_label.configure(text="Incorrect!")
    photo_label.pack_forget() # Removes the photo label after checking password
    result_label.pack() # Shows the result_label after checking password

image = Image.open("images/image.png")
image = image.resize((200, 200))

photo = ImageTk.PhotoImage(image)
photo_label = Label(window, image=photo)
photo_label.pack()

result_label = Label(window, text="")

user_password = Label(window, text="Password")
user_password.pack()

password_input = Entry(window)
password_input.pack()

login_button = Button(window, text="Login", command=check_password)
login_button.pack()

window.mainloop()
