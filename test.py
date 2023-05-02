from tkinter import *
import random

# Event handler for mouse pressed events.
# Adds a randomly colored and sized dot to the canvas.
def add_dot(event):
    color = random.choice(colors)
    radius = random.randint(6, 15)
    canvas.create_oval(event.x - radius, event.y - radius,
                       event.x + radius, event.y + radius,
                       fill=color, outline=color)

# Set up the window and canvas.
root = Tk()
root.title('Mouse Dots')

canvas = Canvas(root, bg='black', width=400, height=300)
canvas.pack(fill=BOTH, expand=True)

colors = ['white', 'red', 'lime', 'yellow', 'gold', 'hotpink', 'magenta', 'cyan']

# Set up the mouse pressed event handler.
canvas.bind('<Button-1>', add_dot)

root.mainloop()