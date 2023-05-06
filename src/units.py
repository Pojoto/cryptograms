from tkinter import *
from unit import *
from alphabet import alpha_set


def find_entry_index(units, entry):
    for i, unit in enumerate(units):
        if(unit.entry == entry):
            return i
    return -1


class Units:

    def __init__(self, root, text):
        self.frame = Frame(root)
        self.entry_units = self.make_units(text)
        self.current_focus = None

    
    def make_units(self, text):
        entry_units = []
        for i, ch in enumerate(text):

            if ch in alpha_set:

                entry_unit = EntryUnit(self.frame, ch)
                entry_units.append(entry_unit)
                entry_unit.frame.grid(row = i // 15, column = i % 15, padx=2)
                
                entry_unit.entry.bind("<FocusIn>", self.update_focus)
                entry_unit.entry.bind("<Key>", self.check_character)

            else:
                unit = Unit(self.frame, ch)
                unit.frame.grid(row = i // 15, column = i % 15, padx=2)
        return entry_units
    

    def check_character(self, event):
        char = event.char.lower()
        print(event.keycode)
        print("character checks")

        print(len(event.widget.get()))

        if char in alpha_set:
            print("go to next")
            self.set_next_focus()
        elif event.keycode == 8: #check if backspace was pressed
            print("go back")
            self.set_prev_focus()
            self.current_focus.delete(0, END)
        elif event.keycode == 32: #check if space was pressed - move to next entry
            self.set_next_focus() 

    def update_focus(self, event):
        print("focus updated")
        self.current_focus = event.widget
        
    #set the current focus to be the next entry in the list. however, if it's the last entry than keep the same focus
    def set_next_focus(self):
        print("setting next focus")
        #find the index of the current focus entry
        index = find_entry_index(self.entry_units, self.current_focus)

        if index + 1 < len(self.entry_units): #if there is a next entry in the list (not the last one)
            next_focus = self.entry_units[index + 1].entry
            self.current_focus = next_focus
            next_focus.focus_set() #physically set the focus

    def set_prev_focus(self):
        index = find_entry_index(self.entry_units, self.current_focus)
        
        if index - 1 >= 0:
            prev_focus = self.entry_units[index - 1].entry
            self.current_focus = prev_focus
            prev_focus.focus_set()