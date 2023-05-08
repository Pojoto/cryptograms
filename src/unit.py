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

        #self.label.pack()

        self.entry_text = StringVar()

        self.entry = Entry(self.frame, width=2, textvariable=self.entry_text, font=("Times New Roman", 20), state='readonly', cursor="arrow")
        self.entry.pack(padx=5,pady=5)

        self.entry.bind("<FocusIn>", self.cryptogram.click_focus)
        self.entry.bind("<Key>", self.check_character)

        #self.entry_text.trace_add("write", lambda *args: self.character_limit(self.entry_text))
    
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


    def character_limit(self, entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])
        entry_text.set(entry_text.get().upper())
        self.cryptogram.copy_entry(self.char, entry_text.get())