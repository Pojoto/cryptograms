from tkinter import *
from unit import *
from alphabet import alpha_set
from chunk import Chunk


def find_entry_index(units, entry):
    for i, unit in enumerate(units):
        if(unit.entry == entry):
            return i
    return -1


class Cryptogram:

    def __init__(self, root, text):
        self.frame = Frame(root)
        self.entry_units = self.make_chunks(text)
        self.current_focus = None
        self.appearances = self.make_appearances()

    def make_chunks(self, text):
        entry_units = []
        max_row = 15
        row_index = 0
        col_index = 0

        for text_chunk in text.split():

            length = len(text_chunk)

            if col_index + length > 15:
                col_index = 0
                row_index += 1
            elif length > 15:
                print("WORD IS TOO LONG")

            chunk = Chunk(self.frame, text_chunk, self)

            chunk.frame.grid(row = row_index, column = col_index, padx=2, sticky=N, columnspan=length)

            entry_units.extend(chunk.entry_units)

            col_index += (length + 1)
                
        return entry_units        

    def copy_entry(self, label_char, user_char):
        for entry_unit in self.appearances[label_char]:
            entry_unit.entry.delete(0, END)
            entry_unit.entry.insert(0, user_char)
        

    def make_appearances(self):
        appearances = {}
        for entry_unit in self.entry_units:
            letter = entry_unit.char
            if letter in alpha_set:
                if letter in appearances:
                    appearances[letter].add(entry_unit)
                else:
                    appearances[letter] = {entry_unit}
        
        return appearances
                

    def clear_answer(self):
        for entry_unit in self.entry_units:
            entry = entry_unit.entry
            entry.delete(0, END)

    def get_answer(self):
        user_answer = ""
        for entry_unit in self.entry_units:
            entry = entry_unit.entry
            user_answer += entry.get().upper()
        return user_answer
    
    def update_focus(self, entry_to_focus):
        if self.current_focus is not None:
            letter = self.current_focus.char
            self.current_focus.config(readonlybackground=self.frame["bg"])
        self.current_focus = entry_to_focus
        print("orange")
        entry_to_focus.config(readonlybackground="orange")

    def click_focus(self, event):
        print("focus")
        self.update_focus(event.widget)
        
    #set the current focus to be the next entry in the list. however, if it's the last entry than keep the same focus
    def set_next_focus(self):
        #find the index of the current focus entry
        index = find_entry_index(self.entry_units, self.current_focus)

        if index + 1 < len(self.entry_units): #if there is a next entry in the list (not the last one)
            next_focus = self.entry_units[index + 1].entry
            self.update_focus(next_focus)
            next_focus.focus_set() #physically set the focus

    def set_prev_focus(self):
        index = find_entry_index(self.entry_units, self.current_focus)
        
        if index - 1 >= 0:
            prev_focus = self.entry_units[index - 1].entry
            self.update_focus(prev_focus)
            prev_focus.focus_set()
    
    def self_destruct(self):
        self.frame.destroy()