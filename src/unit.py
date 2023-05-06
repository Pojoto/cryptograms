from tkinter import *
from random import randint
from alphabet import alpha_set

class Unit:

    def __init__(self, frame, char):
        self.char = char
        
        self.frame = Frame(frame, width=30, height=0)#, background="black")

        self.label = Label(self.frame, text=char, font=("Times New Roman", 20))
        self.label.pack(side=BOTTOM)



class EntryUnit(Unit):
    
    def __init__(self, frame, char):

        super().__init__(frame, char)

        self.entry_text = StringVar()

        self.entry = Entry(self.frame, width=2, textvariable=self.entry_text, font=("Times New Roman", 20))
        self.entry.pack(padx=5,pady=5)

        self.entry_text.trace_add("write", lambda *args: self.character_limit(self.entry_text))
    

    def character_limit(self, entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])