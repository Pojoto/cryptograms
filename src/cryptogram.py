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

            # for ch in chunk:

            #     if ch in alpha_set:
            #         entry_unit = EntryUnit(self.frame, ch)
            #         entry_units.append(entry_unit)
            #         entry_unit.frame.grid(row = row_index, column = col_index, padx=2, sticky=N)
                    
            #         entry_unit.entry.bind("<FocusIn>", self.click_focus)
            #         entry_unit.entry.bind("<Key>", self.check_character)
            #     else:
            #         unit = Unit(self.frame, ch)
            #         unit.frame.grid(row = row_index, column = col_index, padx=2, sticky=N)
                
            #     col_index += 1

            # space = Unit(self.frame, ' ')
            # space.frame.grid(row = row_index, column = col_index, padx=2, sticky=N)
            col_index += (length + 1)
                
        return entry_units         
        
    def clear_answer(self):
        for unit in self.entry_units:
            entry = unit.entry
            entry.delete(0, END)

    def get_answer(self):
        user_answer = ""
        for unit in self.entry_units:
            entry = unit.entry
            user_answer += entry.get().upper()
        return user_answer
    
    def update_focus(self, entry_to_focus):
        if self.current_focus is not None:
            self.current_focus.config(bg="white")
        self.current_focus = entry_to_focus
        entry_to_focus.config(bg="orange")

    def click_focus(self, event):
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