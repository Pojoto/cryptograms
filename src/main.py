
from tkinter import *
from cryptogram import Cryptogram
from random import shuffle
from alphabet import alpha_list


def encrypt(plaintext):

    plaintext = plaintext.lower()
    
    random_chars = alpha_list.copy()
    shuffle(random_chars)

    key = {plain: cipher for plain, cipher in zip(alpha_list, random_chars)}

    ciphertext = ""
    for ch in plaintext:
        if ch in key:
            ciphertext += key[ch]
        else:
            ciphertext += ch
    
    return ciphertext


root = Tk()

root.title("Cryptograms")

root.configure(background='lightblue')

window_width = 900
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


with open("quotes.txt", "r") as quotes_file:
    global plaintext
    plaintext = quotes_file.readline().strip()

ciphertext = encrypt(plaintext)

print(ciphertext)
print(plaintext)

cryptogram = Cryptogram(root, ciphertext, plaintext)
cryptogram.main_frame.pack(expand=True, anchor=CENTER)


# entry_text = StringVar()


# entry1 = Entry(root, width = 5, textvariable=entry_text)
# entry2 = Entry(root, width = 5)

# entry1.pack(side=LEFT, pady=5, padx=5)

# entry_text.trace_add("write", lambda *args: character_limit(entry_text))

#TODO: make sure you only let user type one letter at a time

# entry2.pack(side=LEFT, pady=5, padx=5)

#entry.place(relx = 0.5, rely=0.5, anchor=CENTER)



root.mainloop()

# from tkinter import *

# root = Tk()
# root.geometry("200x200+50+50") # heightxwidth+x+y

# mainPanel = Canvas(root, width = 200, height = 200) # main screen
# mainPanel.pack()

# entry_text = StringVar() # the text in  your entry
# entry_widget = Entry(mainPanel, width = 5, textvariable = entry_text) # the entry
# mainPanel.create_window(100, 100, window = entry_widget)

# def character_limit(entry_text):
#     if len(entry_text.get()) > 0:
#         entry_text.set(entry_text.get()[-1])

# entry_text.trace("w", lambda *args: character_limit(entry_text))

# root.mainloop()