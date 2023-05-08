from tkinter import *
from random import randint
from alphabet import alpha_set

class Unit:

    def __init__(self, cryptogram, frame, char):
        self.char = char
        
        self.cryptogram = cryptogram

        self.frame = Frame(frame, width=30, height=0)#, background="black")

        self.text = Label(self.frame, text=char, font=("Times New Roman", 20))
        self.text.pack(side=BOTTOM)



class EntryUnit(Unit):
    
    def __init__(self, cryptogram, frame, char):

        super().__init__(cryptogram, frame, char)

        self.entry = Entry(self.frame, width=2, textvariable=self.entry_text, font=("Times New Roman", 20), state='readonly', cursor="arrow")
        self.entry.pack(padx=5,pady=5)

        self.entry.bind("<FocusIn>", self.cryptogram.click_focus)
        self.entry.bind("<Key>", self.check_character)

    
    #function handling which characters are pressed, how to react
    def check_character(self, event):
        char = event.char.upper()
        #print(event.keycode)

        if len(self.entry.get()) > 0:
            self.entry.delete(0, END)
        
        print("insert")
        self.entry.insert(0, char)

        if char in alpha_set:
            self.cryptogram.set_next_focus()
        elif event.keycode == 8: #check if backspace was pressed
            self.cryptogram.set_prev_focus()
            self.cryptogram.current_focus.delete(0, END)
        elif event.keycode == 32: #check if space was pressed - move to next entry
            self.cryptogram.set_next_focus()
        elif event.keycode == 37: #check if left arrow was pressed - go to prev entry
            self.cryptogram.set_prev_focus()
        elif event.keycode == 39: # check if right arrow was pressed - go to next entry
            self.cryptogram.set_next_focus()
