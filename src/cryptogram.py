from tkinter import *
from unit import Unit


legal_chars = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}


def find_entry_index(units, entry):
    for i, unit in enumerate(units):
        if(unit.entry == entry):
            return i
    return -1

def test_entry(entry_text):
    #print(type(var))
    print(entry_text)

class Cryptogram:
    
    def __init__(self, window, ciphertext, plaintext):
        self.ciphertext = ciphertext
        self.plaintext = plaintext
        self.frame = Frame(window)
        self.frame.pack(expand=True, fill=X, anchor=CENTER)
        self.units = self.create_units()
        self.current_focus = None

        button = Button(self.frame, text="Enter", command=self.check_answer)
        button.pack()
    
    def update_focus(self, event):
        print("focus updated")
        self.current_focus = event.widget

    def check_character(self, event):
        char = event.char.lower()
        print(event.keycode)
        print("character checks")

        print(len(event.widget.get()))

        if char in legal_chars:
            print("go to next")
            self.set_next_focus()
        elif event.keycode == 8: #check if backspace was pressed
            print("go back")
            self.set_prev_focus()
            self.current_focus.delete(0, END)

    
    def create_units(self):
        units = []
        for ch in self.ciphertext:

            if ch in legal_chars:

                unit = Unit(self.frame, ch)
                units.append(unit)

                #unit.entry.bind("<FocusIn>", lambda *args: self.update_focus(unit))
                unit.entry.bind("<FocusIn>", self.update_focus)

                unit.entry.bind("<Key>", self.check_character)

                #name = unit.entry_text.trace_add("write", lambda *args: test_entry(unit.entry_text))#self.character_checks)#self.character_checks(unit.entry_text, unit.entry))
                #print("observer:", name)
            else:
                unit = Unit(self.frame, ch)

        return units
            

    def set_next_focus(self):
        print("setting next focus")
        #find the index of the current focus entry
        index = find_entry_index(self.units, self.current_focus)

        if index + 1 < len(self.units): #if there is a next entry in the list (not the last one)
            next_focus = self.units[index + 1].entry
            self.current_focus = next_focus
            next_focus.focus_set() #physically set the focus

        #set the current focus to be the next entry in the list. however, if it's the last entry than keep the same focus

    def set_prev_focus(self):

        index = find_entry_index(self.units, self.current_focus)

        if index - 1 >= 0:
            prev_focus = self.units[index - 1].entry
            self.current_focus = prev_focus
            prev_focus.focus_set()
    
    def check_answer(self):
        user_answer = ""

        for unit in self.units:
            entry = unit.entry
            user_answer += entry.get().lower()
        

        print(user_answer)
    

    
    #TODO: make the cryptogram class have its own frame