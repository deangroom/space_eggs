import tkinter as Tk

# Create a window 400 x 400
window = Tk.Tk()
window.title("My First Calculator")
window.geometry("400x400")

# Initialise area_label as None
area_label = None

# Function to calculate and display the area
def calculate_area():
    global area_label  # Use the global area_label
    if area_label:
        area_label.destroy()  # Remove the previous label (if it exists)

    # Get the value from the input box
    width_value = int(width_input.get())
    height_value = int(height_input.get())

    # Calculate the area
    area = width_value * height_value

    # Display the area
    area_label = Tk.Label(window, text=f"Area: {area}")
    area_label.pack()

# Add some text to the window
heading = Tk.Label(window, text="Area Calculator")

# Add label and text input box to enter width
width = Tk.Label(window, text="Enter width:")
width_input = Tk.Entry(window)

# Add label and text input box to enter height
height = Tk.Label(window, text="Enter height:")
height_input = Tk.Entry(window)

# Add button to calculate area
area_button = Tk.Button(window, text="Calculate Area", command=calculate_area)

# Pack the widgets
heading.pack()
width.pack()
width_input.pack()
height.pack()
height_input.pack()
area_button.pack()

window.mainloop()
