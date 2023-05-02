
from tkinter import *
from cryptogram import Cryptogram

root = Tk()

root.title("Cryptograms")

root.configure(width=600, height=300, background='lightblue')

text = "hello there"

cryptogram = Cryptogram(root, text)


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