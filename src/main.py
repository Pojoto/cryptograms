
from tkinter import *
from mainframe import MainFrame
from random import shuffle
from alphabet import alpha_list


root = Tk()

root.title("Cryptograms")

root.configure(background='lightblue')

root.state("zoomed")

#root.attributes("-fullscreen", True)


# window_width = 1200
# window_height = 800

# # get the screen dimension
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # find the center point
# center_x = int(screen_width / 2 - window_width / 2)
# center_y = int(screen_height / 2 - window_height / 2)

# # set the position of the window to the center of the screen
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

with open("quotes.txt", "r") as quotes_file:
    global quotes
    quotes = [line.rstrip() for line in quotes_file]

def start(start_frame):
    start_frame.destroy()
    main_frame = MainFrame(root, quotes)
    main_frame.frame.pack(expand=True, anchor=CENTER)

def start_menu(root):
    frame = Frame(root)
    title = Label(frame, text="Cryptograms", font=("Courier", 100))
    start_button = Button(frame, text="Start", font=("Courier", 20), command=lambda *args: start(frame))
    title.pack()
    start_button.pack()
    frame.pack(expand=True, anchor=CENTER)


start_menu(root)



root.mainloop()