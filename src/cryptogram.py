from tkinter import *
from unit import *
from alphabet import alpha_set
from text_chunk import Chunk


class Cryptogram:

    def __init__(self, root, text):
        self.frame = Frame(root)
    
        self.entry_units = self.make_chunks(text)

        #current focus is an entry unit object
        self.current_focus = None

        #appearances is a dictionary with keys being letters, values being sets of entry units sharing that letter
        self.appearances = self.make_appearances()

        self.add_freqs()

    def make_chunks(self, text):
        entry_units = []
        max_row = 15
        row_index = 0
        col_index = 0

        row = Frame(self.frame)

        row.pack(anchor=W, padx=6, pady=4)

        for i, text_chunk in enumerate(text.split()):

            length = len(text_chunk)

            if col_index + length > max_row:
                
                #start a new row
                row = Frame(self.frame)

                row.pack(anchor=W, padx=6, pady=4)

                col_index = 0
                row_index += 1

            elif length > max_row:
                print("WORD IS TOO LONG")

            chunk = Chunk(self, row, text_chunk)

            chunk.frame.pack(side=LEFT)

            entry_units.extend(chunk.entry_units)

            col_index += length

            #check if we need to add a space unit - if the word takes up till the end of the row, then don't need to add a space at the end
            if col_index < max_row:
                space_unit = SpaceUnit(self, row, ' ')
                space_unit.frame.pack(side=LEFT)
            
            col_index += 1
                
        return entry_units  

    def copy_entry(self, label_char, user_char):
        for entry_unit in self.appearances[label_char]:
            entry_unit.entry.config(state="normal")
            entry_unit.entry.delete(0, END)
            entry_unit.entry.insert(0, user_char)
            entry_unit.entry.config(state="readonly")
        
    #each key in the dict is a letter, the values are a list of all the entry units of that letter in the cryptogram
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

    def add_freqs(self):
        for entry_unit in self.entry_units:
            freq = len(self.appearances[entry_unit.char])
            entry_unit.add_freq(freq)
                

    def clear_answer(self):
        for entry_unit in self.entry_units:
            entry = entry_unit.entry
            entry.config(state="normal")
            entry.delete(0, END)
            entry.config(state="readonly")

    def get_answer(self):
        user_answer = ""
        for entry_unit in self.entry_units:
            entry = entry_unit.entry
            user_answer += entry.get().upper()
        return user_answer
    
    def update_focus(self, unit_to_focus):
        if self.current_focus is not None:
            oldletter = self.current_focus.char
            for entry_unit in self.appearances[oldletter]:
                entry_unit.entry.config(readonlybackground=self.frame["bg"])
        self.current_focus = unit_to_focus
        newletter = unit_to_focus.char
        print("orange")
        for entry_unit in self.appearances[newletter]:
            entry_unit.entry.config(readonlybackground="orange")
        unit_to_focus.entry.config(readonlybackground="red")

    def click_focus(self, entry_unit):
        print(entry_unit.char)
        print("focus")
        self.update_focus(entry_unit)
        
    #set the current focus to be the next entry in the list. however, if it's the last entry than keep the same focus
    def set_next_focus(self):

        start = self.current_focus

        #find the index of the current focus entry
        index = self.entry_units.index(self.current_focus)
        index += 1

        #get the next entry unit in the list, could wrap around to start
        current = self.entry_units[index % len(self.entry_units)]
        while current != start:

            if len(current.entry.get()) == 0:
                break

            index = (index + 1) % len(self.entry_units)
            current = self.entry_units[index]
        
        self.update_focus(current)
        current.entry.focus_set()

    def set_prev_focus(self):
        index = self.entry_units.index(self.current_focus)
        
        if index - 1 >= 0:
            prev_focus = self.entry_units[index - 1]
            self.update_focus(prev_focus)
            prev_focus.entry.focus_set()
    
    def self_destruct(self):
        self.frame.destroy()