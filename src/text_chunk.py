from tkinter import *
from unit import Unit, EntryUnit

from alphabet import alpha_set

from random import choice
colors = ["red", "blue", "green", "yellow", "orange", "pink", "brown", "gray", "purple"]

PAD = 3

class Chunk:

    def __init__(self, root, text_chunk, cryptogram):
        self.frame = Frame(root, bg="lightgray")#, bg=choice(colors))
        self.text_chunk = text_chunk
        self.cryptogram = cryptogram
        self.entry_units = self.make_units()
    
    def make_units(self):
        entry_units = []
        for i, ch in enumerate(self.text_chunk):

            if ch in alpha_set:
                entry_unit = EntryUnit(self.cryptogram, self.frame, ch)
                entry_units.append(entry_unit)
                entry_unit.frame.grid(row = 0, column = i, padx=PAD, pady=PAD, sticky=N)
                #entry_unit.frame.grid(row = 0, column = i, padx=2, ipadx=0, ipady=0, sticky=N)
            else:
                unit = Unit(self.cryptogram, self.frame, ch)
                unit.frame.grid(row = 0, column = i, padx=PAD, pady=PAD, sticky=N)
                #unit.frame.grid(row = 0, column = i, padx=2, ipadx=0, ipady=0, sticky=N)

        return entry_units
