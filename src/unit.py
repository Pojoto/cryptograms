from tkinter import *
from random import randint
from alphabet import alpha_set

from random import choice
colors = ["red", "blue", "green", "yellow", "orange", "pink", "brown", "gray", "purple"]


class Unit:

    def __init__(self, cryptogram, frame, char):
        self.char = char
        
        self.cryptogram = cryptogram

        self.frame = Frame(frame, width=30, height=0, bg="lightgray")#, background = choice(colors))#, background="black")

        self.text = Label(self.frame, text=char, bg="lightgray", font=("Times New Roman", 20))
        self.text.pack(side=BOTTOM)

class SpaceUnit(Unit):

    def __init__(self, cryptogram, frame, char):
        super().__init__(cryptogram, frame, char)

        self.text.configure(width=2, bg="SystemButtonFace")



class EntryUnit(Unit):
    
    def __init__(self, cryptogram, frame, char):

        super().__init__(cryptogram, frame, char)

        self.entry = Entry(self.frame, width=2, font=("Times New Roman", 20), state='readonly', cursor="arrow")
        self.entry.pack(padx=5,pady=5)

        #pass the current entry unit object(self) to the click focus function in cryptogram manager 
        self.entry.bind("<FocusIn>", lambda event: self.cryptogram.click_focus(self))
        self.entry.bind("<Key>", self.check_character)

    def add_freq(self, freq):
        self.freq = Label(self.frame, text=freq, bg="lightgray", font=("Times New Roman", 20))
        self.freq.pack()
    
    #function handling which characters are pressed, how to react
    def check_character(self, event):
        char = event.char.upper()
        
        #print(event.keycode)

        if char in alpha_set or char == " ": #space should also replace chars, and move to next entry (treat as normal letter in this case)

            #copy the user char (char) into all the entries that share the same char as self.char (label char)
            self.cryptogram.copy_entry(self.char, char)
            self.cryptogram.set_next_focus()
            
        elif event.keycode == 8: #check if backspace was pressed
            self.cryptogram.copy_entry(self.char, "") #remove all characters of the shared entries (replace them with space)
            self.cryptogram.set_prev_focus()
        elif event.keycode == 32: #check if space was pressed
            self.cryptogram.copy_entry(self.char, "")
            self.cryptogram.set_next_focus()
        elif event.keycode == 37: #check if left arrow was pressed - go to prev entry
            self.cryptogram.set_prev_focus()
        elif event.keycode == 39: # check if right arrow was pressed - go to next entry
            self.cryptogram.set_next_focus()


