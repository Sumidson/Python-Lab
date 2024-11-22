import tkinter as tk
import random

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_palette():
    for color_label in color_labels:
        color = random_color()
        color_label.config(bg=color, text=color)

# Create the main window
root = tk.Tk()
root.title("Random Color Palette Generator")

# Create labels to display the colors
color_labels = [tk.Label(root, text="", width=20, height=2) for _ in range(5)]

# Arrange the labels in the window
for i, color_label in enumerate(color_labels):
    color_label.grid(row=i, column=0, padx=10, pady=5)

# Create a button to generate the color palette
generate_button = tk.Button(root, text="Generate Palette", command=generate_palette)
generate_button.grid(row=len(color_labels), column=0, pady=10)

# Run the Tkinter event loop
root.mainloop()
