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
    
    def __init__(self, window, text):
        self.text = text
        self.window = window
        self.units = self.create_units()
        self.current_focus = None
    
    def update_focus(self, event):
        print("focus updated")
        self.current_focus = event.widget

    def character_checks(self, event):
        char = event.char.lower()
        print("character checks")

        print(len(event.widget.get()))

        if char in legal_chars:
            print("go to next")
            self.set_next_focus()

    
    def create_units(self):
        units = []
        for ch in self.text:
            unit = Unit(self.window, ch)
            units.append(unit)

            #unit.entry.bind("<FocusIn>", lambda *args: self.update_focus(unit))
            unit.entry.bind("<FocusIn>", self.update_focus)

            unit.entry.bind("<Key>", self.character_checks)

            #name = unit.entry_text.trace_add("write", lambda *args: test_entry(unit.entry_text))#self.character_checks)#self.character_checks(unit.entry_text, unit.entry))
            #print("observer:", name)

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
        self.current_focus = self.units[index + 1].entry if index + 1 < len(self.units) else self.current_focus

    
    #TODO: maybe create a 'unit' class which has both entry and the text letter above/below it. each unit is in its own canvas