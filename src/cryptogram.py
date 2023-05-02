from tkinter import *

class Cryptogram:
    
    def __init__(self, window, text):
        self.text = text
        self.window = window
        self.entries = self.create_entries()
    
    def create_entries(self):
        entries = []
        for ch in self.text:
            entry = Entry(self.window, width = 3)
            entry.pack(side=LEFT, padx=5, pady=5)
            entries.append(entry)
        return entries