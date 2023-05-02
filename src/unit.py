from tkinter import *

class Unit:

    def __init__(self, window, char):
        self.char = char
        self.frame = Frame(window, width=30, height=50)
        self.frame.pack()
        self.entry_text = StringVar()
        print(self.entry_text.get())
        self.entry = Entry(self.frame, width=3, textvariable=self.entry_text)
        self.entry.pack(padx=5,pady=5)
        self.label = Label(self.frame, text=char)
        self.label.pack()

        self.entry_text.trace_add("write", lambda *args: self.character_limit(self.entry_text))
    
    def character_limit(self, entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])


#TODO: each unit should have a stringvar, entry, and letter field all in a packed canvas